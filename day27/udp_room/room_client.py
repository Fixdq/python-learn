#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : room_client.py
# @Software: PyCharm

from socket import *
ip_port = ('192.168.12.35', 8080)
room_client = socket(AF_INET,SOCK_DGRAM)

while True:

    msg = input('>>>>>:').strip()
    if not msg:continue
    room_client.sendto(msg.encode('utf-8'),ip_port)
    res ,addr = room_client.recvfrom(1024)
    print(res.decode('utf-8'))
