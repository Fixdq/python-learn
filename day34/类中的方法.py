#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : 类中的方法.py
# @Software: PyCharm


class T(object):
    def __init__(self, name, pwd):
        self.pwd = pwd
        self.name = name


    @classmethod
    def get_T(cls):
        return cls('127.0.0.1', '8989')

    @staticmethod
    def say_hi():
        return 'hello world'


t = T('name', 'pwd')
t.say_hi()
T.say_hi()
t = T.get_T()
