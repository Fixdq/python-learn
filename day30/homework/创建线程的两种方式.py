#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : 创建线程的两种方式.py
# @Software: PyCharm

# 什么是线程
# 线程指的是一条流水线的工作过程

#
# 第一种开启线程的方式

# from threading import Thread,current_thread
# import time
#
# def task():
#     print(current_thread().name)
#
#
# if __name__ == '__main__':
#
#     for i in range(10):
#         t = Thread(target=task,name='%s' % i)
#         t.start()

# 第二种开启方式
# import os
# from threading import Thread, current_thread
#
#
# class MyThread(Thread):
#     def run(self):
#         print(self.name)
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = MyThread()
#         t.start()
#

# 线程的其他方法
# import os
# from threading import Thread, current_thread,enumerate
#
# import time
#
#
# class MyThread(Thread):
#     def run(self):
#         print('child-->',os.getppid())
#         print('child-->',os.getpid())
#         print('child-->',enumerate())
#         time.sleep(5)
# if __name__ == '__main__':
#         t = MyThread()
#         t.start()
#         print('main-->', os.getppid())
#         print('mian-->', os.getpid())
#         print('mian-->',enumerate())

# 子线的 pid  和 主线程的 pid  是相同的
# enumerate()  返回当前活着的所有线程对象的列表。


# 　互斥锁　

from threading import Thread, current_thread, enumerate, Lock

import time

mutex = Lock()
x = 10


class MyThread(Thread):
    def run(self):
        global x
        mutex.acquire()
        temp = x
        time.sleep(0.2)
        print(self.name)
        x = temp - 1
        mutex.release()


if __name__ == '__main__':
    tl = []
    for thread in range(10):
        t = MyThread()
        tl.append(t)
        t.start()
    for t in tl:
        t.join()

    print('mian')
    print(x)
