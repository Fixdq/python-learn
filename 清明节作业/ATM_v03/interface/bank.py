#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from db import db_handler
from lib import common

logger = common.get_logger('bank')


def repay_interface(name, account):
    user_dic = db_handler.select(name)
    user_dic['account'] += account
    user_dic['bankflow'].append('%s还款%s' % (name, account))
    logger.info('%s还款%s' % (name, account))
    db_handler.update(user_dic)


def withdraw_interface(name, account):
    user_dic = db_handler.select(name)
    user_dic['account'] -= account
    user_dic['bankflow'].append('%s取款%s' % (name, account))
    logger.info('%s取款%s' % (name, account))

    db_handler.update(user_dic)


def transfer_interface(from_user, to_user, account):
    from_user_dic = db_handler.select(from_user)
    to_user_dic = db_handler.select(to_user)

    from_user_dic['account'] -= account
    from_user_dic['bankflow'].append('%s转给%s 金额%s' % (from_user, to_user, account))
    to_user_dic['account'] += account
    to_user_dic['bankflow'].append('%s收到%s 金额%s' % (to_user, from_user, account))

    logger.info('%s转给%s 金额%s' % (from_user, to_user, account))
    logger.info('%s收到%s 金额%s' % (to_user, from_user, account))

    db_handler.update(from_user_dic)
    db_handler.update(to_user_dic)


def check_balance_interface(name):
    logger.info('%s查看余额' % name)
    return db_handler.select(name)['account']


def check_record_interface(name):
    logger.info('%s查看流水记录' % name)
    return db_handler.select(name)['bankflow']
