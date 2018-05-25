#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-24 下午9:01
# @Author  : fixdq
# @File    : mysql.py
# @Software: PyCharm

import pymysql
from day49.orm.mysql_pool import POOL


class MySql:

    def __init__(self):
        self.conn = POOL.connection()
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def select(self, sql, args=None):
        self.cursor.execute(sql, args)
        return self.cursor.fetchall()

    def execute(self, sql, args):
        return self.cursor.execute(sql, args)
