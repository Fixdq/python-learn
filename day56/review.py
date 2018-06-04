#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-6-4 下午7:09
# @Author  : fixdq
# @File    : review.py
# @Software: PyCharm
import functools

# 装饰器的基本格式
import time


def outer(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return wrapper


# 计算每个函数执行的时间

def wrapper(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        total = end_time - start_time
        print(total)

    return inner


# 需要被装饰的函数
@wrapper
def run():
    # 模拟函数的执行时间
    time.sleep(1)


# 调用函数
run()


# 进阶版 修饰有参数的函数
def wrapper(func):
    def inner(*args, **kwargs):  # 在内函数加上通用形参
        start_time = time.time()
        func(*args, **kwargs)  # 将通用形参传递给被修饰函数
        end_time = time.time()
        total = end_time - start_time
        print(total)

    return inner


# 进阶版 修饰有返回值的函数
def wrapper(func):
    def inner(*args, **kwargs):  # 在内函数加上通用形参
        start_time = time.time()
        res = func(*args, **kwargs)  # 将通用形参传递给被修饰函数，接收被装饰函数的返回值
        end_time = time.time()
        total = end_time - start_time
        print(total)
        return res  # 将返回值 返回

    return inner


# 进阶版 装饰器带参数
def decoration_runtime(tp=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            total = end_time - start_time
            print(total, tp)  # 在函数内处理装饰器传入的参数
            return res

        return inner

    return wrapper


# 修复装饰器
# 为什么需要修复装饰器
# 使得包裹函数inner 在调用__name__ ，__module__和 __doc__属性 与被装饰的函数 完全相同
# 方法
# improt functools
# 在装饰器最内层函数 添加修饰@functools.wraps(func)
def decoration_runtime(tp=None):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            total = end_time - start_time
            print(total, tp)  # 在函数内处理装饰器传入的参数
            return res

        return inner

    return wrapper
