#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-20 下午3:09
# @Author  : fixdq
# @File    : src.py
# @Software: PyCharm
import os

from client.tcpclient import client
from client.lib import common
from client.conf import setting

cookie = {
    'session': None
}


def register(conn):
    while True:
        name = input('input you name>>').strip()
        pwd = input('input you password>>').strip()
        pwd1 = input('confirm you password>>').strip()
        if pwd != pwd1:
            print('密码不一致')
            continue
        send_data = {
            'type': 'register',
            'name': name,
            'pwd': pwd,
            'user_type': 'admin'
        }
        res = common.send_back(conn, send_data)

        if res['flag']:
            print(res['msg'])
            break
        else:
            print(res['msg'])


def login(conn):
    while True:
        name = input('input you name>>').strip()
        pwd = input('input you password>>').strip()
        send_data = {
            'type': 'login',
            'name': name,
            'pwd': pwd,
        }
        res = common.send_back(conn, send_data)

        if res['flag']:
            cookie['session'] = res['session']
            print(res['msg'])
            break
        else:
            print(res['msg'])


@common.outter('admin')
def upload(conn):
    while True:
        movies = common.get_movie_all()
        if not movies:
            print('没有可上传的视频')
            break

        for i, movie in enumerate(movies):
            print(i, movies)

        ch = input('请选择要上传的视频').strip()
        if ch == 'q': break
        if not ch.isdigit(): continue
        ch = int(ch)
        if ch < 0 or ch >= len(movies): continue

        # 获取文件信息
        file_path = os.path.join(setting.BASE_DIR_MOVIE, file_name)
        file_name = movies(ch)
        file_size = common.get_filesize(file_path)
        file_md5 = common.get_file_md5(file_path)

        send_data = {'type': 'check_movie',
                     'session': cookie['session'],
                     'file_md5': file_md5}
        res = common.send_back(conn, send_data)
        # 文件已存在
        if not res['flag']:
            print(res['msg'])
            break
        # 文件不存在

        is_free = input('是否是收费（y/n）').strip()
        if is_free not in ['y', 'n']: continue
        if is_free == 'y':
            is_free_tag = 0
        else:
            is_free_tag = 1

        send_data = {'type': 'upload',
                     'session': cookie['session'],
                     'file_name': file_name,
                     'is_free': is_free_tag,
                     'file_md5': file_md5,
                     'file_size': file_size}
        res = common.send_back(conn, send_data, file_path)

        if res['flag']:
            print(res['msg'])
            break
        else:
            print(res['msg'])
            break


@common.outter('admin')
def remove(conn):
    while True:
        send_data = {'type': 'get_movie_all',
                     'session': cookie,
                     }
        res = common.send_back(conn, send_data)
        if not res['flag']:
            print(res)
            return
        movies = res['msg']
        for i, movie in enumerate(movies):
            print(i, movie[1])

        ch = input('请选择要删除的视频').strip()
        if ch == 'q': break
        if not ch.isdigit(): continue
        ch = int(ch)
        if ch < 0 or ch >= len(movies): continue

        send_data = {'type': 'delete_movie',
                     'session': cookie,
                     'id': movies[ch][0]
                     }
        res = common.send_back(conn, send_data)
        if res['flag']:
            print(res['msg'])
            break
        else:
            print(res['msg'])


@common.outter('admin')
def notice(conn):
    while True:
        title = input('请输入标题：').strip()
        content = input('请输入内容：').strip()
        send_data = {'session': cookie['session'],
                     'title': title,
                     'content': content}
        res = common.send_back(conn, send_data)
        if res['flag']:
            print(res['msg'])
            break
        else:
            print(res['msg'])


menu = """
1.注册
2.登录
2.上传视频
2.删除视频
2.发布公告
"""

menu_dic = {
    '1': register,
    '2': login,
    '3': upload,
    '4': remove,
    '5': notice,
}


def view():
    conn = client.get_conn()
    while True:
        print(menu)
        ch = input('>>>:').strip()
        if ch == 'q': break
        if ch not in menu_dic: continue
        menu_dic[ch](conn)
    conn.close()
