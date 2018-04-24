#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : server_mult.py
# @Software: PyCharm

from socket import *
from multiprocessing import Process

ip_port = ('127.8.2.1', 15555)
server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(ip_port)
server.listen(5)


def back(conn, addr):
    while True:
        try:
            msg = conn.recv(1024)
            if not msg: break
            conn.send(msg.upper())
        except ConnectionError:
            print('error')
    conn.close()

if __name__ == '__main__':
    while True:
        conn, addr = server.accept()
        p = Process(target=back, args=(conn, addr))
        p.start()
