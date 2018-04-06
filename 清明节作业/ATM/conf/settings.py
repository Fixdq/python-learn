#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
"""
程序的配置

"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 当前登录的用户
DB_ATUH = os.path.join(BASE_DIR, 'db', 'current_user.json', )
# 商品信息路径
DB_PRODUCTS = os.path.join(BASE_DIR, 'db', 'product_list.json', )
# 用户信息路径
DB_PATH_USERS = os.path.join(BASE_DIR, 'db', 'accounts', )

# 日志路径
# 操作日志
LOG_ACCESS_PATH = os.path.join(BASE_DIR, 'log', 'access', 'access.log', )
# 交易记录
LOG_TRANSACTIONS_PATH = os.path.join(BASE_DIR, 'log', 'transactions', 'transactions.log', )
# msg_fmt
MSG_FMT = '[uname:{uname}]-[money:{money}]-[account:{account}]-[mode:{mode}]'
# 默认信用额度
CREDIT = 15000

# 定义日志输出格式
# 时间--姓名--交易模式--交易金额
format_access = '[%(levelname)s][%(asctime)s] %(message)s'
format_transactions = '[%(levelname)s][%(asctime)s] %(message)s'
LOGGING_DICT = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'access': {
            'format': format_access
        },
        'transactions': {
            'format': format_transactions
        },

    },
    'filters': {},
    'handlers': {
        'access': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'access',
            'filename': LOG_ACCESS_PATH,  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        'transactions': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'transactions',
            'filename': LOG_TRANSACTIONS_PATH,  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        'access': {
            'handlers': ['access'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'transactions': {
            'handlers': ['transactions'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
