#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : mysql.py
# @Software: PyCharm

import pymysql
from day42.test2.setting import *


class MySql(object):
    __instance = None

    def __init__(self):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset=charset,
            autocommit=autocommit,
        )
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def select(self, sql, args=None):
        self.cursor.execute(sql, args)
        res = self.cursor.fetchall()
        return res

    def execute(self, sql, args):
        try:
            self.execute(sql, args)
            affected = self.cursor.rowcount
        except Exception as e:
            raise e.args
        return affected

    def close(self):
        self.cursor.close()
        self.conn.close()

    @classmethod
    def singleton(cls):
        if not cls.__instance:
            cls.__instance = cls()
        return cls.__instance
