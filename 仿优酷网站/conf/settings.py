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
BASE_LOG = os.path.join(BASE_DIR, 'log')
BASE_VIDEOS = os.path.join(BASE_DB, 'videos')
# BASE_VIDEOS_MANAGER = os.path.join(BASE_DB, 'videos','videos_manager')
BASE_NOTICE = os.path.join(BASE_DB, 'notices')
# BASE_NOTICE_MANAGER = os.path.join(BASE_DB, 'notices','notices_manager')
