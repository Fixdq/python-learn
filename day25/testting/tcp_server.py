#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : tcp_server.py
# @Software: PyCharm
import json
from socket import *

import subprocess

import struct

ip_port = ('127.155.101.25', 8090)

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(ip_port)

server.listen(5)

while True:
    conn, addr = server.accept()
    while True:
        cmd = conn.recv(1024)
        if not cmd: break
        print('--------->cmd----', cmd.decode('utf-8'))
        res = subprocess.Popen(cmd.decode('utf-8'),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        ret = res.stdout.read()
        if ret:
            back = ret
        else:
            back = res.stderr.read()

        # 把真实数据的相关信息,包装成字典
        head = {
            'len': len(back)
        }
        # json 序列化 字典信息
        head_str = json.dumps(head)
        # 只包含报头长度 (报头的报头)
        # i 模式,产生一个固定4字节长度bytes
        head_head = struct.pack('i', len(head_str))
        # 发送   (报头的报头)
        conn.send(head_head)
        # 报头数据
        conn.send(head_str.encode('utf-8'))
        # 真实数据
        conn.send(back)

    conn.close()
server.close()
