#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-22 上午11:33
# @Author  : fixdq
# @File    : models.py
# @Software: PyCharm
from orm.fixdorm import Field, StringField, IntergerField, Model


class Record(Model):
    table_name = 'download_record'

    id = IntergerField('id', primary_key=True)
    user_id = IntergerField('user_id')
    movie_id = IntergerField('movie_id')


class User(Model):
    table_name = 'userinfo'

    id = IntergerField('id', primary_key=True)
    name = StringField('name')
    password = StringField('password')
    is_vip = IntergerField('is_vip', default=0)
    locked = IntergerField('locked', default=0)
    user_type = StringField('user_type')
