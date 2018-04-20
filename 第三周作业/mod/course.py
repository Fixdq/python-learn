#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from lib import common as c

"""
课程类
"""


class Course:
    def __init__(self, name, period, price):
        """
        
        :param name: 名称 str
        :param period:周期  int
        :param price: 价格  int
        """
        self.name = name
        self.period = period
        self.price = price

    def show_info(self):
        """
        显示课程信息
        :return: 
        """
        print("课程信息：名字：{}，周期：{}个月，价格：{}".format(
            c.color(self.name),
            c.color(self.period),
            c.color(self.name)
        ))

