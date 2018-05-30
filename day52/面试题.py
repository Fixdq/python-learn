#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-30 上午8:34
# @Author  : fixdq
# @File    : 面试题.py
# @Software: PyCharm


def func(m):
    for k,v in m.items():
        m[k+2] = v+2


m = {1: 2, 3: 4}
l = m  # 浅拷贝
l[9] = 10
func(l)
m[7] = 8


print("l:", l)
print("m:", m)

