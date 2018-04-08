# encoding: utf-8
# by fixdq
import time



# def index():
#     test_time.sleep(0.5)
#     print("这是主页")

# def index():
#     start_time = test_time.test_time()
#     test_time.sleep(0.5)
#     print("这是主页")
#     end_time = test_time.test_time()
#     print('传输时间：%s' % (end_time-start_time))
#
# index()

# # lv 01
# start_time = test_time.test_time()
# index()
# end_time = test_time.test_time()
# print('传输时间：%s' % (end_time - start_time))




# # lv 02
# start_time = test_time.test_time()
# index()
# end_time = test_time.test_time()
# print('传输时间：%s' % (end_time - start_time))

# #lv 03
# def wrapper(func):
#     start_time = test_time.test_time()
#     func()
#     end_time = test_time.test_time()
#     print('传输时间：%s' % (end_time - start_time))
#
# wrapper(index)

#
# def outter(func):
#     def wrapper():
#


def wrapper(func):
    def inner(*args,**kwargs):
        while True:
            uname = input('请输入用户名：').strip()
            upwd = input('请输入密 码：').strip()
            if uname =='fixd'and upwd:
                print('登录成功')
                res = func(*args,**kwargs)
                return res
            else:
                print('用户名或密码错误')

    return inner


@wrapper
def says(yy):
    print('哈哈哈哈哈哈')
    print(yy)
    return '你能上天'


res = says('尅还是')
print(res)





