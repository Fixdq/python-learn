# encoding: utf-8
# by fixdq
import os

product_list = [
    ['Iphone7', 5800],
    ['Coffee', 30],
    ['疙瘩汤', 10],
    ['Python Book', 99],
    ['Bike', 199],
    ['ViVo X9', 2499],
]

msg = '''
1.注册
2.登录
3.购物
'''
shopping_cart = {}
userinfo = []
db_file = r'db.txt'

while True:
    print(msg)
    ch = input('请选择：').strip()
    if ch == '1':
        # 注册
        uname = input('输入用户名：').strip()
        while True:
            pwd1 = input('输入密码：').strip()
            pwd2 = input('验证密码：').strip()
            if pwd1 == pwd2:
                break
            else:
                print('两次密码不一致')

        amount = input('输入充值金额：')
        with open(db_file, 'a', encoding='utf-8') as f:
            f.write('%s|%s|%s\n' % (uname, pwd2, amount))
        print('注册成功，请登录')
    elif ch == '2':
        # 登录
        count = 0
        tag = True
        while tag:
            if count == 3:
                print('输入错误次数，超过3次，退出～！！')
                break
            uname = input('输入用户名：').strip()
            pwd = input('输入密码：').strip()

            with open(db_file, 'r', encoding='utf-8') as f:
                for user in f:
                    user = user.strip("\n").split('|')
                    user_name = user[0]
                    user_pwd = user[1]
                    user_balance = user[2]
                    if user_name == uname and user_pwd == pwd:
                        # 登录成功 存入用户信息
                        print('登录成功')
                        userinfo = [user_name, user_balance]
                        print('%s您好，您的余额为：%s' % (user_name, user_balance))
                        tag = False
                        break
                else:
                    count += 1
                    print('用户名或密码错误')
    elif ch == '3':
        if len(userinfo) == 0:
            print('请先登录')
            continue
        else:
            print('欢迎您%s，您的余额为：%s' % (userinfo[0], userinfo[1]))
            tag = True
            while tag:
                for i, product in enumerate(product_list):
                    print(i, product)

                ch_p = input('请输入商品的编号,退出（q）')
                if len(ch_p) == 0: continue
                if ch_p.isdigit():
                    ch_p = int(ch_p)
                    if ch_p < 0 or ch_p >= len(product_list): continue
                    pname = product_list[ch_p][0]
                    pprice = product_list[ch_p][1]
                    pprice = int(pprice)
                    balance = int(userinfo[1])
                    if balance >= pprice:
                        # 扣钱
                        balance -= pprice
                        userinfo[1] = balance
                        # 判断购买的商品是否存在
                        if pname in shopping_cart:
                            shopping_cart[pname]['count'] += 1
                        else:
                            shopping_cart[pname] = {'price': pprice, 'count': 1}
                        print('购买成功，您的余额还有：%s' % userinfo[1])
                        continue
                    else:
                        print('余额不足')
                        continue
                if ch_p == 'q':
                    total_price = 0
                    print('购物列表')
                    print('%-10s%-10s%-10s%-10s%-10s' % ('编号', '名字', '价格', '数量', '合计'))
                    for i, v in enumerate(shopping_cart):
                        print('%-10s%-10s%-10s%-10s%-10s' % (
                            i,
                            v,
                            shopping_cart[v]['price'],
                            shopping_cart[v]['count'],
                            shopping_cart[v]['price'] * shopping_cart[v]['count']
                        ))
                        total_price += shopping_cart[v]['price'] * shopping_cart[v]['count']
                    while tag:
                        print('您本次的消费金额：%s,您的余额为：%s:' % (total_price,userinfo[1]))
                        ch_q = input('确定购买（y/n）:')
                        if ch_q == 'y':
                            with open(db_file, 'r', encoding='utf-8') as fr, \
                                    open('%s.swap' % db_file, 'w', encoding='utf-8') as fw:
                                for user in fr:
                                    if userinfo[0] == user.split('|')[0]:
                                        user_l = user.split('|')
                                        user_l[2] = '%s\n' % userinfo[1]
                                        user = '|'.join(user_l)
                                    fw.write(user)
                            os.remove(db_file)
                            os.rename('%s.swap' % db_file,db_file)
                            tag = False
                        elif ch_q == 'n':
                            tag = False
                        else:
                            continue

                        userinfo =[]
                        shopping_cart ={}

    else:
        print('error')
