#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-29 下午9:15
# @Author  : fixdq
# @File    : 深浅拷贝.py
# @Software: PyCharm
import copy
# 赋值操作
a = [1, 2, 3]
b = list(a)
print(id(a), id(b))

for j, k in zip(a, b):
    print(id(j), id(k))


# import copy   深copy
c = [1, 2, 3]
d = copy.deepcopy(c)
print(id(c), id(d))
for j, k in zip(a, b):
    print(id(j), id(k))

res = a.index

print(res)