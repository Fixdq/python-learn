#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : fuckorm.py
# @Software: PyCharm
from day42.test1 import MySql


class Field:
    def __init__(self, name, colum_type, primary_key, default):
        self.name = name
        self.colum_type = colum_type
        self.primary_key = primary_key
        self.default = default


class StringField(Field):
    def __init__(self, name, colum_type='varchar(200)', primary_key=False, default=None):
        super().__init__(name, colum_type, primary_key, default)


class IntergerField(Field):
    def __init__(self, name, colum_type='int', primary_key=False, default=0):
        super().__init__(name, colum_type, primary_key, default)


class ModelMetaClass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        table_name = attrs.get('table_name', None)
        if not table_name:
            table_name = name
        primary_key = None
        mappings = {}

        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
                if v.primary_key:
                    if primary_key:
                        raise TypeError('主键重复')
                    primary_key = k  # 设置主键
        for k in mappings.keys():
            attrs.pop(k)

        if not primary_key:
            raise TypeError('主键错误，没有设置')
        attrs['table_name'] = table_name
        attrs['primary_key'] = primary_key
        attrs['mappings'] = mappings

        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):

    def __getattr__(self, item):
        try:
            return self[item]
        except Exception as e:
            raise e.args

    def __setattr__(self, key, value):
        self[key] = value

    # 　具体的数据操作方法

    @classmethod
    def select_all(cls, **kwargs):
        ms = MySql.Mysql.singleton()
        if kwargs:
            key = list(kwargs.keys())[0]
            value = kwargs[key]

            sql = "select * from %s where %s = ?" % (cls.table_name, key)
            sql = sql.replace('?', '%s')
            res = ms.select(sql, value)
        else:
            # 没有参数查询全部
            sql = "select * from %s" % cls.table_name
            res = ms.select(sql)

        return [cls(**r) for r in res]

    @classmethod
    def select_one(cls, **kwargs):
        ms = MySql.Mysql.singleton()
        key = list(kwargs.keys())[0]
        value = kwargs[key]

        sql = "select * from %s where %s = ?" % (cls.table_name, key)
        sql = sql.replace('?', '%s')
        res = ms.select(sql, value)
        return cls(**res[0])


class User(Model):
    table_name = 'user'
    id = IntergerField('id', primary_key=True)
    name = StringField('name')
    balance = IntergerField('balance')


if __name__ == '__main__':
    user = User()

    res = user.select_all()
    print(res)
