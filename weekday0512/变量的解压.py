#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : 变量的解压.py
# @Software: PyCharm

nums = [1, 2, 3, 4]

a, b, c, d = nums

print(a, b, c, d)
a, *_, b = nums

print(a, b)

strs = "0123456789"
print(strs[1:])
print(strs[0:])
print(strs[0:-1])
print(strs[::-2])
print(strs[::-1][-4::])
# 中括号内 单个值 表示  取对应索引的值
# 关于切片的理解     中括号内  顾左边不顾右边   切片参数 左边<右边
# 字符串翻转  切片参数 步长  -1 即可
