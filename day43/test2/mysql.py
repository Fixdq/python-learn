#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : mysql.py
# @Software: PyCharm

from day43.test2.db_utlis import *


class MySql:
    def __init__(self):
        self.conn = POOL.connection()
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def select(self, sql, args =None):
        self.cursor.execute(sql, args)
        res = self.cursor.fetall()
        return res

    def execute(self, sql, args):
        self.cursor.execute(sql, args)
        affected = self.cursor.rowcount
        return affected

    def close(self):
        self.cursor.close()
        self.conn.close()
