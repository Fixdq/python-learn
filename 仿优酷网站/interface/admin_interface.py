#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : admin_interface.py
# @Software: PyCharm
import os

import shutil

from db.models import *
from lib import common
from conf import settings
from interface import common_interface


def login(name, pwd):
    return common_interface.login(name, pwd, 'admin')


def register(name, pwd):
    obj = Admin.get_obj_by_name(name)
    if obj:
        return False, '用户已存在'
    Admin(name, pwd)
    return True, '注册成功'


def upload_video(author, file_name, file_size, file_path, type='1'):
    Video(author, file_name, file_size, file_path, type)
    return True, '服务器接收完毕'


def delete_video(admin, delete_name):
    """
    把需要删除的文件，加上下滑线　标记
    :param admin: 
    :param delete_name: 
    :return: 
    """
    old_path = os.path.join(settings.BASE_DB, 'video', delete_name)
    new_path = os.path.join(settings.BASE_DB, 'video', '_%s' % delete_name)
    os.rename(old_path, new_path)
    # shutil.move(old_path, new_path)
    print()
    return True, '删除成功'


def get_all_real_video():
    all_video = common.get_all_file('video')
    # _ 下划线开头的都是标记删除的
    real_video = [v for v in all_video if not v.startswith('_')]
    if real_video:
        return True, real_video
    return False, '没有能操作的视频了'


def notify(admin, content):
    admin = Admin.get_obj_by_name(admin)
    admin.add_notice(content)
    return True, '发布成功'
