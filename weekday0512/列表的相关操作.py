#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : 列表的相关操作.py
# @Software: PyCharm

ls = [1, 2, 3, 4, 5, 6, 7, 2]

print(ls)
print(ls[::-1])
print(ls.reverse())

ap = [11, 211, 22]

ls.insert(3, ap)
print(ls)
ls.pop()
print(ls)

ls_str = [str(l) for l in ls]

print(ls_str)
ls_str.remove('2')
print(ls)
print(ls_str)

l2 = [1, 2, 3, 4, 2, 3, 4]
ls_str2 = [str(l) for l in l2]
print(ls_str2)
l2_dic = set(ls_str2)
print(l2_dic)
ls_str2_ = list(l2_dic)
print(ls_str2_)
