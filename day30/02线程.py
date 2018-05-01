#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : 02线程.py
# @Software: PyCharm

from threading import Thread


# def task(name):
#
#     print("%s" % (name,))
#
#
# if __name__ == '__main__':
#
#     t = Thread(target=task,args=('fff',))
#     t.start()
#     print('主')


class MyThread(Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        print("%s" % (self.name,))


t = MyThread('lllll')
t.start()
