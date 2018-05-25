#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-24 下午9:02
# @Author  : fixdq
# @File    : fuckorm.py
# @Software: PyCharm
from day49.orm import mysql


class Field:
    def __init__(self, name, colum_type, primary_key, default):
        self.name = name
        self.colum_type = colum_type
        self.primary_key = primary_key
        self.default = default


class StringFidel(Field):
    def __init__(self, name, colum_type='varchar(200)', primary_key=False, default=None):
        super().__init__(name, colum_type, primary_key, default)


class IntergerFidel(Field):
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
                        raise ValueError('主键错误')
                    primary_key = k

        if not primary_key:
            raise ValueError('主键不存在')

        for k in mapping.keys():
            attrs.pop(k)

        attrs['table_name'] = table_name
        attrs['primary_key'] = primary_key
        attrs['mapping'] = mapping

        return super().__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError

    @classmethod
    def select_many(cls, **kwargs):
        ms = mysql.MySql()
        if kwargs:
            k = list(kwargs.keys())[0]
            v = kwargs[k]

            sql = 'select * from %s where %s =?' % (cls.table_name, k)
            sql = sql.replace('?', '%s')
            res = ms.select(sql, v)
        else:
            sql = 'select * from %s' % cls.table_name
            res = ms.select(sql)

        return [cls(**re) for re in res]

    @classmethod
    def select_one(cls, **kwargs):
        ms = mysql.MySql()

        k = list(kwargs.keys())[0]
        v = kwargs[k]

        sql = 'select * from %s where %s =?' % (cls.table_name, k)
        sql = sql.replace('?', '%s')
        res = ms.select(sql, v)
        if res:
            return cls(**res[0])
        else:
            return None

    def save(self):
        ms = mysql.MySql()

        ks = []
        vs = []
        ss = []

        for k, v in self.mapping.items():
            if not v.primary_key:
                ks.append(v.name)
                vs.append(getattr(self, v.name, v.default))
                ss.append('?')

        sql = 'insert into %s (%s) value (%s)' % (
            self.table_name, ','.join(ks), ','.join(ss))
        sql = sql.replace('?', '%s')
        ms.execute(sql, vs),

    def update(self):
        ms = mysql.MySql()

        ks = []
        vs = []

        for k, v in self.mapping.items():
            if v.primary_key:
                pk_v = getattr(self, v.name)
            if not v.primary_key:
                ks.append(v.name + '=?')
                vs.append(getattr(self, v.name, v.default))

        # sql = 'insert into %s (%s) value (%s) where %s = %s' % (
        # self.table_name, ','.join(ks), ','.join(ss), self.primary_key, pk_v)
        sql = 'update %s set %s where %s = %s ' % (self.table_name, ','.join(ks), self.primary_key, pk_v)
        sql = sql.replace('?', '%s')
        ms.execute(sql, vs)


class Record(Model):
    table_name = 'download_record'
    id = IntergerFidel('id', primary_key=True)
    user_id = IntergerFidel('user_id')
    movie_id = IntergerFidel('movie_id')


if __name__ == '__main__':
    # res = Record.select_one(user_id = 26)
    # res.user_id = 100
    # res.update()
    # print(res)

    user = Record(user_id=555, movie=6666)
    user.save()
