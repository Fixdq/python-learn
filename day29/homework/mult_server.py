#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : mult_server.py
# @Software: PyCharm
"""

"""

# 被下载的文件
down_load_path = '/home/fixd/project/python_learn/day29/test.py'
# 上传文件保存目录
path = '/home/fixd/project/python_learn/day29'

user_info = {
    'name': 'fixd',
    'pwd': '123',
}

from socket import *
from multiprocessing import Process
from day29.homework import settings
from day29.homework import common

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(settings.ip_port)
server.listen(5)


def download(conn, addr):
    conn_ok = 'ok'
    # conn.send(conn_ok.encode('utf-8'))
    common.send(conn, conn_ok)
    flag = True
    while flag:
        try:
            # 确认连接成功
            # 验证登录
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
            while True:
                flag = common.recv(conn)
                if flag == 'up':
                    common.recv_file(conn, path)
                    print('up is ok')
                if flag == 'down':
                    common.send_file(conn,down_load_path)
                    print('download is ok ')
                if flag == 'exit':
                    flag = False
                    break
        except ConnectionError:
            continue
    conn.close()


if __name__ == '__main__':
    while True:
        # 建立连接
        conn, addr = server.accept()
        # conn.send()
        # conn.recv()
        p = Process(target=download, args=(conn, addr))
        p.start()
server.close()
