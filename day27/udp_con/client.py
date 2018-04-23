#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : client.py
# @Software: PyCharm

import socket
# IP  port
ip_port = ('127.122.114.15', 8080)
# 创建客户端
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 循环
while True:
    # 接收用户输入
    msg = input('>>>>>>>:').strip()
    if not msg: continue
    # 发送信息
    client.sendto(msg.encode('utf-8'), ip_port)
    # 接收信息
    res,addr = client.recvfrom(1024)
    # 打印信息
    print(res.decode('utf-8'),addr)
# 回收资源
client.close()