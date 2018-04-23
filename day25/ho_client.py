#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
import socket

# ip,端口
ip_prot = ('127.0.0.1', 8884)
# 缓冲区大小
buffer = 1024
# 获取socket
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 根据 ip_port 连接服务器
socket_client.connect(ip_prot)

while True:
    # 接受输入
    cmd = input("cmd>>:").strip()
    # 发送信息
    socket_client.send(cmd.encode('utf-8'))
    # 接受信息
    res = socket_client.recv(buffer)
    # 打印信息
    print(res.decode('utf-8'))
# 关闭socket
socket_client.close()
