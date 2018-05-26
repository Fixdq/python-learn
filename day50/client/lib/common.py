#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-25 下午8:24
# @Author  : fixdq
# @File    : start.py
# @Software: PyCharm
import json
import struct


def send_back(conn, data, file=None):
    data_bytes = json.dumps(data).encode('utf-8')
    conn.send(struct.pack('i', len(data_bytes)))
    conn.send(data_bytes)

    if file:
        with open(file, 'rb') as f:
            for line in f:
                conn.send(line)

    len_bytes = conn.recv(4)
    head = conn.recv(struct.unpack('i', len_bytes)[0]).decode('utf-8')
    return json.loads(head)
