#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-27 下午8:23
# @Author  : fixdq
# @File    : 列表推导式.py
# @Software: PyCharm


lis1 = [1, 2, 3, 4, 5, ]
lis2 = [1, 2, 3, 4, 5, ]

r = [(l1, l2) for l1 in lis1 for l2 in lis2]

print(r)
