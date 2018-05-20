#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-20 下午3:09
# @Author  : fixdq
# @File    : src.py
# @Software: PyCharm

from client.core import admin,user
menu ="""
1.用户
2.管理员
"""

menu_dic = {
    '1':user.view,
    '2':admin.view
}


def run():
    while True:
        print(menu)
        ch = input('>>>:').strip()
        if ch =='q':break
        if ch not in menu_dic:continue
        menu_dic[ch]()