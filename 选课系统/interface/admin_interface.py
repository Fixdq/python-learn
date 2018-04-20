#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


from db import models
from lib import common


def register_interface(name, pwd):
    user_obj = models.Admin.get_obj_by_name(name)
    if user_obj:
        return False, '用户名已存在'
    # 添加用户信息
    models.Admin(name, pwd)
    return True, '注册成功'


def create_school_interface(admin_name, name, address):
    school = models.School.get_obj_by_name(name)
    if school:
        return False, '学校已存在'
    # 获取管理员对象
    admin = models.Admin.get_obj_by_name(admin_name)
    # 通过管理员进行保存学校的对象
    admin.create_school(name, address)
    return True, '学校已经创建成功'


def create_teacher_interface(admin_name, name, password=123):
    teacher = models.Teacher.get_obj_by_name(name)
    if teacher:
        return False, '老师已存在'
    # 获取管理员对象
    admin = models.Admin.get_obj_by_name(admin_name)
    # 通过管理员进行保存学校的对象
    admin.create_teacher(name, password)
    return True, '老师创建成功'


def get_all_school():
    """
    返回学校的全部列表
    :return: 
    """
    return common.get_all_file('school')


def create_course(admin_name, school_name, course_name):
    # 先判断课程是否存在
    course = models.Course.get_obj_by_name(course_name)
    if course:
        return False, '课程已经存在'
    admin = models.Admin.get_obj_by_name(admin_name)
    admin.create_course(course_name)

    school = models.School.get_obj_by_name(school_name)
    school.add_course(course_name)
    return True, '课程保存成功!'
