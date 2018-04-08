#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
"""
终端 打印进度条
"""
import time


def progress(percent, width=100):
    if percent > 1:
        percent = 1
    show_str = ('[%%-%ds]' % width) % (int(width * percent) * '#')
    print('\r%s %d%%' % (show_str, int(100 * percent)), end='')


recv_size = 0
total_size = 100
while recv_size < total_size:
    time.sleep(0.01)
    recv_size += 1
    percent = recv_size / total_size
    progress(percent)
