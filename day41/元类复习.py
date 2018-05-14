#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : 元类复习.py
# @Software: PyCharm


class MyMetaClass(type):
    def __init__(self, class_name, class_bases, class_dic):
        # print('metaclass init is run')
        super(MyMetaClass, self).__init__(class_name, class_bases, class_dic)

    def __call__(self, *args, **kwargs):
        print(self, *args, **kwargs)
        # 创建一个空对象
        obj = object.__new__(self)
        self.__init__(obj, *args, **kwargs)
        return obj

    # def __new__(cls, *args, **kwargs):
    #     obj = object.__new__(cls)
    #     print('metaclass __new__ is run ')
    #     cls.__init__(obj, *args, **kwargs)
    #     return obj


# class TestClass(object, metaclass=MyMetaClass):
class TestClass(object):

    def __new__(cls, *args, **kwargs):
        print('TestClass __new__ is run ')
        return super(TestClass, cls).__new__(cls)

    def __init__(self, name, age):
        print('TestClass init is run')
        self.name = name
        self.age = age

    def say(self):
        print(self.name, self.age)
    #
    # def __new__(cls, *args, **kwargs):
    #     obj = object.__new__(cls)
    #     print('TestClass __new__ is run ')
    #     cls.__init__(obj, *args, **kwargs)
    #     return obj


if __name__ == '__main__':
    t = TestClass('fixd', 20)


# t.say()


# __call__ 的使用
class People(object, metaclass=type):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print(self, *args, **kwargs)

# obj = People('fixd', 8)

# obj(1,2,3)
