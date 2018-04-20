#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
"""
this is a test file
"""


class Person:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def say_hi():
        print('hi')

    def show_info(self):
        print(self.name)
        # print(self.__annotations__)
        print(self.__class__)
        # print(self.__delattr__())
        print('self.__dict__==>', self.__dict__)
        print('self.__doc__==>', self.__doc__)
        # print(self.__eq__())
        # print(self.__format__())
        print('self.__hash__==>', self.__hash__())
        print('self.__module__==>', self.__module__)
        print('self.__reduce__==>', self.__reduce__())
        print('self.__str__==>', self.__str__())
        print('self.__sizeof__==>', self.__sizeof__())
        # print('self.__slots__==>', self.__slots__())


person = Person('fixd')
person.show_info()
