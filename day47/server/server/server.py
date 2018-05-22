#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-22 上午11:52
# @Author  : fixdq
# @File    : server.py
# @Software: PyCharm
import json
import struct
from socket import *
from conf import setting
from server import user_data
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from lib import common

pool = ThreadPoolExecutor(10)
user_data.mutex = Lock()

menu_dic = {

}


def dispatch(conn, data):
    t = data['type']
    if t not in menu_dic:
        back_dic = {'flag': False, 'msg': '请求不存在'}
        common.send(conn, back_dic)
        return
    menu_dic[t](conn, data)


def work(conn, addr):
    while True:

        try:
            head_len = conn.recv(4)
            head_bytes = conn.recv(struct.unpack('i', head_len)[0])
            data_dic = json.loads(head_bytes)
            data_dic['addr'] = addr
            dispatch(conn, data_dic)
        except Exception as e:
            print(e)
            # 清除用户
            user_data.mutex.acquire()
            if user_data.users.get(addr):
                user_data.users.pop(addr)
            user_data.mutex.release()

            break


def run():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(setting.ip_port)
    server.listen(5)
    while True:
        conn, addr = server.accept()
        pool.submit(work, conn, addr)
