#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-20 下午2:19
# @Author  : fixdq
# @Site    : 
# @File    : fixdqorm.py
# @Software: PyCharm

from server.orm01.mysql import MySql


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
        if name == "Model":
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

        for k in mapping.keys():
            attrs.pop(k)

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
        except KeyError:
            raise AttributeError('%s 属性不存在' % item)

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
            sql = 'select * from %s ' % cls.table_name
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
                vs.append(getattr(self, v.name, v.default))
                ss.append('?')

        sql = 'insert into %s (%s) value (%s)' % (self.table_name, ','.join(ks), ','.join(ss))
        sql = sql.replace('?', '%s')
        ms.execute(sql, vs)

    def update(self):
        ms = MySql()

        ks = []
        vs = []

        for k, v in self.mapping.items():
            if v.primary_key:
                pk_v = getattr(self, v.name, v.default)
            else:
                ks.append(v.name + '=?')
                vs.append(getattr(self, v.name, v.default))

        sql = 'update %s set %s where %s = %s' % (self.table_name, ','.join(ks), self.primary_key, pk_v)
        sql = sql.replace('?', '%s')
        ms.execute(sql, vs)


class User(Model):
    table_name = 'userinfo'
    id = IntergerField('id', primary_key=True)
    name = StringField('name')
    password = StringField('password')
    is_vip = IntergerField('is_vip', default=0)
    locked = IntergerField('locked', default=0)
    user_type = StringField('user_type')


if __name__ == '__main__':
    # user = User().select_one(id= 9)
    # user.locked = 1
    # user.update()
    # print(user.select_many(id = 9))
    # print(user.select_one(id = 9))

    user = User(name='fffffdfsdff',
                password='asdfasdfa',
                user_type='user_type')

    user.save()
