#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from interface import user


def login():
    pass


def register():
    while True:
        name = input('用户名：')
        user_dic = user.get_userinfo_interface(name)
        if user_dic:
            print('用户已存在！')
            continue
        else:
            pwd = input('密码：')
            con_pwd = input('确认密码：')
            if pwd == con_pwd:
                user.register_user(name, pwd)
            else:
                print('password not equles')
                continue


menu = {
    '1': register,
}


def run():
    while True:
        for item in menu:
            print('%s : %s' % (item, menu[item].__name__))
        choice = input('请选择你的操作：').strip()
        if choice not in menu: continue
        menu[choice]()
