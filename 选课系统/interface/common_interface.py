#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from db import models


def login_interface(name, pwd, type):
    if type == 'admin':
        obj = models.Admin.get_obj_by_name(name)
    elif type == 'student':
        obj = models.Admin.get_obj_by_name(name)
    elif type == 'teacher':
        obj = models.Admin.get_obj_by_name(name)
    else:
        return False, 'error'
    # 判断用户是否存在
    if obj:
        if pwd == obj.password:
            return True, '登录成功'
        else:
            return False, '密码不正确'
    else:
        return False, '用户名不存在'
