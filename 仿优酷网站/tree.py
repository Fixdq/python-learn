#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : tree.py
# @Software: PyCharm

import os


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        dir_indent = "|   " * (level - 1) + "+-- "
        file_indent = "|   " * level + "+-- "
        if not level:
            print('.')
        else:
            print('{}{}'.format(dir_indent, os.path.basename(root)))
        for f in files:
            print('{}{}'.format(file_indent, f))


list_files('/home/fixd/project/python_learn/仿优酷网站')