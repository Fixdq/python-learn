#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : mysql_test.py
# @Software: PyCharm

import pymysql

host = '127.0.0.1'
port = 3306
user = 'fixd'
pwd = '123'
db = 'db1'

db = pymysql.connect(host=host,
                     user=user,
                     password=pwd,
                     db=db,
                     port=port)
cur = db.cursor()
# # 查询
# sql = 'select * from t1'
#
# try:
#     cur.execute(sql)# 执行sql
#     res = cur.fetchall() #查询所有记录
#     for row in res:
#         print(row)
#
# except Exception as e:
#     print(e.args)
# finally:
#     db.close()
cur.executemany()
sql = '''create table employee();'''