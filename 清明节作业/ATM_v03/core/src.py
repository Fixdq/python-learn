#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from interface import user
from interface import bank
from lib import common
c_user = {
    'name': None,
    'is_auth': False
}


def login():
    if c_user['is_auth']:
        print('您已登录')
        return
    while True:
        name = input('请输入用户名：').strip()
        user_dic = user.get_userinfo_interface(name)
        if not user_dic:
            print('用户名不存在！')
            continue
        pwd = input('请输入密码：').strip()
        if user_dic['password'] == pwd:
            print('登录成功！')
            c_user['name'] = name
            c_user['is_auth'] = True

            break


def register():
    if c_user['is_auth']:
        print('您已登录')
        return

    while True:
        name = input('请输入用户名').strip()
        if user.get_userinfo_interface(name):
            print("用户名存在！")
            continue
        pwd = input('请输入您的密码').strip()
        pwd1 = input('请确认您的密码').strip()
        if pwd == pwd1:
            user.register_interface(name, pwd)
            print('恭喜您注册成功！')
            break
        else:
            print('您两次输入的密码不一致！')

@common.is_auth
def repay():
    while True:
        account = input('请输入您要还款的金额：').strip()
        if not account.isdigit():
            print('金额输入错误')
            continue
        account = int(account)
        bank.repay_interface(c_user['name'], account)
        print('还款成功！')
        break

@common.is_auth
def withdraw():
    while True:
        account = input('请输入您的取款金额：').strip()
        if not account.isdigit():
            print('金额输入错误')
            continue
        account = int(account)
        balance = user.get_userinfo_interface(c_user['name'])['account']
        if account <= balance:
            bank.withdraw_interface(c_user['name'], account)
            print('取款成功！')
            break
        else:
            print('您的余额不足')

@common.is_auth
def transfer():
    while True:
        to_user = input('请输入您要转账人的名字：').strip()
        if not user.get_userinfo_interface(to_user):
            print('用户名不存在')
            continue
        account = input('请输入你要转账的金额：').strip()
        if not account.isdigit():
            print('金额输入错误')
            continue
        account = int(account)
        balance = user.get_userinfo_interface(c_user['name'])['account']
        if account <= balance:
            bank.transfer_interface(c_user['name'], to_user, account)
            print('转账成功！')
            break
        else:
            print('您的余额不足')

@common.is_auth
def check_balance():
    balance = bank.check_balance_interface(c_user['name'])
    print('您的余额还有：%s' % balance)

@common.is_auth
def check_record():
    records = bank.check_record_interface(c_user['name'])
    print('您的流水账单')
    for record in records:
        print(record)

@common.is_auth
def shop():
    pass

@common.is_auth
def check_shopcar():
    pass


menu = {
    '1': login,
    '2': register,
    '3': repay,
    '4': withdraw,
    '5': transfer,
    '6': check_balance,
    '7': check_record,
    '8': shop,
    '9': check_shopcar,
}


def run():
    while True:
        print("""
        '1': login,
        '2': register,
        '3': repay,
        '4': withdraw,
        '5': transfer,
        '6': check_balance,
        '7': check_record,
        '8': shop,
        '9': check_shopcar,
        """)
        choice = input('请输入您的选择：').strip()
        if choice not in menu:
            print('输入错误！')
            continue
        menu[choice]()
