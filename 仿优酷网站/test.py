#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : test.py
# @Software: PyCharm
import os

from conf import settings

path = os.path.join(settings.BASE_DB, '')
print(path)

info = os.stat('/home/fixd/project/python_learn/仿优酷网站/db/notice/')
print(type(info))
print(info)

DIR = "/home/fixd/project/python_learn/仿优酷网站/db/notice/"


def compare(x, y):
    stat_x = os.stat(DIR + "/" + x)
    stat_y = os.stat(DIR + "/" + y)
    if stat_x.st_ctime < stat_y.st_ctime:
        return -1
    elif stat_x.st_ctime > stat_y.st_ctime:
        return 1
    else:
        return 0


iterms = os.listdir(DIR)

# iterms.sort(key=lambda obj: os.stat(os.path.join(DIR, obj)).st_ctime, reverse=True)
iterms.sort(reverse=True)
for iterm in iterms:
    print(iterm)
