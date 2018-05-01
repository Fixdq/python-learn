#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : 04 互斥锁.py
# @Software: PyCharm

from threading import Thread, Lock

import time

mutex = Lock()
x = 100


def task():
    global x
    mutex.acquire()
    temp = x
    time.sleep(0.01)
    x = temp - 1
    mutex.release()


if __name__ == '__main__':
    start = time.time()
    t_l = []
    for i in range(100):
        t = Thread(target=task)
        t_l.append(t)
        t.start()
    for tt in t_l:
        tt.join()
    print(x)
    print('end')
    print(time.time()-start)
