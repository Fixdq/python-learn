#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


class People:
    def __init__(self, name):
        self.name = name


class Student(People):
    def __init__(self, name=None):
        super().__init__(name)


stu = Student('kk')
name = 's'
res = isinstance(stu, object)
res1 = isinstance(stu, People)
res2 = isinstance(name, object)

print(res)
print(res1)
print(res2)

re = issubclass(People,Student )
print(re)
