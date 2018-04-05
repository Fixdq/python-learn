#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from core import transaction as ta
from core import auth
from conf import settings
from lib import common

logger = common.get_logger('src')



def login():
    auth.login()


def register():
    auth.register()


def shopping():
    print('shopping')
    pass


def show_info():
    ta.show_user_info()


def transfer():
    ta.transfer()


def pay_back():
    ta.pay_back()


def with_draw():
    ta.with_draw()


def run():
    while True:
        print('''
        1.登录
        2.注册
        3.购物
        4.查余额
        5.转账
        6.还款
        7.取现
        ''')
        choice = input('请选择操作:')
        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            shopping()
        elif choice == '4':
            show_info()
        elif choice == '5':
            transfer()
        elif choice == '6':
            pay_back()
        elif choice == '7':
            with_draw()
        else:
            print('输入不正确！')
