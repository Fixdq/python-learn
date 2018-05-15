#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : fuckorm.py
# @Software: PyCharm

from day42 import MySql


class Field:
    """
    此类对应--->表结构一个字段的属性
    基类
    """

    def __init__(self, name, cloum_type, primary_key, default):
        self.name = name
        self.cloum_type = cloum_type
        self.primary_key = primary_key
        self.default = default


class StringField(Field):
    """
    字符类型
    """

    def __init__(self, name, cloum_type='varchar(200)', primary_key=False, default=None):
        super().__init__(name, cloum_type, primary_key, default)


class IntergerField(Field):
    """
    数字类型
    """

    def __init__(self, name, cloum_type='int', primary_key=False, default=0):
        super().__init__(name, cloum_type, primary_key, default)


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':  # Model 类  不拦截创建
            return type.__new__(cls, name, bases, attrs)

        table = attrs.get('table', None)  # 从对象中获取 对应表的名称
        if not table:
            table = name  # 如果表名不存在，将类名作为表名
        primary_key = None  # 表的主键
        mappings = dict()  # 表的字段属性

        for k, v in attrs.items():  # 循环判断属性
            if isinstance(v, Field):  # 字段属性 继续执行   其他 忽略
                mappings[k] = v  # 将 信息放入mapping中
                if v.primary_key:  # 判断当前列是否是主键
                    if primary_key:  # 重复主键报错
                        raise TypeError('主键重复%s' % k)
                    primary_key = k  # 设置主键

        for k in mappings.keys():  #
            attrs.pop(k)

        if not primary_key:
            raise TypeError('没有设置主键')

        attrs['table'] = table
        attrs['primary_key'] = primary_key
        attrs['mappings'] = mappings

        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
        """
        dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)
        :param kwargs:
        """
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        """
        .访问属性的时候触发
        :param key:
        :return:
        """
        try:
            return key
        except KeyError:
            raise AttributeError('没有属性%s' % key)

    def __setattr__(self, key, value):
        '''
        赋值的时候触发
        :param key:
        :param value:
        :return:
        '''
        self[key] = value

    @classmethod
    def select_all(cls, **kwargs):
        mysql = MySql.MySql().singleton()
        if kwargs:
            # 有参数传入  根据参数查询
            key = list(kwargs.keys())[0]

            value = kwargs[key]
            sql = "select * from %s where %s = ?" % (cls.table, key)
            sql = sql.replace('?', '%s')
            res = mysql.select(sql, value)
        else:
            # 没有参数传入  查询全部
            sql = "select * from %s" % cls.table
            res = mysql.select(sql)

        # 查询出来的结果 [{k,v},{k,v}]
        #
        return [cls(**r) for r in res]

    @classmethod
    def select_one(cls, **kwargs):
        mysql = MySql.MySql().singleton()
        key = list(kwargs.keys())[0]
        value = kwargs[key]
        sql = "select * from %s where %s = ?" % (cls.table, key)
        sql = sql.replace('?', '%s')
        res = mysql.select(sql, value)
        if res:
            return cls(**res[0])
        else:
            return None


class User(Model):
    table = 'user'

    id = IntergerField('id', primary_key=True)
    name = StringField('name', )
    balance = IntergerField('balance', default=0)


if __name__ == '__main__':
    user = User()
    # res = user.select_all(id=1,)
    res = user.select_one(id=1)
    print(res)
