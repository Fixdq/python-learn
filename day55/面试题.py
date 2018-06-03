#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-6-1 上午8:32
# @Author  : fixdq
# @File    : 面试题.py
# @Software: PyCharm
lis = []
for i in range(4):
    l2 = []
    for k in range(5):
        l2.append(i * k)
    lis.append(l2)

print(lis)
res = [[i * k for k in range(5)] for i in range(4)]
print(res)
