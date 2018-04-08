#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
"""
用户输入未验证，会有bug
"""

import json
import os
import time

cur_user = []


# 登录验证装饰器
def deco_islogin(func):
    def wrapper(*args, **kwargs):
        if cur_user:
            return func(*args, **kwargs)
        else:
            login()

    return wrapper


# 用户交互
def inp_uname_pwd():
    uname = input('请输入用户名：')
    pwd = input('请输入密码：')
    return uname, pwd


# 写入锁定的用户信息
def db_lock(dic):
    with open('lock.json', 'w', encoding='utf-8')as f:
        json.dump(dic, f)


# 清除锁定用户
def db_lock_clear(uname):
    with open('lock.json', encoding='utf-8')as f:
        dic = json.load(f)
        dic.pop[uname]
    with open('lock.json', 'w', encoding='utf-8')as f:
        json.dump(dic, f)


# 读取被锁定的用户信息
def db_lock_get():
    # 判断lock.json是否存在，不存在则创建一个
    if not os.path.exists('lock.json'):
        with open('lock.json', 'w', encoding='utf-8'): pass
    # lock.json中有信息，返回字典
    if os.path.getsize('lock.json'):
        with open('lock.json', encoding='utf-8')as f:
            return json.load(f)
    # lock.json中没有信息 返回空字典
    return {}


# 模拟验证密码
def validate(uname, pwd):
    if uname == 'q' and pwd == 'q':
        return True
    else:
        return False


# login
def login():
    # 用于记录      本次用户的登录记录
    user_name_pwd = {}
    # 登录
    while True:
        uname, pwd = inp_uname_pwd()
        dic = db_lock_get()
        # 用户已经被锁定
        if dic is not None:
            if uname in dic:
                # 获取用户已经被锁定的时间
                lock_time = time.time() - dic[uname]['lock_time']
                # 时间不到5分钟  继续锁定
                if lock_time <= 60 * 5:
                    print('您被锁定5分钟，请稍后再试')
                    continue
                else:
                    # 超过了5分钟，清除用户的锁定状态
                    db_lock_clear(uname)

        # 用户第一次登录，失败 count + 1
        if uname not in user_name_pwd:
            if validate(uname, pwd):
                print('登录成功！')
                break
            else:
                user_name_pwd[uname] = {'count': 1, 'lock_time': time.time()}
                print('验证失败！')
                continue

        # 用户小于3次尝试 登录成功
        if uname in user_name_pwd and user_name_pwd[uname]['count'] < 3 and validate(uname, pwd):
            print('登录成功！')

        # 用户登录失败
        print('验证失败！')
        # count + 1
        user_name_pwd[uname]['count'] += 1
        # 如果 登录失败三次   将用户信息写入文件
        if user_name_pwd[uname]['count'] == 3:
            # 用户最后一次 登录错误的时间
            user_name_pwd[uname]['lock_time'] = time.time()
            # 将用户信息写入文件
            dic[uname] = user_name_pwd[uname]
            db_lock(dic)
            print('您被锁定5分钟，请稍后再试')


# 模拟需要被装饰的函数
@deco_islogin
def shop():
    pass


if __name__ == '__main__':
    shop()
