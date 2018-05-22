#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-22 上午11:51
# @Author  : fixdq
# @File    : common_interface.py
# @Software: PyCharm

from db.models import *
from lib import common


def login(conn, data):
    user = User.select_one(id=data['user_id'])
    if not user:
        back_dic = {'flag': False, 'msg': '用户不存在'}
        common.send(conn, back_dic)
        return

    if data['user_type'] == user.user_type:
        back_dic = {'flag': True, 'msg': '登录成功'}
        if data['user_type'] =='user':
            back_dic['is_vip']=user.is_vip
    else:
        back_dic = {'flag': True, 'msg': '类型错误'}

    session = common.get_uuid(data['name'])



    common.send(conn, back_dic)

def register(conn, data):
    user = User.select_one(name=data['name'])
    if user:
        back_dic = {'flag': False, 'msg': '用户已存在'}
        common.send(conn, back_dic)
        return
    user = User(name=data['name'],
                password=data['password'],
                user_type=data['user_type'])
    user.save()
    back_dic = {'flag': True, 'msg': '注册成功'}
    common.send(conn, back_dic)