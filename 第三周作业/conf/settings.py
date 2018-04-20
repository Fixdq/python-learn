#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

"""
配置信息
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DB = os.path.join(BASE_DIR, 'db')
BASE_STU = os.path.join(BASE_DIR, 'db', 'account')
BASE_TEA = os.path.join(BASE_DIR, 'db', 'teacher')
BASE_SCH = os.path.join(BASE_DIR, 'db', 'school')

# 账户授权类型 1 student 2 teacher 0 admin
AUTH_TYPE = [0, 1, 2]

