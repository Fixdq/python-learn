#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : mysql.py
# @Software: PyCharm

import pymysql
from day43.test1.setting import *


class MySql:
    __instance = None

    def __init__(self):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset=charset,
            autocommit=autocommit
        )
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def select(self, sql, args=None):
        try:
            self.cursor.execute(sql, args)
            res = self.cursor.fetchall()
        except Exception as e:
            raise e.args
        return res

    def execute(self, sql, args):
        try:
            self.cursor.execute(sql, args)
            affected = self.cursor.rowcount
        except BaseException as e:
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
