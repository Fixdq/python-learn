#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-20 下午3:43
# @Author  : fixdq
# @File    : setting.py
# @Software: PyCharm
import os

from db.Models import Notice
from db.Models import *
from lib import common
from conf import setting


@common.login_auth
def pay_vip(conn, data):
    user = User.select_one(id=data['user_id'])
    user.is_vip = 1
    user.update()
    back_data = {'flag': True, 'msg': '会员开通成功'}
    common.send(conn, back_data)


@common.login_auth
def download_movie(conn, data):
    movie = Movie.select_one(id=data['movie_id'])
    file_name = movie.name
    file_path = movie.path
    file_size = os.path.getsize(file_path)

    send_data = {'flag': True,
                 'file_name': file_name,
                 'file_size': file_size}

    user = User.select_one(id=data['user_id'])

    send_data['wait_time'] = 0
    if data['movie_type'] == 'free':
        if not user.is_vip:
            send_data['wait_time'] = 30
    # 保存下载记录
    record = Record(user_id=data['user_id'], movie_id=data['movie_id'])
    record.save()

    common.send(conn, send_data)
    with open(file_path, 'rb') as f:
        for line in f:
            conn.send(line)


@common.login_auth
def get_movies(conn, data):
    movies = Movie.select_many(is_delete=0)
    if not movies:
        back_data = {'flag': False, 'msg': '没有视频'}
        common.send(conn, back_data)
        return
    if data['movie_type'] == 'free':
        movie_list = [[movie.id, movie.name] for movie in movies if movie.is_free == 0]

    elif data['movie_type'] == 'fee':
        movie_list = [[movie.id, movie.name] for movie in movies if movie.is_free == 1]

    back_data = {'flag': True, 'msg': movie_list}
    common.send(conn, back_data)


@common.login_auth
def get_notices(conn, data):
    type = data['notice_type']
    notice = Notice.select_many()
    if not notice:
        back_data = {'flag': False, 'msg': '还没有发布公告'}

    else:
        if type:  # 1
            notices = [[n['name'], n['content'], n['create_time']] for n in notice]
            lates_notice = sorted(notices, key=lambda nt: nt[2],reverse=True)[0]

            back_data = {'flag': True, 'msg': [lates_notice[0], lates_notice[1]]}

        else:  # 0
            back_data = {'flag': True, 'msg': [[n['name'], n['content']] for n in notice]}
    common.send(conn, back_data)


@common.login_auth
def get_records(conn, data):
    records = Record.select_many(user_id=data['user_id'])

    if not records:
        back_data = {'flag': True, 'msg': '没有观影记录'}
        common.send(conn, back_data)
    else:
        re = [Movie.select_one(id=record['movie_id']).name for record in records]
        back_data = {'flag': True, 'msg': re}
        common.send(conn, back_data)
