#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : udp_ntp_server.py
# @Software: PyCharm

from socket import *

import time

ip_port = ('127.122.114.14', 8080)
ntp_server = socket(AF_INET, SOCK_DGRAM)
ntp_server.bind(ip_port)

while True:
    res, addr = ntp_server.recvfrom(1024)
    if 'ntp' == res.decode('utf-8'):
        ntp_server.sendto(str(time.time()).encode('utf-8'), addr)
