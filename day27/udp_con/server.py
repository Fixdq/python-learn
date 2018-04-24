#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : server_mult.py
# @Software: PyCharm
import socket
# ip,端口
ip_port = ('127.122.114.15', 8080)
# 获取socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定IP ,端口
server.bind(ip_port)
# 循环执行
while True:
    # 接收信息
    res, addr = server.recvfrom(1024)
    # 打印信息
    print(res.decode('utf-8'))
    server.sendto('收到了'.encode('utf-8'), addr)
# 回收资源
server.close()
