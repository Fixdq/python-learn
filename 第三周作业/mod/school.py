#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

"""
学校类
"""
from db import db_handler
from conf import settings

db = db_handler.DbHandler(settings.BASE_SCH)


class School:
    def __init__(self, school_name, city_name, teachers=None, courses=None, students=None, classes=None):
        """

        :param school_name: str
        :param city_name: str
        :param teachers: {}
        :param courses: {}
        :param students: {}
        :param classes: {}
        """
        self.school_name = school_name
        self.city_name = city_name
        self.teachers = teachers
        self.courses = courses
        self.students = students
        self.classes = classes



    # 保存校区信息
    def save(self):
        db.dump_data(self, self.school_name)

    def show_courses(self):
        print("-------------课程信息-----------")
        if not self.courses:
            print("还没有课程")
            return
        for k in self.courses:
            print("名称：%s,周期：%s，价格：%s" % (k, self.courses[k].period, self.courses[k].price))
        print("------------------------------")
        return self.courses

    def show_classses(self):
        print("-------------班级信息-----------")
        if not self.classes:
            print("还没有班级")
            return
        for k in self.classes:
            print("名称：%s,讲师：%s" % (k, self.classes[k].teachers))
            # self.classes[k].show_classes()
        print("------------------------------")
        return self.classes

    def show_teachers(self):
        print("-------------讲师信息-----------")
        if not self.teachers:
            print("还没有讲师")
            return
        for teacher in self.teachers:
            print("名称：%s,教授课程：%s" % (teacher, self.teachers[teacher].teaching_course))
        print("------------------------------")
        return self.teachers

    def show_info(self):
        print("""
            校区名称：
            所在城市：
            拥有讲师：
            拥有课程：
            拥有班级：
        """ % (
            self.school_name,
            self.city_name,
            list(self.teachers.keys()),
            list(self.courses.keys()),
            list(self.classes.keys()),
        ))
