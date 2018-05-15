#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : fuckorm.py
# @Software: PyCharm
from day42.test3.mysql import MySql


class Field(object):
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
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)
        table_name = attrs.get('table_name', None)
        if not table_name:
            table_name = name
        primary_key = None
        mapping = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mapping[k] = v
                if v.primary_key:
                    if primary_key:
                        raise KeyError("主键重复")
                    primary_key = k

        if not primary_key:
            raise KeyError('主键不存在')

        for k in mapping:
            attrs.pop(k)

        attrs['table_name'] = table_name
        attrs['primary_key'] = primary_key
        attrs['mapping'] = mapping

        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise KeyError('%skey不存在' % item)

    def __setattr__(self, key, value):

        self[key] = value

    @classmethod
    def select_all(cls, **kwargs):
        ms = MySql.singleton()
        if kwargs:
            key = list(kwargs.keys())[0]
            value = kwargs(key)
            sql = "select * from %s where %s = ?" % (cls.table_name, key)
            sql.replace('?', '%s')
            res = ms.select(sql, value)
        else:
            sql = "select * from %s" % cls.table_name
            res = ms.select(sql)
        return [cls(**re) for re in res]

    @classmethod
    def select_one(cls, **kwargs):
        ms = MySql.singleton()
        key = list(kwargs.keys())[0]
        value = kwargs(key)
        sql = "select * from %s where %s = ?" % (cls.table_name, key)
        sql.replace('?', '%s')
        res = ms.select(sql, value)

        if res:
            return cls(**res[0])
        else:
            return None


class User(Model):
    table_name = 'user'

    id = IntergerField('id', primary_key=True)
    name = StringField('name', )
    balance = IntergerField('balance', default=0)


if __name__ == '__main__':
    user = User()
    res = user.select_all()
    # res = user.select_one(id=2)
    print(res)
