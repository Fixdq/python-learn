#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : admin.py
# @Software: PyCharm
import json
import os
import struct

from interface import admin_interface
from lib import common
from conf import settings


def admin(conn, data_dic):
    print(data_dic)
    res, msg = admin_interface.login(data_dic['name'], data_dic['pwd'])
    res_dic = {
        'res': res,
        'msg': msg
    }
    common.send_obj_json(conn, res_dic)
    conn.close()


def register(conn, data_dic):
    res, msg = admin_interface.register(data_dic['name'], data_dic['pwd'])
    res_dic = {
        'res': res,
        'msg': msg
    }
    common.send_obj_json(conn, res_dic)
    conn.close()


def upload_video(conn, type):
    author, file_name, file_size, file_path = common.recv_file(conn)
    res, msg = admin_interface.upload_video(author, file_name, file_size, file_path, type)
    res_dic = {
        'res': res,
        'msg': msg
    }
    common.send_obj_json(conn, res_dic)
    conn.close()


def upload_free_video(conn):
    upload_video(conn, type='1')


def upload_fee_video(conn):
    upload_video(conn, type='0')
    # # 接收  报头的报头  (固定长度 4 字节)
    # head_head = conn.recv(4)
    # # 反解出 报头的长度
    # head_len = int(struct.unpack('i', head_head)[0])
    # # 接收  自定义报头
    # head = conn.recv(head_len)
    # # 拿到  自定义报头
    # data_dic = json.loads(head.decode('utf-8'))
    #
    # author = data_dic['author']
    # file_name = data_dic['file_name']
    # file_size = data_dic['file_size']
    #
    # file_path = os.path.normpath(os.path.join(
    #     settings.BASE_VIDEOS,
    #     file_name
    # ))
    # recv_size = 0
    # print('----->', file_path)
    # with open(file_path, 'wb') as f:
    #     while recv_size < file_size:
    #         recv_data = conn.recv(settings.max_buffer_size)
    #         f.write(recv_data)
    #         recv_size += len(recv_data)
    #         print(recv_size)


def delete_video(conn):
    #查询
    res, msg = admin_interface.get_all_real_video()
    res_dic = {
        'res': res,
        'msg': msg
    }
    common.send_obj_json(conn, res_dic)

    # 接收用户需要删除的视屏名字

    res_dic = common.recv_obj_json(conn)
    admin = res_dic['admin']
    delete_name = res_dic['delete_name']

    # 调用删除接口
    res,msg = admin_interface.delete_video(admin,delete_name)
    res_dic = {
        'res': res,
        'msg': msg
    }
    common.send_obj_json(conn, res_dic)

    conn.close()


def notify(conn, data_dic):
    res, msg = admin_interface.notify(data_dic['admin'], data_dic['content'])
    res_dic = {
        'res': res,
        'msg': msg
    }
    common.send_obj_json(conn, res_dic)
    conn.close()
