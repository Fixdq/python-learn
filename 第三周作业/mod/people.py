#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


class People:
    """
    student teacher 抽象父类
    """
    def __init__(self, name=None, age=None, gender=None):
        """
        
        :param name: 
        :param age: 
        :param gender: 
        """
        self.name = name
        self.age = age
        self.gender = gender