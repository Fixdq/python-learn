#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from mod import people
from conf import settings

"""
学生类
"""
from db import db_handler

db = db_handler.DbHandler(settings.BASE_STU)


class Student(people.People):
    def __init__(self, name, age, gender='male', study_course=None):
        """
        
        :param name: 
        :param age: 
        :param gender: 
        :param study_course:{}
        """
        super().__init__(name, age, gender)
        self.study_course = study_course
        self.score = 0

    def change_score(self, score_new):
        """
        修改分数
        :param score_new: 
        :return: 
        """
        self.score = score_new
        db.dump_data(self, self.name)

    def choice_course(self, course):
        """
        选课
        :param course: 
        :return: 
        """
        # 将课程信息添加到self
        if self.study_course is None:
            self.study_course = {course.name: course}
        else:
            self.study_course[course.name] = course
        db.dump_data(self, self.name)

    def update_info(self):
        """
        更新
        :return: 
        """
        db.dump_data(self, self.name)

    def show_info(self):
        """
        显示个人信息
        :return: 
        """
        print('-----------------------------')
        print('个人信息')
        print("""
姓名：%s
年龄：%s
性别：%s
        """ % (
            self.name,
            self.age,
            self.gender,
        ))

        if self.study_course is not None:
            print('课程信息')
            for k in self.study_course:
                # course = self.study_course
                print("名称：%s" % k)
                print("周期：%s" % self.study_course[k].period)
                print("价格：%s" % self.study_course[k].price)
        print('-----------------------------')
