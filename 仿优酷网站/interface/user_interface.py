#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : user_interface.py
# @Software: PyCharm
import os

from db.models import *
from conf import settings
from lib import common
from interface import common_interface


def login(name, pwd):
    res, msg = common_interface.login(name, pwd, 'user')
    if res:
        notice = get_new_notice()
        if notice:
            return res, msg, notice
    return res, msg, None


def get_all_notice():
    """
    获取全部公告
    :return: 
    """
    notices_name = common.get_all_file('notice')
    if not notices_name:
        return False, '还没有公告！'
    # 按时间降序
    notices_name.sort(reverse=True)
    notices = [Notice.get_obj_by_name(n).get_notice_content() for n in notices_name]
    return True, notices


def get_new_notice():
    """
    获取最新的一条公告
    :return: 
    """
    notices_name = common.get_all_file('notice')
    if not notices_name:
        return False
    # 按时间降序
    notices_name.sort(reverse=True)
    notice = Notice.get_obj_by_name(notices_name[0])
    return notice.get_notice_content()


def register(name, pwd):
    obj = User.get_obj_by_name(name)
    if obj:
        return False, '用户已存在'
    User(name, pwd)
    return True, '注册成功'


def check_vip(user_name):
    obj = User.get_obj_by_name(user_name)
    if obj.vip:
        return True, '您已经是ｖｉｐ了'
    else:
        return False, '您还不是ｖｉｐ'


def vip(user_name):
    obj = User.get_obj_by_name(user_name)
    if obj.account <= 50:
        return False, '用户余额不足，请充值'
    obj.account -= 50
    obj.vip = True
    obj.save()
    return True, '开通成功'


def check_videos():
    """
        获取全部视频
        :return: 
        """
    all_video = common.get_all_file('video')
    # _ 下划线开头的都是标记删除的
    real_video = [v for v in all_video if not v.startswith('_')]
    if real_video:
        return True, real_video
    return False, '还没视频'


def git_videos_type(video_name):
    video = Video.get_obj_by_name(video_name)
    return video.type


def get_video_by_name(video_name):
    return Video.get_obj_by_name(video_name)


def down_free_videos(user_name, video_name):
    user = User.get_obj_by_name(user_name)
    user.add_view_history(time.strftime("%Y-%m-%d %X"), video_name)
    return True


def down_fee_videos(user_name, video_name):
    user = User.get_obj_by_name(user_name)
    if user.vip:
        if user.account < 5:
            return False
    if not user.vip:
        if user.account < 10:
            return False

    if user.vip:
        user.account -= 5
    else:
        user.account -= 10

    user.add_view_history(time.strftime("%Y-%m-%d %X"), video_name)
    return True


def check_history(user_name):
    user = User.get_obj_by_name(user_name)
    if user.view_history:
        return True, user.view_history
    return False, '还没有看过电影'


def recharge(user_name, recharge_money):
    user = User.get_obj_by_name(user_name)
    user.account += recharge_money
    user.save()
    return True, '成功充值：%s ' \
                 '余额：%s' % (recharge_money, user.account)
