#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : classtest.py
# @Software: PyCharm
from typing import Any


class T(type):
    def __new__(cls, o: object) -> type:
        return super().__new__(cls, o)


class Fo(object, metaclass=T):
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('%s say hello' % self.name)


f = Fo('x')
f.say_hi()
