#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-20 下午3:43
# @Author  : fixdq
# @File    : setting.py
# @Software: PyCharm

import os
import sys
BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)
from tcpserver import server

if __name__ == '__main__':
    server.run()