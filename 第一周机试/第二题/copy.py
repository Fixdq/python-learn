# encoding: utf-8
# by fixdq

import sys

data = sys.argv
path_old = r'%s' % data[1]
path_new = r'%s' % data[2]


with open(path_old,'rb') as fr,\
    open(path_new,'wb') as fw:
    for line in fr:
        fw.write(line)