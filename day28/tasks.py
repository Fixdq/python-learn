#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : tasks.py
# @Software: PyCharm
import os
import random
from multiprocessing import Process

import time


#
# def task(name):
#     print('%s is running ' % name)
#     time.sleep(1)
#     print('%s is end ' % name)
#
#
# if __name__ == '__main__':
#     p = Process(target=task, args=("Sha",))
#     p.start()
#     print("======>>>>>>")


#
#
# class MyProcess(Process):
#     def __init__(self, name):
#         super(MyProcess, self).__init__()
#         self.name = name
#
#
#     def run(self):
#         print('%s is running ' % self.name)
#         time.sleep(1)
#         print('%s is end ' % self.name)
#
#
# if __name__ == '__main__':
#     p = MyProcess('sha')
#     p.start()
#     print('==========+>>>>>>>>')


# s = 10
#
#
# def task():
#     global s
#     time.sleep(1)
#     s = 0
#     print('son is died')
#
#
# if __name__ == '__main__':
#     p = Process(target=task)
#     p.start()
#     time.sleep(2)
#     print(s)

#
# def task(n):
#     print('%s is died' % n)
#     time.sleep(random.randint(1,5))
#
#
# l = []
# for n in range(1, 4):
#     p = Process(target=task, args=(n,))
#     l.append(p)
#     p.start()
#
# for i in l:
#     i.join()
#


def task():
    print('%s--%s' % (os.getpid(), os.getppid()),os.getegid(),os.getuid(),os.getpgid(os.getpid()))


p = Process(target=task)
p.start()

print('%s--%s' % (os.getpid(), os.getppid()))
time.sleep(10)