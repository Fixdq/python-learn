#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : 02 event.py
# @Software: PyCharm
import requests
requests.get()

from threading import Thread, Event, current_thread

import time

event = Event()

def t1():
    print('开始检测%s' % current_thread().name)
    time.sleep(4)
    event.set()


def t2():
    print('等待连接%s' % current_thread().name)
    event.wait()
    print('开始连接了')


if __name__ == '__main__':
    t1 = Thread(target=t2)
    t2 = Thread(target=t2)
    t3 = Thread(target=t2)
