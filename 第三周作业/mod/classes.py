#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

"""
班级类
"""


class Classes:
    def __init__(self, name, course, teachers=None, students=None):
        """
        
        :param name: 
        :param course: str
        :param teachers:[]
        :param students: []
        """
        self.students = students
        self.course = course
        self.teachers = teachers
        self.name = name

    def show_classes(self):
        print('班级名称：%s,课程：%s，老师：%s' % (self.name, self.course.name, self.teachers))

    def add_student(self, student):
        """
        添加student
        :param student: 
        :return: 
        """
        self.students.append(student)

    def add_teacher(self, teacher):
        """
        添加老师
        :param teacher: s
        :return: 
        """
        if self.teachers is None:
            self.teachers = [teacher]
        else:
            self.teachers.append(teacher)
