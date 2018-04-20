#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

#
# 4月16
# 	1、定义MySQL类（参考答案：http://www.cnblogs.com/linhaifeng/articles/7341177.html#_label5）
#
# 	　　1.对象有id、host、port三个属性
#
# 	　　2.定义工具create_id，在实例化时为每个对象随机生成id，保证id唯一
#
# 	　　3.提供两种实例化方式，方式一：用户传入host和port 方式二：从配置文件中读取host和port进行实例化
#
# 	　　4.为对象定制方法，save和get_obj_by_id，save能自动将对象序列化到文件中，文件路径为配置文件中DB_PATH,文件名为id号，保存之前验证对象是否已经存在，若存在则抛出异常，;get_obj_by_id方法用来从文件中反序列化出对象
#
import hashlib
import os
import pickle
import time
import setting


class Mysql:
    def __init__(self, host, port):
        self.id = self.create_id()
        self.host = host
        self.port = port

    def save(self):

        path = os.path.join(setting.DB_PATH, self.id)
        print(os.path.exists('/home/fixd/project/python_learn/day22/11ceb250dfa2dd74b055ec8cf42c6bd3'))
        print(os.path.isfile('/home/fixd/project/python_learn/day22/11ceb250dfa2dd74b055ec8cf42c6bd3'))
        # with open(path, 'wb') as f:
        #     pickle.dump(self, f)

    def get_obj_by_id(self):
        # path = os.path.join(setting.DB_PATH, self.id)
        # if not os.path.exists(path):
        #     raise IOError('')
        # with open(path, 'rb') as f:
        #     return pickle.load(f)
        pass
    @staticmethod
    def create_id():
        m = hashlib.md5()
        m.update(str(time.clock()).encode('utf-8'))
        return m.hexdigest()

    @classmethod
    def get_mysql(cls):
        return cls(setting.HOST, setting.PORT)

    def tell_info(self):
        print("""
        id:%s
        host:%s
        prot:%s
        """ % (
            self.id,
            self.host,
            self.port
        ))


mysql1 = Mysql('192.168.110.106', 80)
mysql2 = Mysql.get_mysql()
mysql1.tell_info()
mysql2.tell_info()

mysql1.save()
mysql = mysql1.get_obj_by_id()
mysql.tell_info()
# 2、定义一个类：圆形，该类有半径，周长，面积等属性，将半径隐藏起来，将周长与面积开放
# 		参考答案（http://www.cnblogs.com/linhaifeng/articles/7340801.html#_label4）
#
#

import math


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def perimeter(self):
        return 2 * math.pi * self.__radius

    @property
    def area(self):
        return math.pi * (self.__radius ** 2)


c1 = Circle(2)
print("""
面积：%s
周长：%s
""" % (
    c1.area,
    c1.perimeter
))


# 3、明日默写
# 		1、简述面向对象三大特性：继承、封装、多态
#      继承：一种新建类的方式，子类会继承父类的属性,减少代码冗余
#      封装：将类的属性进行隐藏，对外隐藏,对内开放，
#      多态：同一种事物的多种形态，通过基类创造统一的规则，强制子类遵循

# 		2、定义一个人的类，人有名字，身高，体重，用property讲体质参数封装成人的数据属性
class People:
    def __init__(self, name, height, weight):
        self.weight = weight
        self.height = height
        self.name = name

    @property
    def dmi(self):
        return self.weight / (self.height ** 2)

# 3、简述什么是绑定方法与非绑定方法，他们各自的特点是什么？
#       绑定方法绑定给谁，就把谁当做第一个参数传入（绑定到对象，绑定到类classmethod）
#       非绑定方法 staticmethod修饰的函数
#
#
#
# 	4、完善选课系统作业
