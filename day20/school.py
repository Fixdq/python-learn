#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


class OldboyPerson:
    """
    抽象父类
    """
    school = "oldboy"

    def __init__(self, name=None, gender=None, age=None):
        self.name = name
        self.age = age
        self.gender = gender

    def f1(self):
        print('par.f1')

    def f2(self):
        print('par.f2')
        self.f1()


class Teacher(OldboyPerson):
    """
    老师类
    """

    def __init__(self, name, age, gender, level, sarlary):
        OldboyPerson.__init__(self, name, age, gender)
        # super().__init__(name, age, gender)
        # 新属性
        self.level = level
        self.sarlary = sarlary

    def change_score(self, student):
        pass


class Student(OldboyPerson):
    """
    学生类
    """

    def f1(self):
        super().f1()
        print('stu.f1')

    def register(self):
        pass

    def choose(self):
        pass


stu = Student('fixd', 15, '0')
#
# stu.f1()
# stu.f2()


# teacher = Teacher('egonn',18,'0',9,10000000)
# print(teacher.name)