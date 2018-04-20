#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

"""
数据处理类
"""
import os
import pickle


class DbHandler:
    def __init__(self, db_path):
        self.db_path = db_path

    def load_data(self, file_name):
        """
        读取数据
        :param file_name: 
        :return: 
        """

        path = os.path.join(self.db_path, file_name)
        with open(path, 'rb') as f:
            return pickle.load(f)

    def dump_data(self, data,file_name):
        """
        写入数据
        :param file_name: 
        :param data: 
        :return: 
        """

        path = os.path.join(self.db_path, file_name)
        with open(path, 'wb') as f:
            return pickle.dump(data, f)

