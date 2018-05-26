#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-25 下午8:22
# @Author  : fixdq
# @File    : common_interface.py
# @Software: PyCharm
from lib import common
def login(conn, data):
    print(list(data))

    send_data = {'flag': True,
                 'msg': 'hello'}
    common.send(conn,send_data)
