#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : pysql_test.py
# @Software: PyCharm

# import pymysql
#
# # 连接数据数据库的必要信息
# host = '127.0.0.1'  # 数据库地址
# port = 3306  # 端口
# user = 'fixd'  # 用户名
# password = '123'  # 密码
# db = 'db_test'  # 连接到的数据库名称
# charset = 'utf8'  # 字符编码，防止中文乱码
#
# # 连接数据库  返回 数据库的连接
# conn = pymysql.connect(
#     host=host,
#     port=port,
#     user=user,
#     password=password,
#     db=db,
#     charset=charset,
# )
# # 获取游标
# cur = conn.cursor()
# # 获取游标，pymysql.cursors.DictCursor以字典的形式 返回结果
# # cur_dic = conn.cursor(pymysql.cursors.DictCursor)
#
# # 需要执行的sql语句
# sql = "select name,password from userinfo"
#
# rows = cur.execute(sql)  # 执行sql语句，返回值 受影响的行数
# res = cur.fetchall()  # 查询全部数据，默认返回的是元组的形式
# print(res)  # (('fixd', '123'), ('kitty', '456'))
#
# # res = cur.fetchone()    # 获取下一个查询的结果，就是一条记录
# # print(res)              #('fixd', '123')
# # res = cur.fetchone()    # 每执行一次 ，获取一条记录
# # print(res)              #('kitty', '456')
#
# res = cur.fetchmany(2)  # 指定每次获取的结果条数
# # print(res)  # (('fixd', '123'), ('kitty', '456'))
#
#
# # 以字典的形式返回结果
# # rows = cur_dic.execute(sql)
# # res = cur_dic.fetchall()
# # print(res)
# # #[{'name': 'fixd', 'password': '123'}, {'name': 'kitty', 'password': '456'}]
#
#
# # 回收资源
# cur.close()
# conn.close()

# import pymysql
#
# # 连接数据数据库的必要信息
# host = '127.0.0.1'  # 数据库地址
# port = 3306  # 端口
# user = 'fixd'  # 用户名
# password = '123'  # 密码
# db = 'db_test'  # 连接到的数据库名称
# charset = 'utf8'  # 字符编码，防止中文乱码
#
# # 连接数据库  返回 数据库的连接
# conn = pymysql.connect(
#     host=host,
#     port=port,
#     user=user,
#     password=password,
#     db=db,
#     charset=charset,
# )
# # 获取游标
# cur = conn.cursor()
#
# # # 第一种方式，直接拼接sql语句
# # sql = "insert into userinfo(name,password) values ('%s','%s')" % ('lili','123')
# # rows = cur.execute(sql)  # 执行sql语句，返回值 受影响的行数
# # conn.commit()           # 这一句必须执行，否则数据无法提交到数据库
#
# # 第二种方式 ，
# sql = "insert into userinfo(name,password) values (%s,%s)"
# # 插入单条数据
# # rows = cur.execute(sql, ('lili1', '123'))
# # 插入多条数据
# rows = cur.executemany(sql, [
#     ('kk1', '123'),
#     ('kk2', '123'),
#     ('kk3', '123'),
#     ('kk4', '123'),
# ])
#
# conn.commit() # 提交数据
#
# # 回收资源
# cur.close()
# conn.close()


import pymysql

# 连接数据数据库的必要信息
host = '127.0.0.1'  # 数据库地址
port = 3306  # 端口
user = 'fixd'  # 用户名
password = '123'  # 密码
db = 'db_test'  # 连接到的数据库名称
charset = 'utf8'  # 字符编码，防止中文乱码

# 连接数据库  返回 数据库的连接
conn = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    db=db,
    charset=charset,
)
# 获取游标
cur = conn.cursor()
# # 更新数据
# sql = "update userinfo set password = %s where name = %s"
# cur.execute(sql,('789','kk2'))
# conn.commit() # 提交数据

# 删除数据
sql = "delete from userinfo where name = %s"
cur.execute(sql, 'kk3')
conn.commit()  # 提交数据

# 回收资源
cur.close()
conn.close()
