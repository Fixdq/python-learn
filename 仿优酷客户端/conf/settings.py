#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : settings.py
# @Software: PyCharm

import os
IP_PORT = ('127.168.145.1',8080)
max_buffer_size = 8192
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DB = os.path.join(BASE_DIR, 'db')
