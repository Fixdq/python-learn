#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
import os

from mod import school as s
from mod import course as c
from mod import teacher as t
from mod import classes as cla
from db import db_handler
from conf import settings

db = db_handler.DbHandler(settings.BASE_SCH)


def choice_school():
    print("--------------选择学校--------------")
    school_list = os.listdir(settings.BASE_SCH)
    if not school_list:
        print("还没有校区！")
        return False
    else:
        print(school_list)
    flag = True
    while flag:
        choice_school_name = input('请选择校区：').strip()
        if choice_school_name not in school_list:
            print('请正确选择校区！')
            continue
        print('您已选择：%s' % choice_school_name)
        return db.load_data(choice_school_name)


def create_school():
    print("--------------创建学校--------------")
    school_list = os.listdir(settings.BASE_SCH)
    if not school_list:
        print("还没有校区！")
    else:
        print(school_list)
    print('开始创建校区！')
    flag = True
    while flag:
        name = input('请输入校区名称（b，返回）：').strip()
        if 'b' == name:
            return
        if name in os.listdir(settings.BASE_SCH):
            print('校区已经存在')
            continue
        city = input('请输入校区所在城市：').strip()

        school = s.School(name, city)
        school.save()
        flag = False
        print('校区创建成功！')
    print("----------------------------------")


def create_course():
    # 选择校区
    school = choice_school()
    print("已存在课程")
    school.show_courses()
    print("--------------创建--------------")
    course_name = input('请输入课程名称(b，返回）:').strip()
    if 'b' == course_name:
        return
    course_period = input('请输入课程周期').strip()
    course_price = input('请输入课程价格').strip()

    course = c.Course(course_name, course_period, course_price)

    if school.courses is None:
        course_dic = {course.name: course}
        school.courses = course_dic
    else:
        school.courses[course.name] = course
    school.save()
    print("添加课程成功！")
    print("--------------end------------------")


def create_classes():
    # 选择校区
    school = choice_school()
    print("已存在班级")
    school.show_classses()
    print("--------------创建--------------")
    classses_name = input('请输入班级名称(b,返回)：').strip()
    if 'b' == classses_name:
        return

    classes_course = None
    # 选择课程
    courses = school.show_courses()
    if courses is not None:
        while True:
            course_name = input('请选择班级课程：').strip()
            if course_name not in list(courses.keys()):
                print('请正确输入课程！')
                continue
            classes_course = course_name
            break

    # 选择老师
    class_teacher_name = None
    teachers = school.show_teachers()
    if teachers is not None:
        while True:
            classses_teacher = input('请选择讲师名称').strip()
            if classses_teacher not in list(teachers.keys()):
                print('请正确选择讲师')
                continue
            class_teacher_name = teachers[classses_teacher].name
            break

    classes = cla.Classes(classses_name, classes_course)
    classes.add_teacher(class_teacher_name)
    if school.classes is None:
        classes_dic = {classes.name: classes}
        school.classes = classes_dic
    else:
        school.classes[classes.name] = classes
    school.save()
    print("添加课程成功！")
    print("--------------end------------------")


def create_teacher():
    # 选择校区
    school = choice_school()
    print("已存在讲师")
    school.show_teachers()
    print("--------------创建--------------")
    name = input('请输入讲师的姓名(b,返回)：').strip()
    if 'b' == name:
        return
    age = input('请输入讲师年龄').strip()
    gender = input('请选择讲师的性别（male/female）：').strip()
    teacher = t.Teacher(name, age, gender)
    courses = school.show_courses()
    if courses is not None:
        while True:
            course_name = input('请选择教授课程：').strip()
            if course_name not in list(courses.keys()):
                print('请正确输入课程！')
                continue
            if teacher.teaching_course is None:
                course_list = [course_name]
                teacher.teaching_course = course_list
            else:
                teacher.teaching_course.append(course_name)
            break
    if school.teachers is None:
        teacher_dic = {teacher.name: teacher}
        school.teachers = teacher_dic
    else:
        school.teachers[teacher.name] = teacher
    school.save()
    print("添加讲师成功！")
    print("--------------end------------------")

#
# def create_student():
#     print('create_student')
