#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : fuckorm.py
# @Software: PyCharm

from day43.test1.mysql import *


class Field(object):
    def __init__(self, name, colum_type, primary_key, default):
        self.name = name
        self.colum_type = colum_type
        self.primary_key = primary_key
        self.default = default


class StringField(Field):
    def __init__(self, name, colum_type="varchar(200)", primary_key=False, default=None):
        super().__init__(name, colum_type, primary_key, default)


class IntergerField(Field):
    def __init__(self, name, colum_type="int", primary_key=False, default=0):
        super().__init__(name, colum_type, primary_key, default)


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
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
                        raise KeyError('主键重复')
                    primary_key = k

        if not primary_key:
            raise KeyError('没有主键')

        for k in mapping.keys():
            attrs.pop(k)

        attrs['table_name'] = table_name
        attrs['primary_key'] = primary_key
        attrs['mapping'] = mapping

        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):

    def __getattr__(self, item):
        try:
            return self[item]
        except Exception as e:
            raise e.args

    def __setattr__(self, key, value):
        self[key] = value

    @classmethod
    def select_all(cls, **kwargs):
        ms = MySql()
        if kwargs:
            key = list(kwargs.keys())[0]
            value = kwargs[0]
            sql = "select * from %s WHERE %s = ?" % (cls.table_name, key)
            sql = sql.replace('?', '%s')

            res = ms.select(sql, value)

        else:
            sql = "select * from %s " % cls.table_name
            res = ms.select(sql)

        return [cls(**re) for re in res]

    @classmethod
    def select_one(cls, **kwargs):
        ms = MySql()
        key = list(kwargs.keys())[0]
        value = kwargs[key]
        sql = "select * from %s WHERE %s = ?" % (cls.table_name, key)
        sql = sql.replace('?', '%s')
        res = ms.select(sql, value)

        if not res:
            return None
        else:
            return cls(**res[0])

    def update(self):
        ms = MySql()
        table_name = self.table_name
        mapping = self.mapping
        pk = self.primary_key

        colum_names = []
        colum_values = []
        pk_v = None
        for k, v in mapping.items():
            if v.primary_key:
                pk_v = getattr(self, v.name, None)
            if not v.primary_key:
                colum_names.append(v.name + '=?')

                colum_values.append(getattr(self, v.name, v.default))

        sql = "update %s set %s where %s = %s" % (table_name, ','.join(colum_names), pk, pk_v)
        sql = sql.replace('?', '%s')
        ms.execute(sql, colum_values)

    def save(self):
        ms = MySql()
        table_name = self.table_name
        mapping = self.mapping

        colum_names = []
        colum_values = []
        replaces = []
        for k, v in mapping.items():
            if not v.primary_key:
                colum_names.append(v.name)
                replaces.append('?')
                colum_values.append(getattr(self, v.name, None))

        sql = "insert into %s(%s) values (%s)" % (table_name, ','.join(colum_names), ','.join(replaces))
        sql = sql.replace('?', '%s')
        ms.execute(sql, colum_values)


class User(Model):
    table_name = 'user'

    id = IntergerField('id', primary_key=True)
    name = StringField('name', )
    balance = IntergerField('balance', default=0)


if __name__ == '__main__':
    user = User()
    u = user.select_one(id=1)
    print(u)
    u.name = 'dd'
    u.balance='200'
    u.update()

    u1 = User(name = 'ff',balance = 2000)
    u1.save()

