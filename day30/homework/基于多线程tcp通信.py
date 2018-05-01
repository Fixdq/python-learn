#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : 基于多线程tcp通信.py
# @Software: PyCharm
from socket import *
from threading import Thread

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8080,))
server.listen(5)


def task(conn, addr):
    while True:
        try:
            res = conn.recv(1204)
            print(res.decode('utf-8'))
            conn.send(res.upper())
        except ConnectionError:
            break

    conn.close()


while True:
    conn, addr = server.accept()
    print(addr)
    conn.send('ok'.encode('utf-8'))
    t = Thread(target=task, args=(conn, addr,))
    t.start()

server.close()
