#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-25 下午8:23
# @Author  : fixdq
# @File    : common.py
# @Software: PyCharm
import json
import struct


def send(conn, data):
    data_bytes = json.dumps(data).encode('utf-8')
    conn.send(struct.pack('i', len(data_bytes)))
    conn.send(data_bytes)
