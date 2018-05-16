#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : fuckorm.py
# @Software: PyCharm

from day43.test2.mysql import *


class Field:
    def __init__(self, name, coloum_type, primary_key, default):
        self.name = name
        self.coloum_type = coloum_type
        self.primary_key = primary_key
        self.default = default


class StringField(Field):
    def __init__(self, name, coloum_type='varchar(200)', primary_key=False, default=None):
        super().__init__(name, coloum_type, primary_key, default)


class IntergerField(Field):
    def __init__(self, name, coloum_type='int', primary_key=False, default=0):
        super().__init__(name, coloum_type, primary_key, default)


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)
        table_name = attrs.get('table_name', None) or name
        primary_key = None
        mappings = dict()

        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
                if v.primary_key:
                    if primary_key:
                        raise KeyError('主键已存在')
                    primary_key = k
        if not primary_key:
            raise KeyError('没有创建主键')

        for k in mappings.keys():
            attrs.pop(k)

        attrs['table_name'] = table_name
        attrs['primary_key'] = primary_key
        attrs['mappings'] = mappings

        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):

    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        self[key] = value

    @classmethod
    def select_all(cls, **kwargs):
        ms = MySql()
        if kwargs:
            key = list(kwargs.keys())[0]
            value = kwargs[key]
            sql = 'select * from %s where %s = ?' % (cls.table_name, key)
            sql = sql.replace('?', '%s')
            res = ms.execute(sql, value)
        else:
            sql = 'select * from %s' % cls.table_name
            res = ms.execute(sql)
        return [cls(**re) for re in res]

    @classmethod
    def select_one(cls, **kwargs):
        ms = MySql()
        key = list(kwargs.keys())[0]
        value = kwargs[key]
        sql = 'select * from %s where %s = ?' % (cls.table_name, key)
        sql = sql.replace('?', '%s')
        res = ms.execute(sql, value)
        if res:
            return cls(**res[0])
        return None

    def update(self):
        ms = MySql()
        table_name = self.table_name

        pk = self.primary_key
        pk_value = getattr(self, pk, None)
        colum_key = []
        colum_value = []

        for k, v in self.mappings.items():
            if not v.primary_key:
                colum_key.append(k + "=?")
                colum_value.append(getattr(self, v.name, None))

        sql = "update %s set %s where %s = %s" % (table_name, ','.join(colum_key), pk, pk_value)
        sql = sql.replace('?', '%s')
        ms.execute(sql, colum_value)

    def save(self):
        ms = MySql()
        table_name = self.table_name

        colum_key = []
        colum_value = []
        colum_space = []
        for k, v in self.mappings.items():
            if not v.primary_key:
                colum_key.append(k)
                colum_space.append('?')
                colum_value.append(getattr(self, v.name, None))

        sql = "insert into %s(%s) values (%s)" % (table_name,','.join(colum_key),','.join(colum_space))
        sql = sql.replace('?','%s')
        ms.execute(sql, colum_value)
