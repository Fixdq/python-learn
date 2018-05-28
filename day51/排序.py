#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-28 上午9:01
# @Author  : fixdq
# @File    : 排序.py
# @Software: PyCharm
from operator import itemgetter,attrgetter
l1 = [11, 2, 3, 22, 2, 4, 11, 3, ]
l2 = list(set(l1))
l2.sort(key=l1.index)
print(l2)

l3 = [
    {'name': 'ss', 'age': 18},
    {'name': 'ss', 'age': 68},
    {'name': 'ss', 'age': 12},
    {'name': 'ss', 'age': 48},
]

# l3.sort(key=lambda x: x['age'])
# print(l3)

