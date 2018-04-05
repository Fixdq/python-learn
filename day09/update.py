# encoding: utf-8
# by fixdq

import os

src_file = 'db.txt'
path_file = r'%s' % src_file
str_new = 'SB'
str_old = 'alex'

# 一
with open(path_file, 'r', encoding='utf-8') as f:
    data = f.read()
    data = data.replace(str_old, str_old)
with open(path_file, 'w', encoding='utf-8') as f:
    f.write(data)
# 二
with open(path_file, 'r', encoding='utf-8') as fr, \
        open(path_file, 'w', encoding='utf-8') as fw:
    for line in fr:
        fw.write(line.replace(str_old, str_new))
