#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from interface import admin_interface
from interface import common_interface
from lib import common

admin_info = {
    'name': None
}


def login():
    if admin_info['name'] is not None:
        print('您已经登录')
        return
    while True:
        name = input('请输入您的名字:').strip()
        pwd = input('请输入如您的密码:').strip()
        res, msg = common_interface.login_interface(name, pwd, 'admin')
        if res:
            admin_info['name'] = name
            print(msg)
            break
        else:
            print(msg)


def register():
    if admin_info['name'] is not None:
        print('您已经登录')
        return
    while True:
        name = input('请输入您的名字:').strip()
        npwd = input('请输入您的密码:').strip()
        cpwd = input('请确认您的密码:').strip()

        if npwd != cpwd:
            print('两次密码输入不一致!')
            continue
        res, msg = admin_interface.register_interface(name, npwd)
        if res:
            print(msg)
            break
        else:
            print(msg)


@common.login("admin")
def create_school():
    while True:
        school_name = input('请输入学校的名字:').strip()
        school_address = input('请输入学校地址:').strip()
        res, msg = admin_interface.create_school_interface(admin_info['name'],school_name, school_address)
        if not res:
            print(msg)
            continue
        print(msg)
        break


@common.login("admin")
def create_teacher():
    while True:
        name = input('请输入老师的名字').strip()
        res, msg = admin_interface.create_teacher_interface(admin_info['name'],name)
        if not res:
            print(msg)
            continue
        print(msg)
        break

@common.login("admin")
def create_course():
    while True:
        # 显示学校
        school_list = admin_interface.get_all_school()

        for i, school in enumerate(school_list):
            print("%s---%s" % (i,school))

        choice = input('请选择课程所在的学校:').strip()
        if not choice.isdigit():
            print('请正确选择')
            continue
        choice = int(choice)
        if choice <0 or choice>= len(school_list):
            print('请正确选择')
            continue
        # 获取学校名称
        school_name = school_list[choice]

        # 输入课程名
        course_name = input('请输入课程的名字:').strip()

        res,msg = admin_interface.create_course(admin_info['name'],school_name,course_name)
        if not res:
            print(msg)
            continue
        print(msg)
        break

menu = """
1.注册
2.登录
3.创建学校
4.创建老师
5.创建课程
"""

menu_dic = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_teacher,
    '5': create_course
}


def admin_view():
    while True:
        print(menu)
        ch = input('请选择您的操作:').strip()
        if ch == 'q': break
        if ch not in menu_dic: continue
        menu_dic[ch]()
