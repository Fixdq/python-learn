import sys


args=sys.argv
path_old = args[1]
path_new = args[2]
with open(r'%s' %path_old,'rb') as fr,\
        open(r'%s' %path_new,'wb') as fw:
    for line in fr:
        fw.write(line)
    else:
        print('copy complete')