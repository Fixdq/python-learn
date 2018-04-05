#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)


from core import src

print(os.getcwd())
print('-------------------')
print(BASE_DIR)

src.run()
