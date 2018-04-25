#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : blog.py
# @Software: PyCharm

# from multiprocessing import Process
#
# import time
#
#
# def pro():
#     for i in range(100):
#         print(i,'------------')
#         time.sleep(1)
#
#
# p = Process(target=pro,)
# p.daemon = True
# p.start()
# time.sleep(5)
# p.terminate()
# time.sleep(2)
# print('main')
import json
from multiprocessing import Process, Lock
import time


def search():
    dic = json.load(open('db.txt'))
    print('\033[32m剩余票数%s\033[32m' % dic['count'])


def get():
    dic = json.load(open('db.txt'))
    time.sleep(0.02)  # 模拟读数据的网络延迟
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(0.05)  # 模拟写数据的网络延迟
        json.dump(dic, open('db.txt', 'w'))
        print('\033[32m购票成功\033[32m')


def task(lock):
    search()
    lock.acquire()
    get()
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(10):  # 模拟并发100个客户端抢票
        p = Process(target=task, args=(lock,))
        p.start()
