#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : server_mult.py
# @Software: PyCharm

from socket import *

ip_port = ('127.8.2.1', 15555)
client = socket(AF_INET, SOCK_STREAM)
client.connect(ip_port)

while True:
    msg = input('>>>>:').strip()
    if not msg :continue
    client.send(msg.encode('utf-8'))

    res = client.recv(1024)

    print(res.decode('utf-8'))
