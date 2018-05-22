#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-22 上午11:03
# @Author  : fixdq
# @File    : mysql.py
# @Software: PyCharm


from orm.mysql import MySql
from db.models import *

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
            return super().__new__(cls, name, bases, attrs)

        table_name = attrs['table_name'] or name
        primary_key = None
        mapping = dict()

        for k, v in attrs.items():
            if isinstance(v, Field):
                mapping[k] = v
                if v.primary_key:
                    if primary_key:
                        raise AttributeError('主键重复')
                    primary_key = k

        if not primary_key:
            raise AttributeError('主键不存在')

        for key in mapping.keys():
            attrs.pop(key)

        attrs['table_name'] = table_name
        attrs['primary_key'] = primary_key
        attrs['mapping'] = mapping

        return super().__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError as e:
            raise e

    def __setattr__(self, key, value):
        self[key] = value

    @classmethod
    def select_many(cls, **kwargs):
        ms = MySql()
        if kwargs:
            k = list(kwargs.keys())[0]
            v = kwargs[k]

            sql = 'select * from %s where %s = ?' % (cls.table_name, k)
            sql = sql.replace('?', '%s')

            res = ms.select(sql, v)
        else:

            sql = 'select * from %s' % cls.table_name
            res = ms.select(sql)

        return [cls(**re) for re in res]

    @classmethod
    def select_one(cls, **kwargs):
        ms = MySql()

        k = list(kwargs.keys())[0]
        v = kwargs[k]

        sql = 'select * from %s where %s = ?' % (cls.table_name, k)
        sql = sql.replace('?', '%s')

        res = ms.select(sql, v)
        if res:
            return cls(**res[0])
        else:
            return None

    def save(self):
        ms = MySql()
        ks = []
        vs = []
        ss = []
        for k, v in self.mapping.items():
            if not v.primary_key:
                ks.append(v.name)
                vs.append(getattr(self, v.name))
                ss.append('?')
        sql = 'insert into %s (%s) value (%s)' % (self.table_name, ','.join(ks), ','.join(ss))
        sql = sql.replace('?', '%s')
        ms.execute(sql, vs)

    def update(self):
        ms = MySql()
        table_name = self.table_name
        pk = self.primary_key

        ks = []
        vs = []
        for k, v in self.mapping.items():
            if v.primary_key:
                pk_v = getattr(self, v.name)
            else:
                ks.append(v.name+'=?')
                vs.append(getattr(self, v.name))
        sql = 'update %s set %s where %s =%s' % (table_name, ','.join(ks), pk,pk_v)
        sql = sql.replace('?', '%s')
        ms.execute(sql, vs)


if __name__ == '__main__':
    res = Record.select_one(id = 13)
    print(res)
    res.user_id = 1000
    res.update()
    # res = Record()
    # res.user_id = 55
    # res.movie_id = 66
    # res.save()