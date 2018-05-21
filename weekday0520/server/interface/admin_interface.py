#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-20 下午3:43
# @Author  : fixdq
# @File    : setting.py
# @Software: PyCharm
import os

from db.Models import Notice
from db.Models import Movie
from lib import common
from conf import setting


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

    upload_path = os.path.join(setting.BASE_DIR_MOVIES,file_name)
    recv_size = 0
    with open(upload_path,'wb')as f:
        while recv_size < file_size:
            re = conn.recv(1024)
            f.write(re)
            recv_size += len(re)

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
def get_movie_all(conn,data):
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

