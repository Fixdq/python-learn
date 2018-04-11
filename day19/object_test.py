#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


class Student:
    school = 'oldboy'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def learn(self):
        print('%s is  learning, %s  is  a  chusheng ' % (self.name,self.age))

stu = Student('Yx',100000)
stu.learn()
stu1 = Student('4x',100000)
stu1.learn()

print(id(stu.learn))
print(stu.learn)

print(id(stu1.learn))
print(stu1.learn)


stu2 = Student
print(stu1)