#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-25 下午8:21
# @Author  : fixdq
# @File    : start.py
# @Software: PyCharm
import os
import sys

BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)

from server import tcpserver

if __name__ == '__main__':
    tcpserver.run()
