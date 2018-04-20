#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
import os
from mod import student
from conf import settings
from db import db_handler
from mod import school as sh
from core import admin

db = db_handler.DbHandler(settings.BASE_STU)


def register_student():
    flag = True
    while flag:
        print("--------------学生注册---------------")
        name = input('请输入你的姓名：').strip()
        age = input('请输入您年龄').strip()
        gender = input('请选择您的性别（male/female）：').strip()
        path = os.path.join(settings.BASE_STU, name)
        if os.path.isfile(path):
            print("学生已存在！")
            continue

        stu = student.Student(name, age, gender)
        while flag:
            # 显示用户信息
            stu.show_info()
            confirm = input("确定注册（y/n）")
            if confirm not in ['y', 'n']:
                print('输入不正确！')
                continue
            if confirm == 'n':
                break
            if confirm == 'y':
                # 保存学生的信息
                stu.update_info()
                flag = False
                print('注册成功！')
                break


def choice_course():
    flag = True
    while flag:
        stu_name = input('请输入您的名字').strip()
        path = os.path.join(settings.BASE_STU, stu_name)
        if not os.path.isfile(path):
            print("名字不存在！")
            continue
        stu = db.load_data(path)
        # 选择校区
        school = admin.choice_school()
        print("--------------已存在课程--------------")
        courses = school.show_courses()
        while flag:
            course = input('请选择课程：').strip()
            if course not in list(courses.keys()):
                print("请正确选择课程！")
                continue
            # 绑定学生和课程信息
            stu.choice_course(courses[course])
            # 绑定学生school
            if school.students is None:
                school.students = {stu.name: stu}
            else:
                school.students[stu.name] = stu
            school.save()
            print('课程选择成功！')
            break

        # l = (key for key in school.classes if school.classes[key].name == course)
        # print(list(l))
        break


def show_info():
    print("--------------学生信息---------------")
    name = input("请输入你的名字：").strip()
    stu = db.load_data(name)
    stu.show_info()
    print("---------------end------------------")
