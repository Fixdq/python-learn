#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-25 下午8:23
# @Author  : fixdq
# @File    : tcpserver.py
# @Software: PyCharm
import json
import struct
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from socket import *
from conf import setting
from server import user_datas
from lib import common
from interface import common_interface

pool = ThreadPoolExecutor()
user_datas.mutex = Lock()

menu_dic = {
    'login': common_interface.login,
}


def dispatch(conn, data):
    type = data.get('type')
    if type not in menu_dic:
        back_data = {'flag': False, 'msg': '请求不存在'}
        common.send(conn, back_data)
        return

    menu_dic[type](conn, data)


def work(conn, addr):
    while True:

        # 分发
        try:
            head_len = conn.recv(4)
            if not head_len: break
            data = conn.recv(struct.unpack('i', head_len)[0]).decode('utf-8')
            head_dic = json.loads(data)
            head_dic['addr'] = addr
            dispatch(conn, head_dic)
        except Exception as e:
            print(e)
            # 关闭链接
            conn.close()
            # 回收资源
            user_datas.mutex.acquire()
            if user_datas.user_datas.get(addr):
                user_datas.user_datas.pop(addr)
            user_datas.mutex.release()

            break


def run():
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind(setting.ip_port)
    server.listen()

    while True:
        conn, addr = server.accept()
        pool.submit(work, conn, addr)
