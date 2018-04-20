#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

"""
程序入口
"""
import os
import sys
from core import main

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    main.run()
