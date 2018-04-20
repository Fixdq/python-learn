#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


class People:
    def __init__(self, name, age, gender):
        self.gender = gender
        self.age = age
        self.name = name


class Teacher(People):
    def __init__(self, name, age, gender, salary, lv):
        super().__init__(name, age, gender)
        self.lv = lv
        self.salary = salary
        self.courses = []

    def change_score(self):
        print('%s is changing score' % self.name)

    def show_course_info(self):
        for course in self.courses:
            course.show_info()


class Student(People):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.courses = []

    def show_course_info(self):
        for course in self.courses:
            course.show_info()


class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def show_info(self):
        print("名称：%s,周期：%s，价格：%s" % (self.name, self.period, self.price))


tea = Teacher("alex", 32, 'male', 3000, 5)
stu1 = Student('kk', 33, 'male')
linux = Course('Linux','6个月',90000)
python = Course('python','6个月',90000)

tea.courses.append(python)
tea.courses.append(linux)

print(tea.courses)

for cours in tea.courses:
    cours.show_info()

tea.show_course_info()












