#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


class People:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def tell_info(self):
        print('name:%s,,age:%s' % (self.name, self.age))

    @classmethod
    def get_obj(cls):
        return cls('是是是', 10000)


tm = People.get_obj()

tm.tell_info()