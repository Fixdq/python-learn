#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


# class Po:
#     def __init__(self, name):
#         self.name = name
#
#     def say(self):
#         print('hello world!')
#
#     def __call__(self, *args, **kwargs):
#         print("__call__", args, kwargs)
#
#
# local_dic = {}
# to = type('TO', (object,), local_dic)
#
# p = Po('name')
# p(1, 3, 3, 4, 5, 5, 6, 6, s=9, f=123, r=78)
#
# class MyMetaClass(type):
#     def __init__(self, class_name, class_bases, class_dic):
#         if not class_name.istitle():
#             raise TypeError('类名必须首字母大写')
#         if not class_dic.get('__doc__'):
#             raise TypeError('类中必须写文档注释')
#         super(MyMetaClass, self).__init__(class_name, class_bases, class_dic)
#
#     def __call__(self, *args, **kwargs):
#         pass
#
#
# class Student(metaclass=MyMetaClass):
#     """
#     3
#     2
#     """
#
#     def __init__(self, name):
#         self.name = name
#
#     def say(self):
#         print('hello')

#
# # 需要执行的字符串代码
# str="""
# x=1
# y=1
# z=x+y
# """
# glo_dic = {}    #执行期间的全局名称空间
# local_dic = {}  #执行期间的局部名称空间
# exec(str,glo_dic,local_dic)
# print(glo_dic)
# print(local_dic)    #{'x': 1, 'y': 1, 'z': 2}
#
#
#
# # ------------------------------------------------------
# class Foo:
#     pass
#
# f1 = Foo()
#
# print(type(f1))
# print(type(Foo))
#
# # ------------------------------------------------------

# # 创建类的两种方式
# class Chinese(object, metaclass=type):
#     country = 'china'
#
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
#     def tell(self):
#         print('%s is speking' % self.name)
#
#
# # 类名
# class_name = 'Chinese'
# # 类的父类
# class_bases = (object,)
# # 类体
# class_body = """
# country = 'china'
# def __init__(self, name, age):
#     self.age = age
#     self.name = name
#
# def tell(self):
#     print('%s is speking' % self.name)
#
# """
#
# class_dic = {}
# exec(class_body, {}, class_dic)
# print(class_dic)
#
# Foo = type(class_name, class_bases, class_dic)
#
# print(Foo)
# print(type(Foo))
# print(isinstance(Foo, type))

# ----------------------------------------------------

# 产生新对象

obj = object.__new__(object)


class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        # if '__doc__' not in class_dic or not class_dic.get('__doc__').strip():
        #     raise TypeError('类中必须写上文档注释')
        print('Mymeta.__init__')
        super(Mymeta, self).__init__(class_name, class_bases, class_dic)

    def __call__(self, *args, **kwargs):
        print('Mymeta.__call__')
        obj = object.__new__(self)

        self.__init__(obj, *args, **kwargs)

        return obj


# class_name = 'People'
# class_bases = (object,)
# class_dic = {}
# People = Mymeta(class_name, class_bases, class_dic)
class People(object, metaclass=Mymeta):
    """
    doc
    """

    def __init__(self):
        print('People.__init__')
        super(People, self)

    def __call__(self, *args, **kwargs):
        print('People.__call__')


People()
