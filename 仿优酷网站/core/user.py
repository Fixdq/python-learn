#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : user.py
# @Software: PyCharm
import os

from interface import user_interface
from lib import common
from conf import settings


def admin(conn, data_dic):
    print(data_dic)
    res, msg, notice = user_interface.login(data_dic['name'], data_dic['pwd'])
    res_dic = {
        'res': res,
        'msg': msg,
        'notice': notice
    }
    common.send_obj_json(conn, res_dic)
    conn.close()


def register(conn, data_dic):
    res, msg = user_interface.register(data_dic['name'], data_dic['pwd'])
    res_dic = {
        'res': res,
        'msg': msg
    }
    common.send_obj_json(conn, res_dic)
    conn.close()


def vip(conn, data_dic):
    user_name = data_dic['name']
    res, msg = user_interface.check_vip(user_name)
    res_dic = {
        'res': res,
        'msg': msg
    }
    common.send_obj_json(conn, res_dic)

    # 开通会员操作
    data = common.recv_obj_json(conn)
    res, msg = user_interface.vip(user_name)
    res_dic = {
        'res': res,
        'msg': msg
    }
    common.send_obj_json(conn, res_dic)
    conn.close()


def check_videos(conn):
    res, msg = user_interface.check_videos()
    res_dic = {
        'res': res,
        'msg': msg
    }
    common.send_obj_json(conn, res_dic)
    conn.close()


def down_videos(conn, data_dic):
    video_name = data_dic['video_name']
    type = user_interface.git_videos_type(video_name)
    res_dic = {
        'type': type
    }
    common.send_obj_json(conn, res_dic, '')
    # 根据用户类型下载
    #######################################################################
    res_dic = common.recv_obj_json(conn)

    user_name = res_dic['user_name']
    if type == '1':
        res = user_interface.down_free_videos(user_name, video_name)
    if type == '0':
        res = user_interface.down_fee_videos(user_name, video_name)
    result_dic = {
        'res': res
    }
    # 反馈下载结果
    common.send_obj_json(conn, result_dic, '')
    if res:
        # path = os.path.join(settings.BASE_DB, 'video', video_name)
        video = user_interface.get_video_by_name(video_name)

        common.send_file(conn, video.author, video.path)


def check_history(conn, data_dic):
    user_name = data_dic['name']
    res, msg = user_interface.check_history(user_name)
    res_dic = {
        'res': res,
        'msg': msg
    }
    common.send_obj_json(conn, res_dic)
    conn.close()


def check_notice(conn):
    res, msg = user_interface.get_all_notice()
    res_dic = {
        'res': res,
        'msg': msg
    }
    common.send_obj_json(conn, res_dic)
    conn.close()


def recharge(conn, data_dic):
    res, msg = user_interface.recharge(data_dic['user_name'], data_dic['recharge_money'])
    res_dic = {
        'res': res,
        'msg': msg
    }
    common.send_obj_json(conn, res_dic)
    conn.close()
