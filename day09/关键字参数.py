# def foo(x, y, z):
#     print(x, y, z)
#
#
# foo(1, 2, 3)  # 位置参数的调用方式
# foo(x=1, y=2, z=3)  # 关键字参数
# foo(y=2, x=1, z=3)  # 关键字参数
#
#
# def register(name, age, sex='male'):  # sex是默认参数
#     print(name, age, sex)
#
#
# register('fixd', 18, )  # 默认参数 没有传值
# register('mike', 20, 'female')  # 默认参数 传入一个新值

m = 10

def foo(x, y=m):
    print(x, y)

m = '20'
foo(1)
foo(1, 11)
