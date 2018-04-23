#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : udp_room.py
# @Software: PyCharm

from socket import *

ip_pool = []
ip_port = ('192.168.12.35', 8080)
room_server = socket(AF_INET, SOCK_DGRAM)
room_server.bind(ip_port)

while True:
    msg, addr = room_server.recvfrom(1024)
    print(addr[0], '连接了')
    if not msg: continue
    if addr[0] not in ip_pool:
        ip_pool.append(addr)
    # 转发信息给其他用户
    for a in ip_pool:
        if a[0] == addr[0]:
            room_server.sendto("".encode('utf-8'), a)
            continue
        print(type(a[0]))
        msg1 = a[0] +':'+ msg.decode('utf-8')
        room_server.sendto(msg1.encode('utf-8'), a)
room_server.close()
