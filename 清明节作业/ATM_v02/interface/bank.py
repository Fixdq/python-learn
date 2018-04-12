#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from db import db_handler
from interface import user
from lib import common

logger = common.get_logger('Bank')


def transfer_interface(from_name, to_name, account):
    """
    转账接口
    :param from_name: 
    :param to_name: 
    :param account: 
    :return: 
    """
    from_user_dic = user.get_userinfo_interface(from_name)
    to_user_dic = user.get_userinfo_interface(to_name)
    if from_user_dic['account'] >= account:  # 判断用户余额
        from_user_dic['account'] -= account
        to_user_dic['account'] += account
        from_user_dic['bankflow'].extend(['%s transfer %s yuan to %s' %
                                          (from_name, account, to_name)])
        to_user_dic['bankflow'].extend(['%s accept %s yuan to %s' %
                                        (to_name, account, from_name)])
        db_handler.update(from_user_dic)
        db_handler.update(to_user_dic)
        logger.info('%s 向 %s 转账 %s' % (from_name, to_name, account))
        return True
    else:
        False


def repay_interface(name, account):
    """
    还款接口
    :param name: 
    :param account: 
    :return: 
    """
    user_dic = user.get_userinfo_interface(name)
    user_dic['account'] += account
    # 记录流水
    user_dic['bankflow'].extend['%s 还款 %s' % (name, account)]
    db_handler.update(user_dic)
    logger.info('%s 还款 %s' % (name, account))


def custom_interface(name, account):
    """
    消费接口
    :param name: 
    :param account: 
    :return: 
    """
    user_dic = user.get_userinfo_interface(name)
    if user_dic['account'] >= account:
        user_dic['account'] -= account
        # 记录流水
        user_dic['bankflow'].extend(['%s custom %s'])
        db_handler.update(user_dic)
        return True
    else:
        return False


def get_balance_interface(name):
    """
    查看余额接口
    :param name: 
    :return: 
    """
    return user.get_userinfo_interface(name)['account']


def withdraw_interface(name, account):
    """
    取款接口
    :param name: 
    :param account: 
    :return: 
    """
    user_dic = user.get_userinfo_interface(name)
    # 判断余额是否足够
    if user_dic['account'] >= account * 1.05:
        user_dic['account'] -= account * 1.05
        # 写入用户数据
        db_handler.update(user_dic)
        # 日志记录
        logger.info('%s 取款 %s' % (name, account))
        return True
    else:
        return False


def check_record(name):
    """
    查看流水接口
    :param name: 
    :return: 
    """
    cur_user = user.get_userinfo_interface(name)
    # 日志记录
    logger.info('%s查看了银行流水' % name)
    return cur_user['bankflow']
