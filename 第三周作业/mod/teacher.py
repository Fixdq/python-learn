#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from mod import people
from db import db_handler
from conf import settings

"""
老师类
"""

db = db_handler.DbHandler(settings.BASE_TEA)


class Teacher(people.People):
    def __init__(self, name, age, gender, teaching_course=None):
        """
        
        :param name: 
        :param age: 
        :param gender: 
        :param teaching_course: []
        """
        super().__init__(name, age, gender)
        self.teaching_course = teaching_course

    def add_course(self, course):
        # 将课程信息添加到self
        self.teaching_course.append(course)
        # 讲老师信息写入文件
        db.dump_data(self, self.name)

    def show_info(self):
        print("""
            姓名：%s
            年龄：%s
            性别：%s
            教授的课程：%s
        """ % (
            self.name,
            self.age,
            self.gender,
            self.teaching_course,
        ))
