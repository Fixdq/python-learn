# !/usr/bin/env python3
# encoding: utf-8
# by fixdq


class Myopen(object):
    def __init__(self, filepath, mode='r', encoding="utf-8"):
        self.filepath = filepath
        self.mode = mode
        self.encoding = encoding
        self.fobj = open(filepath, mode, encoding=encoding)

    def __del__(self):
        self.fobj.close()


f = Myopen('反射.py')
res = f.fobj.read()
print(res)

