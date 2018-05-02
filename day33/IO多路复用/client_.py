#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : client_.py
# @Software: PyCharm
import os
from socket import socket

s = socket()
s.connect_ex(('127.0.1.1', 8080))


while True:
    print(' ----->%s' % os.getpid())
    s.send(b'pppppp')
    res = s.recv(1024)
    print(res.decode('utf-8'))

s.close()