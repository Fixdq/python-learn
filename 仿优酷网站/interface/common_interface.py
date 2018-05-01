#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : common_interface.py
# @Software: PyCharm
import os
from conf import settings

from db.models import *


def login(name, pwd, type):
    """
    0.登录成功
    1.密码错误
    2.用户不存在
    3.登录错误
    4
    :param name: 
    :param pwd: 
    :param type: 
    :return: 
    """
    if type == 'admin':
        obj = Admin.get_obj_by_name(name)
    elif type == 'user':
        obj = User.get_obj_by_name(name)
    else:
        return False, '登录错误'
    if not obj:
        return False, '用户不存在'
    if not obj.pwd == pwd:
        False, '密码错误'
    return True, '登录成功'



