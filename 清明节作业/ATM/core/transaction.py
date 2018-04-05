#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from core import db_handler as db
from conf import settings as st
from core import auth


# 查看用户信息
@auth.auth
def show_user_info():
    uname = db.get_cur_user()
    userinfos = db.db_sel_user_info(uname)
    print('-------------------------------------------')
    print('尊敬的%s，余额：%s，信用额度：%s' % (
        userinfos['uname'],
        userinfos['balance'],
        userinfos['credit'],
    ))
    print('-------------------------------------------')


# 转账
@auth.auth
def transfer():
    tag = True
    while tag:
        account_target = input('请输入目标用户名字：').strip()
        if len(account_target) == 0:
            print('用户名不能为空')
            continue
        if not account_target.isalpha():
            print('用户名必须为字母组成')
            continue
        if not db.db_validate_user(account_target):
            print('目标账户不存在')
            continue
        while tag:
            transfer_money = input('请输入转账金额：').strip()
            if len(transfer_money) == 0:
                print('金额不能为空！')
            if transfer_money.isdigit():
                transfer_money = int(transfer_money)
                # 获取当前用户名
                uname = db.get_cur_user()
                # 获取当前用户余额
                current_user_balance = db.db_sel_user_money(uname)
                if transfer_money >= current_user_balance:
                    print('您的账户余额不足，余额为：%s' % current_user_balance)
                    continue
                else:
                    # 所有条件满足 账户转账
                    # 扣款账户    扣款
                    db.db_update_user(uname, transfer_money)
                    # 目标账户    加钱
                    db.db_update_user(account_target, transfer_money, mode="+")
                    print('转账成功！')
                    tag = False
            else:
                print('金额输入不正确！')


# 还款
@auth.auth
def pay_back():
    # 获取当前登录用户名
    uname = db.get_cur_user()
    credit = st.CREDIT
    # 检测需要还款金额
    current_user_credit_money = db.db_sel_user_money(uname, account='credit')
    pay_back_money = credit - current_user_credit_money
    if pay_back_money <= 0:
        print('您的信用额度为%s，可用额度%s，无需还款！' %
              (credit, current_user_credit_money))
        return
    elif pay_back_money > 0:
        print('您的信用额度为%s，可用额度%s，需还款%s' %
              (credit, current_user_credit_money, pay_back_money))
    while True:
        pay_inp = input('请输入还款额度：').strip()
        if len(pay_inp) == 0:
            print('输入不能为空！')
            continue
        if pay_inp.isdigit():
            pay_inp = int(pay_inp)
            # 检测账户余额是否足够
            balance = db.db_sel_user_money(uname)
            if pay_inp > balance:
                print('余额不足')
                continue
            else:
                # 余额账户扣钱
                db.db_update_user(uname, pay_inp)
                # 信用账户加钱
                db.db_update_user(uname, pay_inp, account='credit', mode="+")
                print("还款成功！")
                break
        else:
            print('输入不正确！')

    # 还款
    pass


# 取现
@auth.auth
def with_draw():
    uname = db.get_cur_user()
    while True:
        money = input('请输入取款金额：').strip()
        if len(money) == 0:
            print('输入不能为空！')
            continue
        if money.isdigit():
            money = int(money)
            # 手续费
            charge_money = int(money / 100 * 5)
            # 检测账户余额是否足够
            balance = db.db_sel_user_money(uname)
            if (money + charge_money) > balance:
                print('余额不足！')
                continue
            else:
                # 余额账户扣钱
                db.db_update_user(uname, money + charge_money)
                print('成功取款%s，手续费%s，余额%s' %
                      (money, charge_money, db.db_sel_user_money(uname)))
                break
        else:
            print('输入不正确！')
