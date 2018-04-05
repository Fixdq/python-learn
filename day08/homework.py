# encoding: utf-8
# 2 - 26
# 作业：
#
# 一、参考: http: // www.cnblogs.com / linhaifeng / articles / 7133357.
# html  # _label12
# 完成购物车作业
#
# 二、函数练习：
# 1、写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作

import os


def f_update_onceall(path, old, new):
    with open(r'%s' % path, 'r', encoding='utf-8') as f:
        data = f.read()
        data = data.replace(old, new)
    with open(r'%s' % path, 'w', encoding='utf-8') as f:
        f.write(data)


def f_update_line(path, old, new):
    with open(r'%s' % path, 'r', encoding='utf-8') as fr, \
            open(r'%s.swap' % path, 'a', encoding='utf-8')as fw:
        for line in fr:
            fw.write(line.replace(old, new))
        os.remove(r'%s' % path)
        os.rename(r'%s.swap' % path, r'%s' % path)


file_path = '/home/fixdq/project/day08/blog'
old = '2'
new = '1'
# f_update_line(file_path, old, new)
f_update_onceall(file_path, old, new)


# 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数


def attr_count(strs):
    # 数字个数
    nd_count = 0
    # 字母个数
    letter_count = 0
    # 空格个数
    space_count = 0
    # 其他个数
    other_count = 0
    for item in strs:
        if item.isdigit():
            nd_count += 1
        elif item.isalpha():
            letter_count += 1
        elif item == ' ':
            space_count += 1
        else:
            other_count += 1
    return nd_count, letter_count, space_count, other_count


res = attr_count('a6b7 n8h 9+q1 r4+')
print(res)


# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。


def len_more_five(obj):
    """
    obj --> 字符串、列表、元组
    :param obj:
    :return 长度是否大于5 True 长度是否小于5 False
    """

    return len(obj) > 5


# 4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。


def len_list(ls):
    if len(ls) > 2:
        list_new = ls[:2]
        return list_new
    else:
        return list


# 5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。


def odd_list_tuple(ls):
    return ls[1::2]


# 6、写函数，检查字典的每一个value的长度, 如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
# PS: 字典中的value只能是字符串或列表


def len_v_more_two(dicts):
    for k, v in dicts.items():
        if len(v) > 2:
            v_new = v[:2]
            dicts[k] = v_new
    return dicts


dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
print(len_v_more_two(dic))


# 7、编写认证功能函数，注意：后台存储的用户名密码来自于文件
# name|pwd

def auth(uname, pwd):
    """
    用户登录验证
    :param uname:
    :param pwd:
    :return: 成功True  失败False
    """
    with open('db.txt', 'r', encoding='utf-8') as f:
        for line in f:
            user = line.split("|")
            if uname == user[0] and pwd == user[1].strip('\n'):
                return True
    return False


# 8、编写注册功能函数，将用户的信息储存到文件中


def regist(uname, pwd):
    """
    用户注册
    :param uname:
    :param pwd:
    :return 用户已存在 False  True 注册成功:
    """
    # 判断用户名是否存在
    with open('db.txt','r',encoding='utf-8') as fr:
        for line in fr:
            user = line.split("|")
            if user[0] == uname:
                return False
    with open('db.txt', 'a', encoding='utf-8') as fw:
        fw.write('%s|%s\n' % (uname, pwd))
    return True


# 9、编写查看用户信息的函数，用户的信息是事先存放于文件中的


def show_users():
    """
    展示用户信息
    :return: None
    """
    with open('db.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line)


# 模拟数据 注册

res = regist('fixd', '123456')
print(res)
# 登录
res = auth('fixd', '123456')
print(res)
# 查看用户
show_users()