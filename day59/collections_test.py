#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-6-7 下午8:42
# @Author  : fixdq
# @File    : collections_test.py
# @Software: PyCharm


from collections import deque

def search(file,pattern,max_len=5):
    pre_lines =deque(maxlen=max_len)
    for line in file:
        if pattern in line:
            yield pre_lines,line
        pre_lines.append(line)


if __name__ == '__main__':
    with open("ces") as f:
        for pre_l,line in search(f,'Exchange'):
            print('-'*60)
            for i in pre_l:
                print(i)
            print('匹配行》》》》》',line)