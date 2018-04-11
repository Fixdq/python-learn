#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from db import db_handler


def get_userinfo_interface(name):
    return db_handler.select(name)


def register_interface(name, pwd, credit=15000):
    user_dic = {
        'name': name,
        'password': pwd,
        'account': credit,
        'credit': credit,
        'locked': False,
        'shop_car': {},
        'ban': [],
    }

    db_handler.update(user_dic)


def lock_user(name):
    user_dic = db_handler.select(name)
    user_dic['locked'] = True
    db_handler.update(user_dic)



def unlock_user(name):
    user_dic = db_handler.select(name)
    user_dic['locked'] = False
    db_handler.update(user_dic)
