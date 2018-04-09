#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from db import db_handler


def get_userinfo_interface(name):
    return db_handler.select(name)


def register_user(name, pwd, balance=15000):
    user_dic = {'name': name,
                'password': pwd,
                'locked': False,
                'account': balance,
                'credit': balance,
                'shopping_cart': {},
                'bankflow': []
                }
    db_handler.update(user_dic)

