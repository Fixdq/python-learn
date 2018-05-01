#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : user.py
# @Software: PyCharm
from lib.client import *
from conf import settings
from lib import common

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
        conn = socket.socket(address_family, socket_type)
        conn.connect(settings.IP_PORT)
        name = input('请输入用户名：').strip()
        pwd = input('请输入密码：').strip()
        if name == '' or pwd == '':
            continue
        data = {
            'name': name,
            'pwd': pwd
        }
        while flag:
            common.send_obj_json(conn, data, 'user_login')
            res_dic = common.recv_obj_json(conn)
            if res_dic['res']:
                print(res_dic['msg'])
                if res_dic['notice']:
                    print(res_dic['notice'])
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
        conn = socket.socket(address_family, socket_type)
        conn.connect(settings.IP_PORT)
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
            common.send_obj_json(conn, data, 'user_register')
            res_dic = common.recv_obj_json(conn)
            if res_dic['res']:
                print(res_dic['msg'])
                flag = False
                conn.close()
            else:
                print(res_dic['msg'])
                conn.close()
                break


@common.is_login('user')
def vip():
    print('冲会员')
    conn = TCPClient(settings.IP_PORT).get_request()
    data = {
        'name': user_data['name']
    }
    common.send_obj_json(conn, data, 'user_vip')
    res_dic = common.recv_obj_json(conn)
    if res_dic['res']:
        print(res_dic['msg'])
        conn.close()
        return
    while True:
        ch = input('是否充值会员（50）y/n：').strip()
        if ch == 'q':
            conn.close()
            break
        if ch not in ['y', 'Y', 'n', 'N']:
            print('输入不正确！')
            continue
        if ch in ['y', 'Y', ]:
            data = {
                'name': 'get'
            }
            # 发送充值信息
            common.send_obj_json(conn, data, '')
            res_dic = common.recv_obj_json(conn)
            if res_dic['res']:
                print(res_dic['msg'])
                conn.close()
                return


@common.is_login('user')
def check_videos():
    print('查看视频列表')
    conn = TCPClient(settings.IP_PORT).get_request()
    data = {
        'name': 'get'
    }
    common.send_obj_json(conn, data, 'user_check_videos')
    res_dic = common.recv_obj_json(conn)

    if res_dic['res']:
        videos = res_dic['msg']

        for i, v in enumerate(videos):
            print(i, v)

        conn.close()
    else:
        print(res_dic['msg'])
        conn.close()


@common.is_login('user')
def down_videos():

    print('下载视频')
    flag = True
    while flag:

        conn = TCPClient(settings.IP_PORT).get_request()
        data = {
            'name': 'get'
        }
        common.send_obj_json(conn, data, 'user_check_videos')
        res_dic = common.recv_obj_json(conn)

        if not res_dic['res']:
            print(res_dic['msg'])
            conn.close()
            break
        conn.close()

        while flag:
            conn = TCPClient(settings.IP_PORT).get_request()
            videos = res_dic['msg']
            for i, v in enumerate(videos):
                print(i, v)
            ch = input('选择你要下载的视频：').strip()
            if ch == 'q':
                conn.close()
                flag = False
                break
            if not ch.isdigit():
                print('输入不正确')
                continue
            ch = int(ch)
            if ch < 0 or ch > len(videos):
                print('输入不正确')
                continue
            video_name = videos[ch]
            # 判断视屏是否收费
            data = {
                'video_name': video_name
            }
            common.send_obj_json(conn, data, 'user_down_videos')
            # 接收视频类型信息
            res_dic = common.recv_obj_json(conn)

            if res_dic['type'] == '1':
                # 免费的
                print('此视频免费，尽情下载吧')
                data = {
                    'user_name': user_data['name'],
                }
                #######################################################################
                common.send_obj_json(conn, data, '')

                # # 接收文件
                # es = common.recv_obj_json(conn)
                # if res['res']:
                #     # 接收文件
                #     common.recv_file(conn)
                #     break

            elif res_dic['type'] == '0':
                # 收费的
                data = {
                    'user_name': user_data['name'],
                }
                ch = input('收费视频(非会员：10 会员：5)，确认下载（y）：').strip()
                if ch != 'y':
                    conn.close()
                    flag = False
                    break
                # 发送下载请求
                common.send_obj_json(conn, data, '')

            res = common.recv_obj_json(conn)
            if res['res']:
                # 接收文件
                common.recv_file(conn)
                flag = False
                break
            else:
                print('余额不足')
                conn.close()
                flag = False
                break



@common.is_login('user')
def check_history():
    print('查看观影历史')
    conn = TCPClient(settings.IP_PORT).get_request()
    data = {
        'name': user_data['name']
    }
    common.send_obj_json(conn, data, 'user_check_history')
    res_dic = common.recv_obj_json(conn)
    if res_dic['res']:
        for k, v in res_dic['msg'].items():
            print(k, v)
        conn.close()
    else:
        print(res_dic['msg'])
        conn.close()


@common.is_login('user')
def check_notice():
    print('查看公告')
    while True:
        conn = TCPClient(settings.IP_PORT).get_request()
        data = {
            'name': user_data['name']
        }
        common.send_obj_json(conn, data, 'user_check_notice')
        res_dic = common.recv_obj_json(conn)
        if res_dic['res']:
            for notice in res_dic['msg']:
                print(notice)
            conn.close()
            break
        else:
            print(res_dic['msg'])
            conn.close()


@common.is_login('user')
def recharge():
    print('充值：')

    flag = True
    while flag:
        conn = TCPClient(settings.IP_PORT).get_request()
        account = input('请输入充值金额：').strip()
        if 'q' == account:
            conn.close()
            break
        if not account.isdigit():
            print('金额输入错误')
            continue
        account = int(account)
        if account <= 0:
            print('金额输入错误')
            continue

        data = {
            'user_name': user_data['name'],
            'recharge_money': account,
        }

        while flag:
            common.send_obj_json(conn, data, 'user_recharge')
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
1. 注册
2. 登录
3. 冲会员
4. 查看视频
5. 下载视频
6. 查看观影记录
7. 查看公告
8. 充值
"""
menu_dic = {
    '1': register,
    '2': login,
    '3': vip,
    '4': check_videos,
    '5': down_videos,
    '6': check_history,
    '7': check_notice,
    '8': recharge,
}


def show():
    while True:
        print(menu)
        ch = input('>>>:').strip()
        if ch == 'q': break
        if ch not in menu_dic: continue
        menu_dic[ch]()
