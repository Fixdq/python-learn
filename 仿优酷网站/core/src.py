#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : src.py
# @Software: PyCharm
from lib.mysocket import TCPServer
from lib import common
from conf import settings
from concurrent.futures import ThreadPoolExecutor
# 这个导包 一定不能删除  运行时调用
from core import admin, user

import os


server = TCPServer(settings.IP_PORT)
tp = ThreadPoolExecutor()

def router(conn):
    """
    路由分发
    :param conn: 连接对象
    :return: 
    """
    try:
        type, data = common.recv_obj_json(conn)
        print('dic')
        if type in menu:
            print('ok')
            eval(menu[type])
    except Exception as e:
        print('error')
        print(e.args)
        # conn.close()


def run():
    while True:
        print(os.getpid())
        print('run')

        # 建立连接
        conn, addr = server.get_request()
        print(addr[0])

        #开启线程池

        tp.submit(router, conn)


menu = {
    'admin_login': 'admin.admin(conn,data)',
    'admin_register': 'admin.register(conn,data)',
    'admin_upload_free_video': 'admin.upload_free_video(conn)',
    'admin_upload_fee_video': 'admin.upload_fee_video(conn)',
    'admin_delete_video': 'admin.delete_video(conn)',
    'admin_notify': 'admin.notify(conn,data)',

    'user_login': 'user.admin(conn,data)',
    'user_register': 'user.register(conn,data)',
    'user_vip': 'user.vip(conn,data)',
    'user_check_videos': 'user.check_videos(conn)',
    'user_down_videos': 'user.down_videos(conn,data)',
    'user_check_history': 'user.check_history(conn,data)',
    'user_check_notice': 'user.check_notice(conn)',
    'user_recharge': 'user.recharge(conn,data)',

}
