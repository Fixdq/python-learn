#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : server_.py
# @Software: PyCharm
from socket import *
import select

s = socket()
s.bind(('127.0.1.1', 8080))
s.setblocking(False)
s.listen()

r_list = [s, ]
w_list = []
w_data = {}
while True:
    print('r_list --->>%s' % len(r_list))
    print('w_list --->>%s' % len(w_list))
    rl, wl, xl = select.select(r_list, w_list, [],1)
    # 收消息
    for r in rl:
        if r == s:
            conn, addr = r.accept()
            # 将连接对象放到  r_list 进行监测
            r_list.append(conn)
        else:
            try:
                data = r.recv(1024)
                if not data:
                    r.close()
                    r_list.remove(r)
                    continue
                w_data[r] = data.upper()
                w_list.append(r)
            except ConnectionResetError:
                conn.close()
                r_list.remove(r)
                continue
    # 发消息
    for w in w_list:
        w.send(w_data[w])
        w_list.remove(w)
        w_data.pop(w)
