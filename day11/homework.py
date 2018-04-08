# encoding: utf-8
# by fixdq
import time

# 3-29 作业
# 	一：编写一个有参和一个无参函数，然后实现下列装饰器
# def run():
#     print('正在跑步')
# def runs(name):
#     print('%s正在跑步' % name)

# 	二：编写装饰器，为函数加上统计时间的功能
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = test_time.test_time()
#         res = func(*args, **kwargs)
#         end_time = test_time.test_time()
#         print(end_time - start_time)
#         return res
#
#     return wrapper


# @decorator
# def run():
#     test_time.sleep(1)
#     print('正在跑步')
#
#
# @decorator
# def runs(name):
#     test_time.sleep(1)
#     print('%s正在跑步' % name)
#
# run()
# runs('fixd')

# 	三：编写装饰器，为函数加上认证的功能

# def decorator(func):
#         def wrapper(*args, **kwargs):
#             uname = input('请输入用户名：').strip()
#             upwd = input('请输入密 码：').strip()
#             if uname == 'fixd' and upwd == '123':
#                 print('登录成功')
#                 res = func(*args, **kwargs)
#                 return res
#             else:
#                 print('用户名或密码错误')
#
#         return wrapper
# @decorator
# def runs(name):
#     test_time.sleep(1)
#     print('%s正在跑步' % name)
# runs('fixd')

# 	四：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
# 	注意：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式

# path_file = r'db.txt'
# current_user = {'name':'','password':''}
# ss = 's'
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         if current_user['name']:
#             print('在线中。。。')
#             r = func(*args, **kwargs)
#             return r
#         while True:
#             uname = input('输入用户名:').strip()
#             pwd = input('输入密 码:').strip()
#
#             with open(path_file,'r',encoding='utf-8') as f:
#                 for line in f:
#                     user = eval(line.strip('\n'))
#                     if uname == user['name'] and pwd == user['password']:
#                         print('登录成功')
#                         current_user['name'] = uname
#                         r = func(*args, **kwargs)
#                         return r
#                 else:
#                     print('用户名或密码不正确！')
#     return wrapper
# @decorator
# def index():
#     print('index page')
# @decorator
# def manager():
#     print('manager page')
#
# index()
# manager()


# 	五：编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录
# import test_time
# path_file = r'db.txt'
# current_user = {'name':'','login_time':''}
# auto_loginout_time = 10
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         if current_user['name']:
#             current_time = test_time.test_time()
#             login_time = current_user['login_time']
#             if current_time - login_time < auto_loginout_time:
#                 print('在线中。。。')
#                 r = func(*args, **kwargs)
#                 return r
#         while True:
#             uname = input('输入用户名:').strip()
#             pwd = input('输入密 码:').strip()
#
#             with open(path_file,'r',encoding='utf-8') as f:
#                 for line in f:
#                     user = eval(line.strip('\n'))
#                     if uname == user['name'] and pwd == user['password']:
#                         print('登录成功')
#                         current_user['name'] = uname
#                         current_user['login_time'] = test_time.test_time()
#                         r = func(*args, **kwargs)
#                         return r
#                 else:
#                     print('用户名或密码不正确！')
#     return wrapper
# @decorator
# def index():
#     test_time.sleep(2)
#     print('index page')
# @decorator
# def manager():
#     print('manager page')
#
# index()
# manager()










#
# 	六：编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
#
# import requests
#
# url = "https://www.baidu.com"
# def get_html(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.text
# res = get_html(url)
# print(res)
# 	七：为题目五编写装饰器，实现缓存网页内容的功能：
# 	具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中
#
# 	扩展功能：用户可以选择缓存介质/缓存引擎，针对不同的url，缓存到不同的文件中
#
# import requests
# path_db_url =r'db_url.txt'
# url = "https://www.baidu.com"
# def decoretor(func):
#     def wrapper(*args,**kwargs):
#         url = args[0]
#         with open(path_db_url,'r',encoding='utf-8') as f:
#             data = f.read()
#             if len(data) == 0:
#                 res = func(*args, **kwargs)
#                 with open(path_db_url, 'w', encoding='utf-8') as f:
#                     f.write(res)
#                 return res
#             else:
#                 print('缓存')
#
#                 return data
#     return wrapper
# @decoretor
# def get_html(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#        return response.text
# res = get_html(url)
# print(res)


# import requests
#
# path_db_txt_url = r'db_url.txt'
# path_db_text_url = r'db_url.text'
# url = "https://www.baidu.com"
#
# def change(db):
#     def decoretor(func):
#         def wrapper(*args, **kwargs):
#             url = args[0]
#             path_db = ''
#             if db == "txt":
#                 path_db =path_db_txt_url
#             elif db == "text":
#                 path_db = path_db_text_url
#
#             with open(path_db, 'r', encoding='utf-8') as f:
#                 data = f.read()
#                 if len(data) == 0:
#                     res = func(*args, **kwargs)
#                     with open(path_db, 'w', encoding='utf-8') as f:
#                         f.write(res)
#                     return res
#                 else:
#                     print('缓存')
#                     return data
#         return wrapper
#     return decoretor
#
# @change('text')
# def get_html(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.text
#
#
# res = get_html(url)
# print(res)


# 	八：还记得我们用函数对象的概念，制作一个函数字典的操作吗，来来来，我们有更高大上的做法，在文件开头声明一个空字典，然后在每个函数前加上装饰器，完成自动添加到字典的操作
#

# dic_func ={}
#
# def make_rute(name):
#     def deco(func):
#             dic_func[name] = func
#     return deco
#
#
# @make_rute('aaa')
# def aaa():
#     print('aaa')
#
# @make_rute('bbb')
# def bbb():
#     print('bbb')
#
#
# @make_rute('ccc')
# def ccc():
#     print('ccc')
#
# print(dic_func)

# 	九 编写日志装饰器，实现功能如：一旦函数f1执行，则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，日志文件路径可以指定
# 	注意：时间格式的获取
# 	import test_time
# 	test_time.strftime('%Y-%m-%d %X')
#
#
import os


def choice_file(logfile):
    def deco(func):
        if os.path.exists(logfile):
            with open(logfile,'w'):pass
        def inner(*args,**kwargs):
            res = func(*args,**kwargs)
            with open(logfile,'a',encoding='utf-8') as f:
                f.write("%s %s run\n" % (time.strftime('%Y-%m-%d %X'),func.__name__ ))
            return res
        return inner
    return deco

@choice_file(logfile='f.log')
def f1():
    print('开始了')
f1()
# 	参考答案：
# 	http://www.cnblogs.com/linhaifeng/articles/7532497.html#_label6
