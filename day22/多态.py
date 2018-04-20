#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
import abc


class Animal(mataclass=abc.ABCMeta):
    @abc.abstractmethod
    def bark(self):
        print('bark')


class Cat(Animal):
    def bark(self):
        print('cat is miao ')


cat = Cat()

cat.bark()
