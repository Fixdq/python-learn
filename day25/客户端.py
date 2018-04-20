#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
import socket

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(('192.168.12.162', 8080))

while True:
    msg = input('>>>>>>>').strip()
    tcp_client.send(msg.encode('utf-8'))
    # res = tcp_client.recv(1024)
    # print(res.decode('utf-8'))

tcp_client.close()
