#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : 05 死锁现象递归锁.py
# @Software: PyCharm

from threading import Thread,RLock
import time
mutexA = mutexB = RLock()


class MyThread(Thread):

    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print('%s 拿到了A锁' %self.name)

        mutexB.acquire()
        print('%s 拿到了B锁' %self.name)
        mutexB.release()

        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print('%s 拿到了B锁' %self.name)
        time.sleep(0.1)

        mutexA.acquire()
        print('%s 拿到了A锁' %self.name)
        mutexA.release()

        mutexB.release()

if __name__ == '__main__':
    for t in range(10):
        t = MyThread()
        t.start()