#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
import re

# 4月9日作业：
# == == == == == == == == == == == == == == == 必做作业 == == == == == == == == == == == == == == == =
# 用谷歌浏览器打开http: // maoyan.com /，点击榜单，然后点击鼠标右键选择：显示网页源代码，然后将显示出的内容存储到文件index.html中
# 1、匹配出文件index.html所有的链接
with open('index.html', encoding='utf-8') as f:
    content = f.read()
    reg = 'href="(http.*?)"'
    res = re.findall(reg, content)
    for link in res:
        print(link)
        # 2、有字符串
        # 'email1:378533872@qq.com email2:333312312@163.com eamil3:alexsb123@gmail.com'
        # 匹配出所有的邮箱地址：['378533872@qq.com', '333312312@163.com', 'alexsb123@gmail.com']
str1 = 'email1:378533872@qq.com email2:333312312@163.com eamil3:alexsb123@gmail.com'
reg1 = ':([a-z0-9]+@[a-z0-9]+.com)'
res1 = re.findall(reg1, str1)
for link in res1:
    print(link)
    # 3、编写程序，
    # 1、让用户输入用户名，要求用户输入的用户名只能是字母或数字，否则让用户重新输入，
    # 2、让用户输入密码，要求密码的长度为8 - 10位，密码的组成必须为字母、数字、下划线，密码开头必须为字母，否则让用户重新输入


def login():
    while True:
        uname = input('请输入用户名：').strip()
        if not re.match('^[a-zA-Z0-9]+$', uname):
            print('用户名只能是字母或数字')
            continue
        break
    while True:
        pwd = input('请输入密码：').strip()
        if not re.match('^[a-zA-Z][\w]{7,9}$', pwd):
            print('密码的组成必须为字母、数字、下划线，密码开头必须为字母(8-10)')
            continue
        break
    # login()

    # 4、有字符串
    # "1-12*(60+(-40.35/5)-(-4*3))"，匹配出所有的数字如['1', '-12', '60', '-40.35', '5', '-4', '3']


str2 = "1-12*(60+(-40.35/5)-(-4*3))"
reg2 = '-?\d+\.?\d*'
res2 = re.findall(reg2, str2)
for link in res2:
    print(link, end=',')

print()
    # 5、有字符串
    # "1-2*(60+(-40.35/5)-(-4*3))"，找出所有的整数如['1', '-2', '60', '', '5', '-4', '3']
str3 = "1-2*(60+(-40.35/5)-(-4*3))"
reg3 = '-?\d+\.\d*|(-?\d+)'
res3 = re.findall(reg3, str3)
for link in res3:
    print(link, end=',')
    # 6、ATM + 购物车作业：
    # 1、构建程序基本框架
    # 2、实现注册功能
    #
    # 7、明天早晨默写6
    #
    # == == == == == == == == == == == == == == == 答案 == == == == == == == == == == == == == == == =
    # 答案：
    # 1、re.findall('href="(.*?)"', 读取文件内容)
    # 2、re.findall(r":(.*?@.*?com)", 'email1:378533872@qq.com email2:333312312@163.com eamil3:alexsb123@gmail.com')
    # 3、
    # 1、判断用户输入的内容中如果匹配到[ ^ a - zA - Z0 - 9]则让用户重新输入
    # 2、 ^ [a - zA - Z]\w
    # {7, 10}$
    #
    #
    # 4、re.findall(r'-?\d+\.?\d*', "1-12*(60+(-40.35/5)-(-4*3))")
    # 5、re.findall(r"-?\d+\.\d*|(-?\d+)", "1-2*(60+(-40.35/5)-(-4*3))")
    #
    # 6、略
    #
    # 7、略
    #
    # == == == == == == == == == == == == == 可以考虑选做一个作业（不做完全可以）：正则表达式 + 函数递归调用实现一个计算器 == == == == == == == == == == == == == == == == == ==
    # 用户输入：1 - 2 * (
    # (60 + 2 * (-3 - 40.0 / 5) * (9 - 2 * 5 / 3 + 7 / 3 * 99 / 4 * 2998 + 10 * 568 / 14)) - (-4 * 3) / (16 - 3 * 2))
    # 可以得到计算的结果
