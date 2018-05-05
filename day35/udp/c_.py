#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : c_.py
# @Software: PyCharm

import socketserver
from socket import *


c = socket(AF_INET,SOCK_DGRAM)


c.sendto(b'helolo',('127.0.0.1',8080))

res,addr = c.recvfrom(1024)

print(res,addr)