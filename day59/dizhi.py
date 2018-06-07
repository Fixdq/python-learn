#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-6-7 上午8:26
# @Author  : fixdq
# @File    : dizhi.py
# @Software: PyCharm
import re
from collections import Counter
urls = {}

with open('/home/fixd/workspace/python_learn/day59/xx.log','r',encoding='utf-8') as f:
        us = f.read()
        lis = re.findall(r'https://.*?/.*?',us)
        print(lis)