#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : 01 守护进程应用场景.py
# @Software: PyCharm

import time
from multiprocessing import Process, JoinableQueue


def consumer(name, q):
    while True:
        res = q.get()
        time.sleep(0.2)
        print('\033[46m消费者===》%s 吃了 %s\033[0m' % (name, res))
        q.task_done()


def producer(name, q, food):
    for i in range(5):
        time.sleep(0.5)
        res = '%s%s' % (food, i)
        q.put(res)
        print('\033[45m生产者者===》%s 生产了 %s\033[0m' % (name, res))


if __name__ == '__main__':
    # 1、共享的盆
    q = JoinableQueue()

    # 2、生产者们
    p1 = Process(target=producer, args=('egon', q, '包子'))
    p2 = Process(target=producer, args=('刘清政', q, '泔水'))
    p3 = Process(target=producer, args=('杨军', q, '米饭'))

    # 3、消费者们
    c1 = Process(target=consumer, args=('alex', q))
    c2 = Process(target=consumer, args=('梁书东', q))
    c1.daemon = True
    c2.daemon = True

    p1.start()
    p2.start()
    p3.start()

    c1.start()
    c2.start()


    # 确定生产者确确实实已经生产完毕
    p1.join()
    p2.join()
    p3.join()
    # 在生产者生产完毕后，拿到队列中元素的总个数，然后直到元素总数变为0，q.join()这一行代码才算运行完毕
    q.join()
    #q.join()一旦结束就意味着队列确实被取空，消费者已经确确实实把数据都取干净了
    print('主进程结束')
