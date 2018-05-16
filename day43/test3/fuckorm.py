#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : fuckorm.py
# @Software: PyCharm

from day43.test3.mysql import *


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
    def __init__(self, name, colum_type='int', primary_key=False, default=0):
        super().__init__(name, colum_type, primary_key, default)


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)
        table_name = attrs['table_name'] or name
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
            raise KeyError('主键不存在')
        for k in mappings.keys():
            attrs.pop(k)

        attrs['table_name'] = table_name
        attrs['primary_key'] = primary_key
        attrs['mappings'] = mappings
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):

    def __getattr__(self, item):
        try:
            return self[item]
        except Exception:
            raise KeyError('key 不存在')

    def __setattr__(self, key, value):

        self[key] = value

    @classmethod
    def select_all(cls, **kwargs):
        ms = MySql()
        if kwargs:
            key = list(kwargs.keys())[0]
            values = kwargs[key]
            sql = "select * from %s where %s =?" % (cls.table_name, key)
            sql = sql.replace('?', '%s')
            res = ms.select(sql, values)
        else:
            sql = "select * from %s" % cls.table_name
            res = ms.select(sql)

        return [cls(**re) for re in res]

    @classmethod
    def select_one(cls, **kwargs):
        ms = MySql()
        key = list(kwargs.keys())[0]
        values = kwargs[key]
        sql = "select * from %s where %s =?" % (cls.table_name, key)
        sql = sql.replace('?', '%s')
        res = ms.select(sql, values)
        if res:
            return cls(**res[0])
        else:
            return None

    def update(self):
        ms = MySql()
        pk = self.primary_key
        colum_keys = []
        colum_value = []
        for k, v in self.mappings.items():
            if v.primary_key:
                pk_v = getattr(self, v.name, None)
            if not v.primary_key:
                colum_keys.append(k+'=?')
                colum_value.append(getattr(self,v.name,None))

        sql = 'update %s set %s where %s = %s' % (self.table_name,','.join(colum_keys),pk,pk_v)
        sql = sql.replace('?','%s')
        ms.execute(sql,colum_value)

    def save(self):
        ms = MySql()
        colum_keys = []
        colum_value = []
        colum_space = []
        for k, v in self.mappings.items():
            if not v.primary_key:
                colum_keys.append(k)
                colum_space.append('?')
                colum_value.append(getattr(self, v.name, None))
        sql = 'insert into %s(%s) values (%s)' % (self.table_name,','.join(colum_keys),','.join(colum_space))
        sql = sql.replace('?', '%s')
        ms.execute(sql, colum_value)




class User(Model):

    table_name = 'user'
    id = IntergerField('id',primary_key=True)
    name = StringField('name')
    balance = IntergerField('balance')

if __name__ == '__main__':
    u = User()
    # res = u.select_all()select_all
    # print(res)
    one = u.select_one(id='1')
    print(one)
    one.name='999999999'
    one.update()
    # user = User(name='lllllllll',balance = 20000)
    # user.save()
    #