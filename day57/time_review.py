#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-6-5 下午7:23
# @Author  : fixdq
# @File    : time_review.py
# @Software: PyCharm
#
import time

print(time.time())  # 时间戳
print(time.localtime())  # 本地结构化时间
print(time.localtime())  # UTC时区的结构化时间

print(time.strftime("%Y-%m-%d %X"))  # 自定义结构化时间
# print(time.strptime())  # 自定义结构化时间

print(time.ctime())
print(time.ctime(time.time()))

import datetime

print(datetime.datetime.now())

import sys

print(sys.version)
print(sys.maxsize)
print(sys.path)
print(sys.platform)





import hashlib

md5 = hashlib.md5()
md5.update('梁书东是个DSB'.encode())
print(md5.hexdigest())
import os

bs = os.path.dirname(__file__)
