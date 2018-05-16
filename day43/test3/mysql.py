#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : mysql.py
# @Software: PyCharm

from day43.test3.db_utlis import *


class MySql:
    def __init__(self):
        self.conn = POOL.connection()
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def select(self, sql, args=None):
        self.cursor.execute(sql, args)
        res = self.cursor.fetchall()
        return res

    def execute(self, sql, args):
        try:
            self.cursor.execute(sql, args)
            affected = self.cursor.rowcount
        except Exception as e:
            raise e.args
        return affected

    def close(self):
        self.conn.close()
