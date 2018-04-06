#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
"""
装饰器
用户认证装饰器
记录用户流水日志
"""
from core import db_handler
from conf import settings


# 用户认证装饰器
def auth(func):
    def wrapper(*args, **kwargs):
        if db_handler.get_is_auth():
            return func(*args, **kwargs)
        else:
            print("您还没登录！")

    return wrapper


# 记录用户流水日志
def user_access(logger):
    def out(func):
        def wrapper(*args, **kwargs):
            # 默认操作
            account = 'balance'
            mode = '-'
            if args:
                uname = args[0]
                money = args[1]
            if kwargs:
                for key in kwargs:
                    if key == 'account':
                        account = kwargs['account']
                    if key == 'mode':
                        mode = kwargs['mode']
            logger.info(settings.MSG_FMT.format(
                uname=uname,
                money=money,
                account=account,
                mode=mode,
            ))
            res = func(*args, **kwargs)
            return res

        return wrapper

    return out
