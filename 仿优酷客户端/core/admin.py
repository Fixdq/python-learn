#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : admin.py
# @Software: PyCharm
import json
import os
import struct

from lib.client import *
from conf import settings
from lib import common
from lib.client import TCPClient

address_family = socket.AF_INET

socket_type = socket.SOCK_STREAM

request_queue_size = 5

user_data = {
    'name': None
}


def login():
    if user_data['name']:
        print('已登录')
        return
    flag = True
    while flag:
        conn = TCPClient(settings.IP_PORT).get_request()
        name = input('请输入用户名：').strip()
        pwd = input('请输入密码：').strip()
        if name == '' or pwd == '':
            continue
        data = {
            'name': name,
            'pwd': pwd
        }
        while flag:
            common.send_obj_json(conn, data, 'admin_login')
            res_dic = common.recv_obj_json(conn)
            if res_dic['res']:
                print(res_dic['msg'])
                user_data['name'] = name
                flag = False
                conn.close()
            else:
                print(res_dic['msg'])
                conn.close()
                break


def register():
    if user_data['name']:
        print('已登录')
        return
    flag = True
    while flag:
        conn = TCPClient(settings.IP_PORT).get_request()
        name = input('请输入用户名：').strip()
        pwd = input('请输入密码：').strip()
        pwd2 = input('请确认密码：').strip()
        if name == '' or pwd == '' or pwd2 == '':
            continue
        if not pwd == pwd2:
            print('两次密码输入不一致')
            continue

        data = {
            'name': name,
            'pwd': pwd
        }
        while flag:
            common.send_obj_json(conn, data, 'admin_register')
            res_dic = common.recv_obj_json(conn)
            if res_dic['res']:
                print(res_dic['msg'])
                flag = False
                conn.close()
            else:
                print(res_dic['msg'])
                conn.close()
                break


@common.is_login('admin')
def upload_free_video():
    upload_video('admin_upload_free_video')


@common.is_login('admin')
def upload_fee_video():
    upload_video('admin_upload_fee_video')


@common.is_login('admin')
def upload_video(type):
    flag = True
    while flag:
        conn = TCPClient(settings.IP_PORT).get_request()
        path = input('请输入上传文件的绝对路径:').strip()
        if not os.path.isfile(path):
            conn.close()
            return False, '文件不存在'
        data = {
            'type': 'get'
        }
        # 发送路由信息
        common.send_obj_json(conn, data, type)
        # 发送文件
        common.send_file(conn, user_data['name'], path)
        # 接收反馈信息
        res_dic = common.recv_obj_json(conn)
        if res_dic['res']:
            print(res_dic['msg'])
            flag = False
            conn.close()
        else:
            print(res_dic['msg'])
            conn.close()


@common.is_login('admin')
def delete_video():
    conn = TCPClient(settings.IP_PORT).get_request()
    data = {
        'type': 'get'
    }
    # 发送路由信息
    common.send_obj_json(conn, data, 'admin_delete_video')
    # 接收反馈信息
    res_dic = common.recv_obj_json(conn)
    videos = res_dic['msg']
    if not res_dic['res']:
        print(videos)
        conn.close()

    flag = True
    while flag:

        # 显示存在的视频
        for i, v in enumerate(videos):
            print(i, v)
        ch = input('选择你要删除的视频：').strip()
        if ch == 'q':
            conn.close()
            break
        if not ch.isdigit():
            print('输入不正确')
            continue
        ch = int(ch)
        if ch < 0 or ch > len(videos):
            print('输入不正确')
            continue
        delete_name = videos[ch]

        data = {
            'admin': user_data['name'],
            'delete_name': delete_name
        }
        # 发送删除请求
        common.send_obj_json(conn, data, '')

        # 接收反馈信息
        res_dic = common.recv_obj_json(conn)
        if res_dic['res']:
            print(res_dic['msg'])
            flag = False
            conn.close()
        else:
            print(res_dic['msg'])
            conn.close()


@common.is_login('admin')
def notify():
    print('发布公告')
    flag = True
    while flag:
        conn = TCPClient(settings.IP_PORT).get_request()
        content = input('请输入公告内容：').strip()
        if content == '':
            print('内容不能为空！')
            continue

        data = {
            'admin': user_data['name'],
            'content': content,
        }
        while flag:
            common.send_obj_json(conn, data, 'admin_notify')
            res_dic = common.recv_obj_json(conn)
            if res_dic['res']:
                print(res_dic['msg'])
                flag = False
                conn.close()
            else:
                print(res_dic['msg'])
                conn.close()
                break


menu = """
1.注册
2.登录
3.上传普通视频
4.上传收费视频
5.删除视频
6.发布公告
"""
menu_dic = {
    '1': register,
    '2': login,
    '3': upload_free_video,
    '4': upload_fee_video,
    '5': delete_video,
    '6': notify,
}


def show():
    while True:
        print(menu)
        ch = input('>>>:').strip()
        if ch == 'q': break
        if ch not in menu_dic: continue
        menu_dic[ch]()
