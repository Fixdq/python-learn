#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : file_tcp_server.py
# @Software: PyCharm

from socket import *
from threading import Thread

from 仿优酷网站 import common

# 被下载的文件
down_load_path = '/home/fixd/project/python_learn/day30/test.txt'
# 上传文件保存目录
path = '/home/fixd/project/python_learn/day30'

# 默认登录账户
user_info = {
    'name': 'fixd',
    'pwd': '123',
}

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8080,))
server.listen(5)


def login(conn):
    """
    用户登录
    :param conn: 
    :return: 
    """

    while True:
        # 接收用户信息
        login_info = common.recv_obj_json(conn)
        # 验证 用户名  和  密码
        if user_info['name'] == login_info['name'] and \
                        user_info['pwd'] == login_info['pwd']:
            # 登录成功  状态返回值  1
            msg = '1'
            common.send(conn, msg)
            break
        else:
            # 登录失败  状态返回值  0
            msg = '0'
            common.send(conn, msg)
            continue


def link(conn, addr):
    """
    线程的任务   每一个连接创建一次
    :param conn: 
    :param addr: 
    :return: 
    """
    conn_ok = 'ok'
    # conn.send(conn_ok.encode('utf-8'))
    common.send(conn, conn_ok)
    flag = True
    while flag:
        try:
            # 登录
            login(conn)
            while flag:
                flag = common.recv(conn)
                if flag == 'up':
                    # 接收上传文件
                    common.recv_file(conn, path)
                    print('up is ok')
                if flag == 'down':
                    # 发送下载文件
                    common.send_file(conn, down_load_path)
                    print('download is ok ')
                if flag == 'exit':
                    # 退出  断开连接
                    flag = False
                    break
        except ConnectionError:
            break

    conn.close()


while True:
    conn, addr = server.accept()
    print(addr)
    t = Thread(target=link, args=(conn, addr,))
    t.start()

server.close()
