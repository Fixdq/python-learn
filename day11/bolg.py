# encoding: utf-8
# by fixdq
#
# import test_time
# # 计算每个函数执行的时间
# def warpper(func):
#     def inner(*args,**kwargs):
#         # 函数开始的时间点
#         start_time = test_time.test_time()
#         res = func(*args,**kwargs)    # 原函数有返回值
#         # 函数结束的时间点
#         end_time = test_time.test_time()
#         # 显示执行时间
#         total = start_time - end_time  # 单位秒
#         print(total)
#         return res #返回值
#     return inner
#
# # 语法糖
# @warpper
# def run(name):
#     test_time.sleep(1)
#     print('%s刚才在跑步' % name)
#     return '跑步结束'
#
# res = run('fixd')
# print(res)
#
# #无参装饰器模板
# def wrapper(func):
#     def inner(*args,**kwargs):
#         res=func(*args,**kwargs)
#         return res
#     return inner


# def run():
#         test_time.sleep(1)
#         print('刚才在跑步')
#
# # 函数开始的时间点
# start_time = test_time.test_time()
# # 调用
# run()
# # 函数结束的时间点
# end_time = test_time.test_time()
# # 显示执行时间
#  # 单位秒
# print(end_time - start_time)


# def run():
#         test_time.sleep(1)
#         print('刚才在跑步')
#
# def timer(func):
#     start_time = test_time.test_time()
#     func()
#     # 函数结束的时间点
#     end_time = test_time.test_time()
#     # 显示执行时间
#     total = end_time - end_time  # 单位秒
#     print(end_time - start_time)
# # 调用
# timer(run)
#
# # 闭包函数
# def wrapper(func):
#     def inner():
#         func()    # 原函数
#     return inner
# run = wrapper(run)
#
# run()
#
#
#
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         pass
#     return wrapper
#
# def db_link():
#     print('默认数据库连接')
#

import functools


def log(k=''):  # 这里参数定义的是一个默认参数，如果没有传入参数，默认为空，可以换成其他类型的参数
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('start')
            print('{}:{}'.format(k, func.__name__))  # 这里使用了装饰器的参数k
            r = func(*args, **kwargs)
            print('end')
            return r

        return wrapper
    return decorator


@log()  # fun1=log()(fun1) 装饰器没有使用参数
def fun1(a):
    print(a + 10)


fun1(10)


# print(fun1.__name__)        # 上面装饰器如果没有@functools.wraps(func)一句的话，这里打印出的函数名为wrapper

@log('excute')  # fun2=log('excute')(fun2) 装饰器使用给定参数
def fun2(a):
    print(a + 20)

fun2(10)