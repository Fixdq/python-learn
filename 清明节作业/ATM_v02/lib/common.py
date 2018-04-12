#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
import logging.config

from core import src
from conf import setting


def login_auth(func):
    """
    验证用户登录装饰器
    :param func: 
    :return: 
    """

    def wrapper(*args, **kwargs):
        if src.cur_user is None:
            print('对不起，您还没有登录!')
            src.login()
        else:
            return func(*args, **kwargs)

    return wrapper


def get_logger(log_name):
    """
    log 日志
    :param log_name: 
    :return: 
    """
    # 导入logging 字典配置
    logging.config.dictConfig(setting.LOGGING_DIC)
    logger = logging.getLogger(log_name)
    return logger
