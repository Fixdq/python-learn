#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
"""
购物车
"""
from core import db_handler as db

# 临时购物车
product_car = {}
product_list = []
uname = ''
current_balance = 0


# 初始化购物信息
def shop_init():
    global product_list, uname, current_balance
    product_list = db.db_sel_product_list()
    uname = db.get_cur_user()
    current_balance = db.db_sel_user_money(uname, account='credit')


# 显示商品列表
def show_product_list(product_list):
    # 商品信息
    print('--------------------------------------')
    print('%-18s%-18s%-18s' % ('编号', '名称', '单价'))
    for i, v in enumerate(product_list):
        print('%-20s%-20s%-20s' % (
            i,
            v[0],
            v[1],
        ))
    print('--------------------------------------')


# 显示购物车列表
def show_car_list(product_car):
    print('--------------------------------------')
    print('%-18s%-18s%-18s%-18s%-18s' % ('编号', '名称', '单价', '数量', '合计'))
    totals = 0
    for i, v in enumerate(product_car):
        pprice = product_car[v]['pprice']
        count = product_car[v]['count']
        totals += pprice * count
        print('%-20s%-20s%-20s%-20s%-20s' % (
            i,
            v,
            pprice,
            count,
            pprice * count
        ))
    print('--------------------------------------')
    return totals


# 添加商品到购物车
def car_add(pname, pprice):
    global current_balance
    if pname in product_car:
        product_car[pname]['count'] += 1
    else:
        product_car[pname] = {'pprice': pprice, 'count': 1}
    # 扣钱
    current_balance -= pprice
    # 提示
    print(' %s 已经添加到购物车！～！' % pname)


# 结算
def shop_settle(product_car_list):
    while True:
        # 显示购物车信息
        totals = show_car_list(product_car)
        choice = input('%s你好，您一共消费了%s，是否够买(y/n)' % (uname, totals))
        if len(choice) == 0:
            print('输入不能为空')
            continue
        if choice not in ['y', 'n']:
            print('输入不正确')
            continue
        if choice == 'y':
            # 确认购买
            # 更新用户余额 使用信用
            db.db_update_user(uname, totals, account='credit', mode='-')
            print('结算成功！')

        break


# 购物
def shopping():
    # 初始化
    shop_init()
    global product_car
    tag = True
    while tag:
        # 商品信息
        show_product_list(product_list)
        # 开始买了
        choice = input('请输入商品编号购买（q:查看购物车，结账）：').strip()
        if len(choice) == 0:
            print('请正确输入您的选择！')
            continue
        if choice.isdigit():
            choice = int(choice)
            if choice < 0 or choice >= len(product_list):
                print('请正确输入您的选择！')
                continue
            production = product_list[choice]
            # 检测是否购买过
            pname = production[0]
            pprice = production[1]
            # 判断用户余额是否足够
            # 可用信用额度
            user_credit = current_balance
            if user_credit < pprice:
                print('您的信用额度不足，还有：%s' % user_credit)
                continue
            # 添加商品到购物车
            car_add(pname, pprice)
        elif choice == 'q':
            if not product_car:
                print('购物车没有商品～！～！～')
                continue
            # 结算
            shop_settle(product_car)
            return
