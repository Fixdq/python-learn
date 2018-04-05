#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


from conf import settings
from lib import common

logger = common.get_logger('src')

def login():
    with open(settings.DB_PATH, encoding='utf-8') as f:
        print(f.read())


def register():
    pass


def shopping():
    pass


def transfer():
    logger('3333')


def pay():
    pass


def run():
    while True:
        print('''
        1.登录
        2.注册
        3.购物
        4.转账
        5.支付
        ''')
        choice = input('请选择操作:')
        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            shopping()
        elif choice == '4':
            transfer()
        elif choice == '5':
            pay()
        else:
            print('输入不正确！')
