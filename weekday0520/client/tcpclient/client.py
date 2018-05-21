#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-20 下午3:10
# @Author  : fixdq
# @File    : client.py
# @Software: PyCharm

import socket
from conf import setting


def get_conn():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(setting.ip_port)
    return conn
