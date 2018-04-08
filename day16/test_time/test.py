#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
# import time
#
#
# print(time.time())
# print(time.strftime("%Y"))
# print(time.localtime())
# print(time.gmtime())

import random

# 生成随机验证码（大小写字母，数字）
def make_code(n):
    code = ''
    for i in range(n):
        s1 = str(random.randint(0, 9))
        s2 = chr(random.randint(65, 90))
        s3 = chr(random.randint(97, 122))
        s4 = random.choice([s2, s3])
        code += random.choice([s1, s4])
    return code

if __name__ == '__main__':
    print(make_code(10))