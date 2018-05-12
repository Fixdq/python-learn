#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : tcp_client.py
# @Software: PyCharm
"""


"""
from socket import *
from day29.homework import settings
from day29.homework import common

client = socket(AF_INET, SOCK_STREAM)
client.connect_ex(settings.ip_port)

flag = True



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
    common.recv_file(conn, '/home/fixd/project/python_learn/day29/homework.sql')
    print('down is ok')



while flag:
    res = common.recv(client)
    if res != 'ok':
        print('连接服务器失败!')
        break
    print('连接服务器成功!')

    while flag:
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
        while flag:
            menu = """
            1.上传
            2.下载
            3.退出
            """
            ch = input('>>>:').strip()

            if ch == '1':
                upload(client)
            if ch == '2':
                upload(client)
            if ch == '3':
                upload(client)


            print()
            path = input('上传>>:').strip()

            common.send_file(client, path)
            input('=========>').strip()

client.close()


def login(conn):
    print('开始登录!')
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
        return res

