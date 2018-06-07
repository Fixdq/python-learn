#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/6/4


"""
1. os和sys都是干什么的？
2. 你工作中都用过哪些内置模块？
json time datatime hashlib logging
3. 有没有用过functools模块？

"""

import os
import sys
import functools
print(os.path.dirname(__file__))
print(os.path.getsize(r"/home/fixd/workspace/python_learn/day57"))
print(os.path.exists(r'/home/fixd/workspace/python_learn/day57'))
print(os.listdir(r'/home/fixd/workspace/python_learn/day57'))


print(sys.path)
print(sys.stdout)





