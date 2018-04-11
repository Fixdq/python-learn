#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from core import src


def login_auth(func):
    """
    验证用户登录装饰器
    :param func: 
    :return: 
    """
    def wrapper(*args, **kwargs):
        if not src.cur_user:
            src.login()
        else:
            return func(*args, **kwargs)
    return wrapper
