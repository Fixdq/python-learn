#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : mysql.py
# @Software: PyCharm


from day43.test_tool.db_utlis import *


class MySql:

    def __init__(self):
        self.conn = POOL.connection()
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
