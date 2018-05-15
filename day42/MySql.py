#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : MySql.py
# @Software: PyCharm
import pymysql
from day42 import settings


class MySql:
    __instance = None

    def __init__(self):
        self.conn = pymysql.connect(
            host=settings.host,
            user=settings.user,
            password=settings.password,
            database=settings.database,
            port=settings.port,
            charset=settings.charset,
            autocommit=settings.autocommit
        )
        #
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def close(self):
        """
        关闭mysql 连接
        :return:
        """
        self.cursor.close()
        self.conn.close()

    def select(self, sql, args=None):
        """
        查询功能
        :param sql:
        :param args:
        :return:
        """
        self.cursor.execute(sql, args)
        res = self.cursor.fetchall()
        return res

    def execute(self, sql, args):
        """
        增删改
        :param sql:
        :param args:
        :return:
        """
        try:
            # 执行sql语句
            self.cursor.execute(sql, args)
            # 受影响的行数
            affected = self.cursor.rowcount
        except Exception as e:
            raise e.args
        return affected

    @classmethod
    def singleton(cls):
        if not cls.__instance:
            cls.__instance = cls()
        return cls.__instance
