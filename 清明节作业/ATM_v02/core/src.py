#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from interface import user
from lib import common

cur_user = {
    'name': None,
    'is_auth': False
}


def register():
    if cur_user['name'] is not None:
        print('您已经登录了')
        return
    while True:
        name = input('input you name').strip()
        user_dic = user.get_userinfo_interface(name)
        if user_dic:
            print('用户名已存在！')
            continue
        pwd1 = input('input you passwoed').strip()
        pwd2 = input('confirm you passwoed').strip()
        if pwd1 == pwd2:
            user.register_interface(name, pwd2)
            print('register success')
            break
        else:
            print('两次密码输入不一致！')
            continue


def login():
    if cur_user['name'] is not None:
        print('您已经登录了')
        return
    count = 0
    while True:
        name = input('input you name').strip()
        pwd = input('input you password').strip()
        user_dic = user.get_userinfo_interface(name)

        if not user_dic:
            print('用户不存在')
            continue
        if count == 3:
            user.lock_user(name)
            print('您已被锁定')
            continue
        if user_dic['password'] == pwd and not user_dic['locked']:
            cur_user['name'] = name
            cur_user['is_auth'] = True
            print('登录成功')
            break
        else:
            count += 1
            print('密码错误或账户已被锁定')
            continue

@common.login_auth
def check_balance():
    pass

@common.login_auth
def transfer():
    pass

@common.login_auth
def repay():
    pass

@common.login_auth
def withdraw():
    pass

@common.login_auth
def check_records():
    pass

@common.login_auth
def shopping():
    pass

@common.login_auth
def check_shopping_cart():
    pass


menu = {

    '1': login,
    '2': register,
    '3': check_balance,
    '4': transfer,
    '5': repay,
    '6': withdraw,
    '7': check_records,
    '8': shopping,
    '9': check_shopping_cart
}


def run():
    while True:
        print('''
            1 login
            2 register
        ''')
        ch = input('input you choice').strip()
        if ch in menu:
            menu[ch]()
        else:
            print('input error')
