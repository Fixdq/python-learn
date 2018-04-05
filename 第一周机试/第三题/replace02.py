# encoding: utf-8
# by fixdq
import os

path_test = r'b.txt'
path_test_swap = r'b.txt.swap'

with open(path_test, 'r', encoding='utf-8') as fr, \
        open(path_test_swap, 'a', encoding='utf-8') as fw:
    for line in fr:
        data = line.replace('alex', 'SB')
        fw.write(data)
    os.remove(path_test)
    os.renames(path_test_swap, path_test)
