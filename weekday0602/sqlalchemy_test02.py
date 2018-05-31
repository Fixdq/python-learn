#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-30 下午3:54
# @Author  : fixdq
# @File    : sqlalchemy_test01.py
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker

# 创建实例，并连接数据库

engine = create_engine("mysql+pymysql://fixd:123@127.0.0.1:3306/db_test", encoding='utf-8', echo=True)

metadata = MetaData()

user = Table(
    'user', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('password', String(64)),

)


class User(object):
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

    def __repr__(self):
        return "<User(name='%s',  password='%s')>" % (self.name, self.password)

mapper(User, user)  # 关联user 与 User

# 创建与数据库的回话 session class 注意这里返回给session的是个class 不是实例

Session_class = sessionmaker(bind=engine)  # 实例和engine绑定
Session = Session_class()  # 生成session实例，相当于游标

# user_boj = User(id=11, name='fixd', password='123456')
# print(user_boj.id, user_boj.name, user_boj.password)
#
# Session.add(user_boj)
# print(user_boj.id, user_boj.name, user_boj.password)
# Session.commit()
# #
myuser = Session.query(User).filter_by().all()

print(myuser)
# print(myuser.id, myuser.name, myuser.password)
