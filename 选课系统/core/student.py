#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
from lib import common

student_info = {
    'name': None
}


def student_login():
    pass


def student_register():
    pass


@common.login("student")
def choose_school():
    pass


@common.login("student")
def create_course():
    pass


@common.login("student")
def check_score():
    pass


menu = """
1.注册
2.登录
3.选择学校
4.选择课程
5.查看分数
"""

menu_dic = {
    '1': student_login,
    '2': student_register,
    '3': choose_school,
    '3': create_course,
    '3': check_score
}


def student_view():
    while True:
        print(menu)
        ch = input('请选择您的操作:').strip()
        if ch == 'q': break
        if ch not in menu_dic: continue
        menu_dic[ch]()
