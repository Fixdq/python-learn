#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


# 注册
import json
import random

import time


def register():
    uname = input('请输入用户名:')
    pwd1 = input('请输入密码:')
    pwd2 = input('请确认密码:')
    gender = input('性别:')
    age = input('请输入年龄:')
    user_info = {
        'uname': uname,
        'pwd': pwd1,
        'gender': gender,
        'age': age,
    }
    code = random_code(4)
    start_time = time.time()
    while True:
        print(code)
        code_inp = input('请输入验证码：')
        if code == code_inp:
            db_write_user(user_info)
            print("注册成功！")
            break
        else:
            if time.time() - start_time > 5:
                code = random_code(4)
                start_time = time.time()
                print('验证码过期！')

            else:
                print('验证码输入不正确！')


# 写入用户信息
def db_write_user(userinfo):
    with open('%s.json' % userinfo['uname'], 'w', encoding='utf-8') as f:
        json.dump(userinfo, f)


# 生成随机验证码
def random_code(len):
    code = ''
    for i in range(len):
        s1 = str(random.randint(0, 9))
        s2 = chr(random.randint(65, 90))
        code += random.choice([s1, s2])
    return code


if __name__ == '__main__':
    # login()
    register()
