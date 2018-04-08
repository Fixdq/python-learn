#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
import random


def random_code(len):
    code = ''
    for i in range(len):
        s1 = str(random.randint(0, 9))
        s2 = chr(random.randint(65, 90))
        code += random.choice([s1, s2])
    return code

print(random_code(5))