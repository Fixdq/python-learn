#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


import logging.config
from conf import setting
from core import src


def get_logger(name):
    logging.config.dictConfig(setting.LOGGING_DIC)
    return logging.getLogger(name)


def is_auth(func):
    def wrapper(*args, **kwargs):
        if src.c_user['is_auth']:
            return func(*args, **kwargs)
        else:
            print('你还没登录，请登录！')
            src.login()

    return wrapper
