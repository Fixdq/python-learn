#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : 03 线程的其他方法.py
# @Software: PyCharm
from threading import Thread,current_thread,enumerate

def task():
    print('oooo')
    current_thread().name

if __name__ == '__main__':
    t = Thread(target=task)

    t.start()


    print(current_thread().name)
    print(enumerate())
    print(t.getName())