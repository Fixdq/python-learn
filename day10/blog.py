# encoding: utf-8
# by fixdq

# 比较两个数的大小
def max2(x,y):
    if x > y:
        return x
    else:
        return y
# 比较三个数的大小
def max3(x,y,z):
    res1=max2(x,y)
    res2=max2(res1,z)
    return res2

print(max3(11,199,2))



def func1():
    print('from func1')
    def func2(): #func2=内存地址
        print('from func2')
    print(func2)
func1()




x=1
y=x
def bar():
    print('from bar')
f=bar   # 作为对象赋值时 bar代表的值是 内存地址
f()


#2、可以当中参数传入
# x=1
# def func(a):
#     print(a)
#
# func(x)



# def bar():
#     print('from bar')
#
# def wrapper(func): #func=bar
#     func() #bar()
#
# wrapper(bar)


#3、可以当中函数的返回值
# x=1
# def foo():
#     return x
#
# res=foo()
# print(res)



# def bar():
#     print('from bar')
#
# def foo(func): #func=<function bar at 0x00000225AF631E18>
#     return func #return <function bar at 0x00000225AF631E18>
#
#
# # print(bar)
# f=foo(bar) #f=<function bar at 0x00000225AF631E18>
# # print(f)
# f()


#4、可以当中容器类型的元素
# x=1
# l=[x,]
#
# print(l)

# def get():
#     print('from get')
#
# def put():
#     print('from put')
#
# l=[get,put]
#
# # print(l)
# l[0]()










def func():
    print('from func')

#1、func可以被引用
f=func

#2、func可以当作参数传给x
def bar(x):
    print(x)
    x()

bar(func)

#3、func还可以当作返回值
def bar(x): # x=func
    return x #return func

res=bar(func) #res=func
# print(res)
res()