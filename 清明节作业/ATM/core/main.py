#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
"""
程序主要逻辑
"""
from core import transaction as ta
from core import auth
from core import db_handler as db
from core import decorator as deco
from core import shopping as sh
from lib import common

# 获取logger对象
logger = common.get_logger('access')


# 登录
def login():
    logger.info('登录')
    auth.login()


# 注册
def register():
    logger.info('注册')
    auth.register()


# 购物
@deco.auth
def shopping():
    logger.info('购物')
    sh.shopping()


# 查询
@deco.auth
def show_info():
    logger.info('查询')
    ta.show_user_info()


# 转账
@deco.auth
def transfer():
    logger.info('转账')
    ta.transfer()


# 还款
@deco.auth
def pay_back():
    logger.info('还款')
    ta.pay_back()


# 取现
@deco.auth
def with_draw():
    logger.info('取现')
    ta.with_draw()


# 入口
def run():
    db.rm_cur_user()
    while True:
        print('''
        1.登录
        2.注册
        3.购物
        4.查余额
        5.转账
        6.还款
        7.取现
        8.退出登录
        9.退出程序
        ''')
        choice = input('请选择操作:')
        if choice == '1':
            if db.get_cur_user():
                print('您已登录！')
            else:
                login()
        elif choice == '2':
            if db.get_cur_user():
                print('您已登录，请退出在进行注册！')
            else:
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
        elif choice == '8':
            if db.get_cur_user():
                db.rm_cur_user()
                print('已退出登录！')
            else:
                print('您还没有登录！！！')

        elif choice == '9':
            db.rm_cur_user()
            break
        else:
            print('输入不正确！')
