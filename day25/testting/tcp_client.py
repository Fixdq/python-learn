#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : tcp_client.py
# @Software: PyCharm
import json
from socket import *
import struct

ip_port = ('127.155.101.25', 8090)
client = socket(AF_INET, SOCK_STREAM)

client.connect_ex(ip_port)

while True:
    cmd = input('>>>>>:').strip()
    client.send(cmd.encode('utf-8'))

    # 接收  报头的报头  (固定长度 4 字节)
    head_head = client.recv(4)
    # 反解出 报头的长度
    head_len = int(struct.unpack('i',head_head)[0])
    # 接收  自定义报头
    head = client.recv(head_len)
    # 拿到  自定义报头的长度
    body_len = json.loads(head.decode('utf-8'))['len']
    # 接收  真实的数据
    data = client.recv(body_len)
    print(data.decode('utf-8'))

client.close()
