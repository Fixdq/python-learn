# !/usr/bin/env python3
# encoding: utf-8
# by fixdq

class Foo:
    __shool = 'ttttt'

    def __init__(self, name):
        self._Foo_name = name
        self.__name = name

    def get_name(self):
        return self.__name

    @property
    def Foo_name(self):
        return self._Foo_name


foo = Foo('ggg')
print(foo.get_name())
print(foo.Foo_name)
