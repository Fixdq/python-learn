#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


str = '你说的法师打发斯蒂芬'
# bytes >>>>>>> utf-8
with open('a.txt','wb') as f:
    str = str.encode('utf-8')
    f.write(str)

with open('a.txt','rb') as f:
    res = f.read()
    res = res.decode('utf-8')
    print(res)

str = '你说的法师打发斯蒂芬'
print(type(str))