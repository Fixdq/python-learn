#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

import json
import os
from conf import settings as st


# DB_ATUH = '/home/fixd/project/oldboy/清明节作业/ATM/db/current_user.json'


# dic = {"uname":""}
# with open(DB_ATUH, 'w',encoding='utf-8') as f:
#     json.dump(dic,f)
#

# 查询数据  是否授权
def get_is_auth():
    with open(st.DB_ATUH, encoding='utf-8') as f:
        res = json.load(f)
        if res['uname']:
            return True
        else:
            return False


# 格式化用户信息字典
def get_dic_user(uname, pwd, balance, credit):
    dic = {
        "uname": uname,
        "pwd": pwd,
        "balance": balance,
        "credit": credit,
    }
    return dic


# 拼接用户信息的具体路径
def get_path(uname):
    return os.path.join(st.DB_PATH_USERS, '%s.json' % uname)


# 添加用户登录状态
def add_cur_user(uname):
    dic = {"uname": uname}
    with open(st.DB_ATUH, 'w', encoding='utf-8') as f:
        json.dump(dic, f)


# 获取当前登录用户
def get_cur_user():
    with open(st.DB_ATUH, 'r', encoding='utf-8') as f:
        return json.load(f)['uname']


# 清除当前登录,退出登录
def rm_cur_user():
    dic = {"uname": ""}
    with open(st.DB_ATUH, 'w', encoding='utf-8') as f:
        json.dump(dic, f)


# 验证用户名，密码
def db_validate_user(uname, pwd=None):
    """
    uname 存在 True   不存在  False
    :param pwd: 密码
    :param uname: 用户名
    :return:boolean
    """
    # 用户信息文件路径
    db_path = get_path(uname)
    if pwd is None:
        # 判断文件是否存在 即判断用户是否存在
        return os.path.isfile(db_path)
    else:
        if os.path.isfile(db_path):

            # 判断用户密码是正确
            with open(db_path, encoding='utf-8') as f:
                user = json.load(f)
                if pwd == user['pwd']:
                    return True
                else:
                    return False
        else:
            return False


# 添加新用户信息
def db_add_user(uname, pwd, balance, credit=st.CREDIT):
    """

    :param uname:
    :param pwd:
    :param balance:
    :param credit:
    :return:
    """
    db_path = get_path(uname)
    dic = get_dic_user(uname, pwd, balance, credit)
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(dic, f)


# 更新用户信息
def db_update_user(uname, money, account='balance', mode='-'):
    """

    :param uname: 用户名
    :param money: 变动金额
    :param account: 'balance' 余额账户， 'credit' 信用账户
    :param mode: '-' 扣钱操作， '+' 加钱操作
    :return:None
    """
    db_path = get_path(uname)
    # 获取用户信息   更改用户的数据
    with open(db_path, 'r', encoding='utf-8') as f:
        user_dic = json.load(f)
        if account == 'balance':
            if mode == '-':
                user_dic['balance'] -= money
            elif mode == '+':
                user_dic['balance'] += money
        elif account == 'credit':
            if mode == '-':
                user_dic['credit'] -= money
            elif mode == '+':
                user_dic['credit'] += money
    # 覆盖原来的信息
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f)


# 根据用户名，获取用户余额
def db_sel_user_money(uname, account='balance'):
    """
    根据 uname 获取用户余额/信用额度
    :param uname:用户名
    :param account: 'balance' 余额账户， 'credit' 信用账户,'all' 两个账户都返回
    :return:int
    """
    db_path = get_path(uname)
    with open(db_path, 'r', encoding='utf-8') as f:
        if account == 'balance':
            return json.load(f)['balance']
        if account == 'credit':
            return json.load(f)['credit']


# 根据用户名，获取用户信息
def db_sel_user_info(uname):
    """
    根据用户名，获取用户信息
    :param unname: 用户名
    :return: dict
    """
    db_path = get_path(uname)
    with open(db_path, encoding='utf-8') as f:
        return json.load(f)
