#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : tcp_client.py
# @Software: PyCharm
"""


"""
from socket import *

from 仿优酷网站 import common

client = socket(AF_INET, SOCK_STREAM)
client.connect_ex(('127.0.0.1', 8080,))


def upload(conn):
    while True:
        common.send(conn, 'up')
        path = input('请输入上传文件的绝对路径:').strip()
        if not os.path.isfile(path):
            return False, '文件不存在'
        common.send_file(conn, path)
        print('上传成功')
        break


def download(conn):
    common.send(conn, 'down')
    # 下载保存的路径
    common.recv_file(conn, '/home/fixd/project/python_learn/day30/homework')
    print('down is ok')


def login(conn):
    while True:
        name = input('用户名:').strip()
        pwd = input('密码:').strip()
        if not name or not pwd: continue
        user_dic = {
            'name': name,
            'pwd': pwd
        }
        common.send_obj_json(client, user_dic)
        print('登录中.....')
        res = common.recv(client)
        if res == '0':
            print('登录失败,用户名密码不正确')
            continue
        if res == '1':
            print('登录成功')
            break


flag = True
while flag:
    res = common.recv(client)
    if res != 'ok':
        print('连接服务器失败!')
        break
    print('连接服务器成功!')
    login(client)
    while flag:

        menu = """
1.上传
2.下载
3.退出
                    """
        print(menu)
        ch = input('>>>:').strip()

        if ch == '1':
            upload(client)
        elif ch == '2':
            download(client)
        elif ch == '3':
            common.send(client, 'exit')
            flag = False
        else:
            continue

client.close()
