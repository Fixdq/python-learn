#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-29 上午8:38
# @Author  : fixdq
# @File    : test.py
# @Software: PyCharm

def extend_list(v, li=[]):
    li.append(v)
    return li

list1 = extend_list(10)
list2 = extend_list(123,[])
list3 = extend_list('a')

print(list1)
print(list2)
print(list3)

print(list1 is list3)

list11 = ["a", "b", "c", "d", "e"]
print(list11[10:])



