# encoding: utf-8
# by fixdq

# def f1():
#     print('f1')
#
#
# def f2():
#     print('f2')
#
#
# def f3():
#     print('f3')
#
#
# L = [f1, f2, f3]
# for f in L:
#     f()
# ch_l = {
#     '1':f1,
#     '2':f2,
#     '3':f3
#
# }
#
#
# while True:
#     print('''
#         1. f1
#         2. f2
#         3. f3
#
#     ''')
#     ch_u = input('选择：')
#     if ch_u in ch_l:
#         ch_l[ch_u]()
#     else:
#         print('非法输入')
#         continue
#
#

def foo(x,y,z,*args): #args=(4,5,6,7,8)
    print(x,y,z)
    print(args)

foo(1,2,3,4,5,6,7,8,)

def foo(x,y,z,**kwargs): # kwargs={'c':3,'a':1,'b':2}
    print(x,y,z)
    print(kwargs)

foo(x=1,y=2,z=3,a=1,b=2,c=3)