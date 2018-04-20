#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp.bind(('192.168.12.35', 8888))
tcp.listen(5)
print('开始干活啦')
print('--------------------')
# 开始循环接受请求
while True:
    conn, address = tcp.accept()
    print('收到信息--------来自---%s---' % address)
    # 开始循环接收数据
    while True:
        try:
            msg = conn.recv(1024)
            print(msg.decode('utf-8'))
            re = print('>>>>>>>>:').strp()
            conn.send(re.encode('utf-8'))
        except Exception:
            break
    conn.close()
tcp.close()