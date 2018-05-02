#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : server_.py
# @Software: PyCharm

from socket import *
import select
import os

s = socket()
s.bind(('127.0.0.1', 8878))
s.setblocking(False)
s.listen()

r_list = [s, ]
w_list = []
w_data = {}

while True:
    rl, wl, xl = select.select(r_list, w_list, [], 0.5)
    # 收消息
    for r in rl:
        if r == s:
            conn, addr = r.accept()
            r_list.append(conn)

        else:
            try:
                data = r.recv(1024)
                if not data:
                    r.close()
                    r_list.remove(r)

                w_list.append(r)
                w_data[r] = data.upper()
            except ConnectionResetError:
                r.close()
                r_list.remove(r)
                continue

    for w in w_list:
        w.send(w_data[w])
        w_list.remove(w)
        w_data.pop(w)
