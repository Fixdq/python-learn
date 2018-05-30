#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-25 下午8:24
# @Author  : fixdq
# @File    : start.py
# @Software: PyCharm


from client import tcpclient
from lib import common


def login(conn):
    send_data = {'type': 'login',
                 'msg': 'hello'}
    res = common.send_back(conn, send_data)
    if res['flag']:
        print(res['msg'])
    else:
        print(res['msg'])


def register(conn):
    pass


menu = """
1.登录
2.注册
3.
4.
5.
"""
menu_dic = {
    '1': login,
    '2': register,
}


def view():
    conn = tcpclient.get_client()
    while True:
        print(menu)
        ch = input('>>>').strip()
        if ch == 'q ': break
        if ch not in menu_dic: continue
        menu_dic[ch](conn)
    conn.close()
