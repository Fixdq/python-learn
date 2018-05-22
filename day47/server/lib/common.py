#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-22 上午11:46
# @Author  : fixdq
# @File    : common.py
# @Software: PyCharm
import hashlib
import json
import struct
import time


def send(conn, dic):
    json_bytes = json.dumps(dic).encode()
    conn.send(struct.pack('i', json_bytes))
    conn.send(json_bytes)


def get_uuid(args):
    md5 = hashlib.md5()
    md5.update(args)
    md5.update(str(time.clock()).encode())
    return md5.hexdigest()


