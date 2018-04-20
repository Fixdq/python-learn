#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
import socket

ip_prot = ('127.0.0.1', 8884)
buffer = 1024
socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_client.connect(ip_prot)

while True:
    cmd = input("cmd>>:").strip()
    socket_client.send(cmd.encode('utf-8'))
    res = socket_client.recv(buffer)
    print(res.decode('utf-8'))
