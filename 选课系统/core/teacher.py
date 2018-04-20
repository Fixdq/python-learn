#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
from lib import common

teacher_info = {
    'name': None
}


def teacher_login():
    pass


@common.login("teacher")
def check_course():
    pass


@common.login("teacher")
def choose_couse():
    pass


@common.login("teacher")
def check_student():
    pass


@common.login("teacher")
def modify_score():
    pass


menu = """
1.登录
2.查看教授课程
3.选择教授课程
4.查看课程下学生
5.修改成绩
"""

menu_dic = {
    '1': teacher_login,
    '2': check_course,
    '3': choose_couse,
    '3': check_student,
    '3': modify_score
}


def teacher_view():
    while True:
        print(menu)
        ch = input('请选择您的操作:').strip()
        if ch == 'q': break
        if ch not in menu_dic: continue
        menu_dic[ch]()
