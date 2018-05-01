#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : tcp_pool.py
# @Software: PyCharm

from socket import *
# 　导入进程池，线程池
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def task(conn, addr):
    # ok = '% link is ok ' % addr[0]
    # conn.send(ok.encode('utf-8'))
    while True:
        try:
            msg = conn.recv(1024)
            conn.send(msg.upper())
        except ConnectionError:
            break
    conn.close()


def run():
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    print('start')
    while True:
        conn, client_addr = server.accept()
        # 进程池
        # p = ProcessPoolExecutor(3)
        # p.submit(task, conn, client_addr)


        #　线程池
        t = ThreadPoolExecutor(3)
        t.submit(task, conn, client_addr)


    server.close()


if __name__ == '__main__':
    run()
