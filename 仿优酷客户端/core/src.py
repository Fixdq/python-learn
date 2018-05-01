#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : src.py
# @Software: PyCharm
from core import user,admin
menu="""
1.用户视图
2.管理视图
"""
menu_dic={
    '1':user.show,
    '2':admin.show
}
def run():
    while True:
        print(menu)
        ch = input('>>>:').strip()
        if ch =='q':break
        if ch not in menu_dic:continue
        menu_dic[ch]()

