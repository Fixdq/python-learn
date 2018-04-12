#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from interface import user
from interface import bank
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
        if name == 'q':break
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
        if 'q' == name:break
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
    user_balance = bank.get_balance_interface(cur_user['name'])
    print('您的余额为：%s' % user_balance)

@common.login_auth
def transfer():
    while True:
        to_user = input('请输入您要转账人的名字：').strip()
        if not user.get_userinfo_interface(to_user):
            print('转账人不存在！')
            continue
        account = input('请输入您的转账金额：').strip()
        if not account.isdigit():
            print('请输入正确的转账金额！')
            continue
        balance = user.get_userinfo_interface(cur_user['name'])['account']
        account = int(account)
        if balance < account:
            print('您的账户余额不足！')
            continue
        bank.transfer_interface(to_user,cur_user['name'],account)
        print('转账成功')
        break
@common.login_auth
def repay():
    while True:
        account = input('请输入您的还款金额：').strip()
        if not account.isdigit():
            print('请输入正确的还款金额')
            continue
        account = int(account)
        bank.repay_interface(cur_user['name'],account)
        print('还款成功！')
        break


@common.login_auth
def withdraw():
    while True:
        account = input('请输入取款金额：').strip()
        if bank.withdraw_interface(cur_user['name'],account):
            print('取款成功！')
            break
        else:
            print('您的余额不足')
            continue
@common.login_auth
def check_records():
    user_records = bank.check_record(cur_user['name'])
    for record in user_records:
        print(record)

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
                '1': login,
                '2': register,
                '3': check_balance,
                '4': transfer,
                '5': repay,
                '6': withdraw,
                '7': check_records,
                '8': shopping,
                '9': check_shopping_cart
        ''')
        ch = input('input you choice').strip()
        if ch in menu:
            menu[ch]()
        else:
            print('input error')
