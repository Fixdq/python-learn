#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
from db import db_handler


class BaseClass:
    def save(self):
        db_handler.save(self)

    @classmethod
    def get_obj_by_name(cls, name):
        return db_handler.select(name, cls.__name__.lower())


class School(BaseClass):
    def __init__(self, name, address):
        self.address = address
        self.name = name
        self.courses = []

    def add_course(self, course_name):
        self.courses.append(course_name)
        self.save()


class Course(BaseClass):
    def __init__(self, name):
        self.name = name


class Teacher(BaseClass):
    def __init__(self, name, password):
        self.name = name
        self.password = password


class Admin(BaseClass):
    def __init__(self, name, pwd):
        self.password = pwd
        self.name = name
        self.save()  # 将产生的新对象进行保存

    def create_school(self, school_name, school_address):
        school = School(school_name, school_address)
        school.save()

    def create_course(self, course_name):
        course = Course(course_name)
        course.save()

    def create_teacher(self, name, password):
        teacher = Teacher(name, password)
        teacher.save()
