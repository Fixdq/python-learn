#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-25 下午8:24
# @Author  : fixdq
# @File    : start.py
# @Software: PyCharm

from core import admin
from core import user

menu = """
1.用户
2.管理
"""
menu_dic = {
    '1': user.view,
    '2': admin.view,
}


def run():
    while True:
        print(menu)
        ch = input('>>>').strip()
        if ch == 'q ': break
        if ch not in menu_dic: continue
        menu_dic[ch]()
