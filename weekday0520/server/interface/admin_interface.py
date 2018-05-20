#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-20 下午3:43
# @Author  : fixdq
# @File    : setting.py
# @Software: PyCharm

from server.db.Models import Notice
from server.db.Models import Movie
from server.lib import common
from server.conf import setting


@common.login_auth
def notice(conn, data):
    notice = Notice(name=data['title'],
                    content=data['content'],
                    create_time=common.get_nowtime(),
                    user_id=data['user_id'])
    notice.save()
    back_dic = {'flag': True, 'msg': '发布成功'}
    common.send(conn, back_dic)


@common.login_auth
def upload(conn, data):
    file_size = data['file_size']
    file_name = data['file_name']
    is_free = data['is_free']
    file_md5 = data['file_md5']
    user_id = data['user_id']

    upload_path = setting.BASE_DIR_MOVIES
    recv_size = 0
    while recv_size < file_size:
        conn.recv(8192)
        recv_size += 8192

    movie = Movie()
    movie.path = upload_path
    movie.name = common.get_uuid(file_name) + file_name
    movie.is_free = is_free
    movie.file_md5 = file_md5
    movie.user_id = user_id

    movie.save()
    back_data = {'flag': True, 'msg': '上传成功'}
    common.send(conn, back_data)


@common.login_auth
def check_movie(conn, data):
    file_md5 = data['file_md5']
    movie = Movie.select_one(file_md5=file_md5)

    if movie:
        back_data = {'flag': False, 'msg': '视频已存在'}
        common.send(conn, back_data)
    else:
        back_data = {'flag': True}
        common.send(conn, back_data)


@common.login_auth
def get_movie_all(conn, data):
    movies = Movie.select_many(is_delete=0)
    if movies:
        movie_list = [[movie.id, movie.name] for movie in movies]
        back_data = {'flag': True, 'msg': movie_list}
        common.send(conn, back_data)
    else:
        back_data = {'flag': False, 'msg': '没有视频可以删除'}
        common.send(conn, back_data)


@common.login_auth
def delete_movie_by_id(conn, data):
    delete_id = data['id']

    movie = Movie.select_one(id=delete_id)
    movie.is_delete = 1
    movie.update()
    back_data = {'flag': True, 'msg': '没有视频可以删除'}
    common.send(conn, back_data)
