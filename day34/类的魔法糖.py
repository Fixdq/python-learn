#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : 类的魔法糖.py
# @Software: PyCharm

class Stu(object):
    def __init__(self, name, wt, ht):
        self.__name = name
        self.wt = wt
        self.ht = ht

    @property
    def bmi(self):
        return self.wt / (self.ht ** 2)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name == name

    @name.deleter
    def name(self):
        del self.__name


stu = Stu('tt',70,1.75)
print(stu.bmi)