#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-20 下午3:47
# @Author  : fixdq
# @File    : server.py
# @Software: PyCharm
import json
import socket
import struct

from conf import setting
from tcpserver import userdata
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from lib import common
from interface import admin_interface, common_interface, user_interface

pool = ThreadPoolExecutor(10)
mutex = Lock()
userdata.mutex = mutex
menu_dic = {
    'register': common_interface.register,
    'login': common_interface.login,
    'check_movie': admin_interface.check_movie,
    'upload': admin_interface.upload,
    'notice': admin_interface.notice,

    'get_movie_all': admin_interface.get_movie_all,
    'delete_movie': admin_interface.delete_movie_by_id,
    'pay_vip': user_interface.pay_vip,
    'download_movie': user_interface.download_movie,
    'get_movies': user_interface.get_movies,
    'get_notices': user_interface.get_notices,
    'get_records': user_interface.get_records,

}


def dispatch(conn, data):
    type = data['type']
    if type not in menu_dic:
        back_data = {
            'flag': False,
            'msg': '请求不存在'
        }
        common.send(conn, back_data)
    else:
        menu_dic[type](conn, data)


def work(conn, addr):
    while True:
        try:
            head_len_bytes = conn.recv(4)
            if not head_len_bytes: break
            head_bytes = conn.recv(struct.unpack('i', head_len_bytes)[0])
            data = json.loads(head_bytes.decode(setting.charset))
            data['addr'] = addr
            dispatch(conn, data)
        except Exception as e:
            print(e)
            conn.close()
            userdata.mutex.acquire()
            if userdata.userdata.get(addr):
                userdata.userdata.pop(addr)
            userdata.mutex.release()
            break

def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(setting.ip_port)
    server.listen(5)
    while True:
        conn, addr = server.accept()
        pool.submit(work, conn, addr)
