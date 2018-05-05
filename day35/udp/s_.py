#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : s_.py
# @Software: PyCharm

from socket import *


s = socket(AF_INET,SOCK_DGRAM)
s.bind(('127.0.0.1',8080))

res,addr = s.recvfrom(1024)
print(res,addr)
s.sendto(res.upper(),addr)