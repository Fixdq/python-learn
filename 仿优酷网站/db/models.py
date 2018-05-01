#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : models.py
# @Software: PyCharm
import time

from db import db_hanlder


class BaseClass(object):
    def save(self):
        db_hanlder.save(self)

    @classmethod
    def get_obj_by_name(cls, name):
        return db_hanlder.select(name, cls.__name__.lower())


class User(BaseClass):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.account = 0
        self.vip = False
        self.view_history = {}
        self.save()

    def add_view_history(self, date, video_name):
        self.view_history[date] = video_name
        self.save()

    def set_vip(self):
        self.vip = True
        self.save()

    def del_vip(self):
        self.vip = False
        self.save()


class Admin(BaseClass):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.save()

    def add_notice(self, content):
        t = time.strftime("%Y-%m-%d %X")
        Notice(t, self.name, content)




# class NoticeManager(BaseClass):
#     def __init__(self):
#         self.notices = []
#
#     def add_notice(self, author, content):
#         t = time.strftime("%Y-%m-%d %X")
#         self.notices.append(t)
#         notice = Notice(t, author, content, )
#         path = notice.save_notice()

class Notice(BaseClass):
    def __init__(self, date, author, content):
        self.name = date
        self.author = author
        self.date = date
        self.content = content
        self.save()

    def get_notice_content(self):
        return """
----------------{date}----------------

{content}

发布者:{author}
---------------------------------------------------
        """.format(
            date=self.date,
            content=self.content,
            author=self.author
        )


class Video(BaseClass):
    def __init__(self, author, name, size, path, type='1'):
        self.author = author
        self.name = name
        self.size = size
        self.md5 = None
        self.date = time.strftime("%Y-%m-%d %X")
        self.path = path
        self.type = type
        self.save()
