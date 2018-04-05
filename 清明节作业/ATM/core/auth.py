#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from conf import settings
from core import db_handler


# 用户认证装饰器
def auth(func):
    def wrapper(*args, **kwargs):
        if db_handler.get_is_auth():
            return func(*args, **kwargs)
        else:
            print("您还没登录！")

    return wrapper


# 用户登录
def login():
    # 登录
    while True:
        uname = input('用户名：').strip()
        pwd = input('密码：').strip()
        if len(uname) == 0 or len(pwd) == 0:
            print('用户名和密码不能为空')
            continue
        if db_handler.db_validate_user(uname, pwd):
            # 登录成功  添加用户名
            db_handler.add_cur_user(uname)
            print('登录成功')
            break
        else:
            print('用户名或密码错误！')


# 用户注册
def register():
    uname = get_uname()
    pwd = get_pwd()
    money = get_money()
    db_handler.db_add_user(uname, pwd, money)
    print('注册成功')


# 获取输入的用户名
def get_uname():
    while True:
        uname = input('请输入用户名：').strip()
        if len(uname) == 0:
            print('用户名不能为空')
            continue
        if not uname.isalpha():
            print('用户名必须为字母组成')
            continue
        # 验证用户名是否存在
        if db_handler.db_validate_user(uname):
            print('用户名已存在')
        else:
            return uname


# 获取输入的密码
def get_pwd():
    while True:
        pwd1 = input('请输入密码：').strip()
        pwd2 = input('请再次输入密码：').strip()
        if len(pwd1) == 0 or len(pwd2) == 0:
            print('密码不能为空')
            continue
        if pwd2 == pwd1:
            return pwd1
        else:
            print('两次密码输入不一致')


# 获取充值的金额
def get_money():
    while True:
        balance = input('请输入充值金额：').strip()
        if len(balance) == 0:
            print('输入不能为空')
            continue
        if balance.isdigit():
            balance = int(balance)
            if balance < 0:
                print('金额输入不正确')
                continue
            else:
                return balance
        else:
            print('金额输入不正确')
