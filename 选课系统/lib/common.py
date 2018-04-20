#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
import os
from conf import settings


def login(type):
    from core import admin, student, teacher
    def is_auth(func):
        def wrapper(*args, **kwargs):
            if type == "admin":
                if admin.admin_info['name'] is not None:
                    return func(*args, **kwargs)
                else:
                    print("请先登录!")
                    admin.login()
            elif type == "student":
                if student.student_info['name']:
                    return func(*args, **kwargs)
                else:
                    print("请先登录!")
                    student.login()
            elif type == "teacher":
                if teacher.teacher_info['name']:
                    return func(*args, **kwargs)
                else:
                    print("请先登录!")
                    teacher.login()

        return wrapper

    return is_auth


def get_all_file(type):
    path = os.path.join(settings.BASE_DB, type)
    if not os.path.isdir(path):
        os.mkdir(path)
    return os.listdir(path)
