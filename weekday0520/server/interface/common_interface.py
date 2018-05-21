#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-20 下午3:43
# @Author  : fixdq
# @File    : setting.py
# @Software: PyCharm

from db.Models import User
from lib import common
from tcpserver import userdata


def register(conn, data):
    user = User.select_one(name=data['name'])
    if user:
        back_data = {'flag': False, 'msg': '用户已存在'}
        common.send(conn, back_data)
    else:

        user = User(name=data['name'],
                    password=common.get_md5(data['pwd']),
                    user_type=data['user_type'])
        user.save()
        back_data = {'flag': True, 'msg': '注册成功'}
        common.send(conn, back_data)


def login(conn, data):
    user = User.select_one(name=data['name'])
    if not user:
        back_data = {'flag': False, 'msg': '用户不存在'}
        common.send(conn, back_data)
        return
    if user.user_type != data['user_type']:
        back_data = {'flag': False, 'msg': '用户类型错误'}
        common.send(conn, back_data)
        return

    if common.get_md5(data['pwd']) != user.password:
        back_data = {'flag': False, 'msg': '密码不正确'}
        common.send(conn, back_data)
        return
    # 生成session
    session = common.get_uuid(data['name'])
    # 保存session 在服务端
    # 加锁
    userdata.mutex.acquire()
    userdata.userdata[data['addr']] = [session, user.id]
    userdata.mutex.release()
    back_data = {'flag': True, 'msg': '登录成功', 'session': session}
    if data['user_type'] == 'user':
        back_data['is_vip'] = user.is_vip
    common.send(conn, back_data)
