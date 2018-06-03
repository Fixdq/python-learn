#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-6-2 上午10:43
# @Author  : fixdq
# @File    : request_test.py
# @Software: PyCharm


import requests
import json

url = "https://192.168.1.1"

res = requests.get(url)

dic = json.loads(res)
print(list(dic))
