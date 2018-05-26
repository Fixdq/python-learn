#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-25 下午8:24
# @Author  : fixdq
# @File    : start.py
# @Software: PyCharm

from socket import *
from conf import settings


def get_client():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect_ex(settings.ip_port)
    return client