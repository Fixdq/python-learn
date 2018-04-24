#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : test.py
# @Software: PyCharm

from multiprocessing import Process
import time, os


def run():
    print('子', os.getpid())


if __name__ == '__main__':
    p = Process(target=run)
    p.start()

    print('主', os.getpid())
    time.sleep(1000)