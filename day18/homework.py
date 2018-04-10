#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

import hashlib

# 4月10号作业
# 	1、编写用户认证功能，要求如下
# 		1.1、对用户密码加盐处理
# 		1.2、用户名与密文密码存成字典，是以json格式存到文件中的
# 		1.3、要求密用户输入明文密码，但程序中验证的是密文
#
import json
import subprocess


def register():
    uname = input('input username:')
    pwd = input('input pwd:')
    m = hashlib.md5()
    m.update('kl'.encode('utf-8'))
    m.update(pwd.encode('utf-8'))
    m.update('lk'.encode('utf-8'))
    res = m.hexdigest()
    user_dic = {
        'name': uname,
        'pwd': res,
    }
    with open('%s.json' % uname, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f)


def auth():
    uname = input('input username:')
    pwd = input('input pwd:')
    m = hashlib.md5()
    m.update('kl'.encode('utf-8'))
    m.update(pwd.encode('utf-8'))
    m.update('lk'.encode('utf-8'))
    with open('%s.json' % uname, encoding='utf-8') as f:
        user_dic = json.load(f)
    if m.hexdigest() == user_dic['pwd'] and uname == user_dic['name']:
        # print('login success')
        return True
    else:
        # print('name or password is fail~')
        return False


# register()
# auth()

# 	2、编写功能，传入文件路径，得到文件的hash值
#

def get_file_md5(path):
    m = hashlib.md5()
    with open(path, 'rb') as f:
        for line in f:
            m.update(line)
        res = m.hexdigest()
    print(res)


# get_file_md5('/home/fixd/project/python_learn/day18/subprocess_test.py')


# 	3、编写类cmd的程序，要求
# 		1、先验证用户身份
# 		2、认证通过后，用户输入命令，则将命令保存到文件中

def cmd_func():
    if auth():
        cmd = input('>>>:').strip()
        res = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        info_success = res.stdout.read().decode('utf-8')
        with open('%s.json' % cmd, 'w', encoding='utf-8') as f:
            json.dump(info_success, f)


# cmd_func()
# 	4、如果我让你编写一个选课系统，那么有如下对象，请抽象成类，然后在程序中定义出来
# 		4.1 老男孩有两所学校：北京校区和上海校区
# 		4.2 老男孩学校有两们课程：python和linux
# 		4.3 老男孩有老师：egon，alex，lxx，wxx，yxx
# 		4.3 老男孩有学生：。。。
# 		4.4 老男孩有班级：python全栈开发1班，linux高级架构师2班


class Student:
    name = ''
    age = ''
    gender = ''
    school = ''
    class_name = ''

    def learn(self):
        print('is learning')

    def choose(self):
        print('is learning')


class Teacher:
    name = ''
    age = ''
    gender = ''
    school = ''
    teach_class_name = ''

    def teach(self):
        print('is learning')

    def choose(self):
        print('is learning')
