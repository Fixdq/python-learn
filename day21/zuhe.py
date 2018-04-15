#!/usr/bin/env python3
# encoding: utf-8
# by fixdq



class Date:
    def __init__(self, year, mon, day):
        self.year = year
        self.mon = mon
        self.day = day

    def tell_birth(self):
        print("""%s-%s-%s"""
              %
              (
                  self.year,
                  self.mon,
                  self.day,
              ))


class OldPerson:
    school = "oldboy"

    def __init__(self, name, age, sex, ):
        self.name = name
        self.age = age
        self.sex = sex


class Student(OldPerson):
    """
    学生类
    """

    def __init__(self, name, age, sex, score):
        super().__init__(name, age, sex, )
        self.score = score


class Teacher(OldPerson):
    """
    学生类
    """

    def __init__(self, name, age, sex, level, salary):
        super().__init__(name, age, sex, )
        self.score = level
        self.score = salary


class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def tell_info(self):
        print("""
=============课程信息=============
名字：%s
周期：%s
价格：%s
""" % (
            self.name,
            self.period,
            self.price
        ))


birth = Date(1998, 3, 2)
course = Course('linux', 5, 200)
stu1 = Student('马六', 20, 'male', 90)

stu1.birth = birth
stu1.course = course

stu1.course.tell_info()
stu1.birth.tell_birth()
