#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-20 下午3:09
# @Author  : fixdq
# @File    : src.py
# @Software: PyCharm
import os
import time

from lib import common
from tcpclient import client
from conf import setting

cookie = {
    'session': None,
    'is_vip': None
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
            'user_type': 'user'
        }
        res = common.send_back(conn, send_data)

        if res['flag']:
            print(res['msg'])
            break
        else:
            print(res['msg'])


def login(conn):
    print('登录')
    while True:
        name = input('input you name>>').strip()
        if name == 'q': break
        pwd = input('input you password>>').strip()
        send_data = {
            'type': 'login',
            'name': name,
            'pwd': pwd,
            'user_type': 'user'
        }
        res = common.send_back(conn, send_data)

        if res['flag']:
            cookie['session'] = res['session']
            cookie['is_vip'] = res['is_vip']
            print(res['msg'])
            # 查询公告
            send_data = {'type': 'get_notices',
                         'session': cookie['session'],
                         'notice_type': 1
                         }
            back_data = common.send_back(conn, send_data)
            print(back_data['msg'])
            break
        else:
            print(res['msg'])


@common.outter('user')
def get_vip(conn):
    while True:

        if cookie['is_vip'] == 1:
            print('您已经是会员了')
            break
        ch = input('是否充值会员（y/n）').strip()
        if ch == 'q': break
        if ch not in ['y', 'n']: continue
        if ch == 'n': break
        send_data = {'type': 'pay_vip',
                     'session': cookie['session']
                     }
        back_data = common.send_back(conn, send_data)
        if back_data['flag']:
            print(back_data['msg'])
            break
        else:
            print(back_data['msg'])


@common.outter('user')
def check_movie(conn):
    send_data = {'type': 'get_movie_all',
                 'session': cookie['session'],
                 }
    res = common.send_back(conn, send_data)
    if not res['flag']:
        print(res)
        return
    movies = res['msg']
    for i, movie in enumerate(movies):
        print(i, movie[1])


@common.outter('user')
def get_notice(conn):
    send_data = {'type': 'get_notices',
                 'session': cookie['session'],
                 'notice_type': 0
                 }
    back_data = common.send_back(conn, send_data)
    if back_data['flag']:
        for v in back_data['msg']:
            print(v[0], v[1])
    else:
        print(back_data['msg'])


@common.outter('user')
def get_movie_free(conn):
    while True:
        send_data = {'type': 'get_movies',
                     'session': cookie['session'],
                     'movie_type': 'free'
                     }
        back_data = common.send_back(conn, send_data)
        if not back_data['flag']:
            print(back_data['msg'])
            break

        for i, movie in enumerate(back_data['msg']):
            print(i, movie[1])

        ch = input('请选择下载电影的编号').strip()
        if ch == 'q': break
        if not ch.isdigit(): continue
        ch = int(ch)
        if ch < 0 or ch > len(back_data['msg']): continue

        # 发送下载请求
        send_data = {'type': 'download_movie',
                     'session': cookie['session'],
                     'movie_type': 'free',
                     'movie_id': back_data['msg'][ch][0]
                     }
        back_data = common.send_back(conn, send_data)
        if back_data['wait_time']:
            print('广告时间。。。')
            time.sleep(back_data['wait_time'])
        # 开始下载
        file_name = back_data['file_name']
        file_size = back_data['file_size']

        down_path = os.path.join(setting.BASE_DIR_MOVIE_DOWN, file_name)

        recv_size = 0
        with open(down_path, 'wb') as f:
            while recv_size < file_size:
                bytes = conn.recv(1024)
                f.write(bytes)
                recv_size += len(bytes)
                common.progress(recv_size / file_size)
        print()
        print('下载完成')
        break


@common.outter('user')
def get_movie_fee(conn):
    while True:
        send_data = {'type': 'get_movies',
                     'session': cookie['session'],
                     'movie_type': 'fee'
                     }
        back_data = common.send_back(conn, send_data)
        if not back_data['flag']:
            print(back_data['msg'])
            break

        for i, movie in enumerate(back_data['msg']):
            print(i, movie[1])

        ch = input('请选择下载电影的编号').strip()
        if ch == 'q': break
        if not ch.isdigit(): continue
        ch = int(ch)
        if ch < 0 or ch > len(back_data['msg']): continue

        # 发送下载请求
        send_data = {'type': 'download_movie',
                     'session': cookie['session'],
                     'movie_type': 'free',
                     'movie_id': back_data['msg'][ch][0]
                     }
        back_data = common.send_back(conn, send_data)

        # 开始下载
        file_name = back_data['file_name']
        file_size = back_data['file_size']

        down_path = os.path.join(setting.BASE_DIR_MOVIE_DOWN, file_name)

        recv_size = 0
        with open(down_path, 'wb') as f:
            while recv_size < file_size:
                bytes = conn.recv(1024)
                f.write(bytes)
                recv_size += len(bytes)
                common.progress(recv_size / file_size)
        print()
        print('下载完成')
        break


@common.outter('user')
def get_records(conn):
    send_data = {'type': 'get_records',
                 'session': cookie['session'],
                 'movie_type': 'fee'
                 }
    back_data = common.send_back(conn, send_data)
    if back_data['flag']:
        for re in back_data['msg']:
            print(re)

    else:
        print(back_data['msg'])


menu = """
1 注册
2 登录
3 冲会员
4 查看视频
5 下载免费视频
6 下载收费视频
7 查看观影记录
8 查看公告
"""

menu_dic = {
    '1': register,
    '2': login,
    '3': get_vip,
    '4': check_movie,
    '5': get_movie_free,
    '6': get_movie_fee,
    '7': get_records,
    '8': get_notice,
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
