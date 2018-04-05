# encoding: utf-8
# by fixdq

path_test = r'a.txt'

with open(path_test,'r',encoding='utf-8') as f:
        data = f.read()
        data = data.replace('alex','SB')
with open(path_test,'w',encoding='utf-8') as f:
    f.write(data)
