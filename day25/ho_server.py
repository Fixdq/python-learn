#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

import socket
# ip,端口
ip_prot = ('127.0.0.1', 8884)
# 缓冲区大小
buffer = 1024
# 创建 socket对象
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定 ip 端口
socket_server.bind(ip_prot)
# 服务端开始监听
socket_server.listen(5)
while True:
    # 　连接对象,客户端地址（ip:port）
    conn, address = socket_server.accept()
    while True:
        try:
            # 接收信息
            msg = conn.recv(buffer)
            #
            # res = subprocess.Popen(cmd,
            #                        shell=True,
            #                        stdin=subprocess.PIPE,
            #                        stdout=subprocess.PIPE,
            #                        stderr=subprocess.PIPE)
            # msg_success = res.stdout.read()
            # msg_error = res.stdout.read()
            # print('发送-----')
            # conn.send(msg_success)
            # conn.send(msg_error)
            # msg 字母变大写  发送个客户端
            conn.send(msg.upper())
        except ConnectionError:
            break
    # 关闭连接
    conn.close()
# 关闭socket服务
socket_server.close()
