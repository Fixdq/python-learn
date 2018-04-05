# encoding: utf-8
# by fixdq



def outter():

    def inner():
        x = 2
        print('inner func %s' % x )

    return inner

f= outter()



def foo():
    x= 4444444444
    f()

foo()