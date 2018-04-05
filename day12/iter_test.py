# encoding: utf-8
# by fixdq


strs = 'lsdfadsfhkjhaskdjhfa'
l_test = ['asdf',234,'asddf',11]
dictulp = ('234',234,'sfdsdf','11221211212')
dic  = {'sd':'1111','fdf':22222}



iter_obj = dic.__iter__()

while True:
    try:
        print(iter_obj.__next__())
    except StopIteration:
        break