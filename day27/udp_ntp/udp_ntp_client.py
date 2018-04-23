#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : udp_ntp_server.py
# @Software: PyCharm

from socket import *

ip_port = ('127.122.114.14', 8080)
ntp_client = socket(AF_INET, SOCK_DGRAM)

ntp_client.sendto('ntp'.encode('utf-8'), ip_port)
time, addr = ntp_client.recvfrom(1024)

print(time.decode('utf-8'))
