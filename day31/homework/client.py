#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : client.py
# @Software: PyCharm

from socket import *


client = socket(AF_INET, SOCK_STREAM)

client.connect(('127.0.0.1', 8080))
# print('start')
# is_ok = client.recv(1024)
# print(is_ok.decode('utf-8'))

while True:
    msg = input('>>>：').strip()
    if not msg : continue
    client.send(msg.encode('utf-8'))
    res = client.recv(1024)
    print(res.decode('utf-8'))