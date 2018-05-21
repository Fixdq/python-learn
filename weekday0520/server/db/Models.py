#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-20 下午4:28
# @Author  : fixdq
# @File    : Models.py
# @Software: PyCharm

from orm01.fixdqorm import Model, StringField, IntergerField


class User(Model):
    table_name = 'userinfo'
    id = IntergerField('id', primary_key=True)
    name = StringField('name')
    password = StringField('password')
    is_vip = IntergerField('is_vip', default=0)
    locked = IntergerField('locked', default=0)
    user_type = StringField('user_type')


class Movie(Model):
    table_name = 'movie'
    id = IntergerField('id', primary_key=True)
    name = StringField('name')
    path = StringField('path')
    is_free = IntergerField('is_free',default=0)
    is_delete = IntergerField('is_delete',default=0)
    create_time = StringField('create_time')
    user_id = IntergerField('user_id')
    file_md5 = StringField('file_md5')


class Notice(Model):
    table_name = 'notice'
    id = IntergerField('id', primary_key=True)
    name = StringField('name')
    content = StringField('content')
    create_time = StringField('create_time')
    user_id = IntergerField('user_id')

class Record(Model):
    table_name = 'download_record'
    id = IntergerField('id', primary_key=True)
    user_id = IntergerField('user_id')
    movie_id = IntergerField('movie_id')