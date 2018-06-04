#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-6-4 上午8:33
# @Author  : fixdq
# @File    : 每日练习题.py
# @Software: PyCharm

import time


def decoration_time(func):
    def wrapper(*args, **kwargs):
        print(time.strftime("%Y-%m-%d", time.localtime()))
        func(*args, **kwargs)
        print(time.strftime("%Y-%m-%d", time.localtime()))

    return wrapper


@decoration_time
def f():
    print("2018-06-04")


f()
