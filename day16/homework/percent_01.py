#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
import time





def progress(pre,wid=100):
    if pre > 1:
        pre = 1
    str = ('[%%-%ds]' % wid) % (int(pre*wid)*'#')
    print('\r%s %s%%' % (str,pre*100),end='')

c = 0
t = 100
while c < t:
    time.sleep(0.05)
    c+=1
    progress(c/t)