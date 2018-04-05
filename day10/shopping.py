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
    choice01 = input('请选择：')
    if choice01 == '1':
        # 注册
        tag = True
        while tag:
            # 用户名
            while tag:
                uname = input('请输入用户名：').strip()
                if len(uname) == 0:
                    print('用户名不能为空')
                    continue
                if not uname.isalpha():
                    print('用户名不能为空')
                    continue
                with open(db_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        if uname == line.split('|')[0]:
                            print('用户名已存在')
                            break
                    else:
                        # 密码
                        while tag:
                            pwd1 = input('请输入密码：').strip()
                            pwd2 = input('请再次输入密码：').strip()
                            if len(pwd1) == 0:
                                print('密码不能为空')
                                continue
                            if pwd1 == pwd2:
                                # 充值金额
                                while tag:
                                    balance = input('请输入充值金额')
                                    if len(balance) == 0:
                                        print("余额不能为空")
                                    if balance.isdigit():
                                        balance = int(balance)
                                        if balance < 0:
                                            print('输入不正确')
                                        else:
                                            with open(db_file, 'a', encoding='utf-8') as f:
                                                f.write('%s|%s|%s\n' % (uname, pwd2, balance))
                                                print('注册成功')
                                                tag = False
                                                break
                                    else:
                                        print('输入不正确')
                            else:
                                print('两次密码输入不一致')

    elif choice01 == '2':
        count = 0
        tag = True
        while tag:
            if count == 3:
                print('错三次了，退出')
                break
            # 用户名
            uname = input('请输入用户名：').strip()
            pwd = input('请输入密码：').strip()
            if len(pwd) == 0 or len(uname) == 0:
                print('用户名和密码不能为空')
                count += 1
                continue
            # 验证
            while tag:
                with open(db_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        user_l = line.strip("\n").split('|')
                        if uname == user_l[0] and pwd == user_l[1]:
                            print('登录成功')
                            userinfo = [uname,int(user_l[2])]
                            tag = False
                            break
                    else:
                        count += 1
                        print('用户或密码错误')
                        break

    elif choice01 == '3':
        # 判断用户是否登录
        if not userinfo:
            print('请先登录！')
            continue
        # 显示余额
        print('欢迎%s,您的余额为%s' % (userinfo[0], userinfo[1]))
        # 打印商品列表
        tag = True

        # 用户选择
        while tag:
            print('---------------------------------------------------')
            print('%-18s%-18s%-18s' % (
                '编号',
                '名字',
                '价格',
            ))
            for i, v in enumerate(product_list):
                print('%-20s%-20s%-20s' % (
                    i,
                    v[0],
                    v[1],
                ))
            print('---------------------------------------------------')
            choice = input('请选择购买的商品编号：(q退出)').strip()

            if choice.isdigit():
                choice = int(choice)
                if choice < 0 or choice > len(product_list):
                    print('输入非法')
                    continue
                # 检测余额
                pname = product_list[choice][0]
                pprice = int(product_list[choice][1])
                if userinfo[1] < int(pprice):
                    print('余额不足，你的余额还有：%s' % userinfo[1])
                    continue
                # 余额充足

                if pname in shopping_cart:
                    shopping_cart[pname]['count'] += 1
                else:
                    shopping_cart[pname]={'pprice':pprice,'count':1}

                # 扣钱
                userinfo[1] -= pprice
                # 显示提示
                print('%s购买成功，消费：%s,您的余额：%s' % (
                    pname,
                    pprice,
                    userinfo[1]
                ))
            elif choice == 'q':
                total = 0
                print('您的购买列表')
                print('---------------------------------------------------')
                print('%-18s%-18s%-18s%-18s%-18s' % (
                    '编号',
                    '名字',
                    '价格',
                    '数量',
                    '总价',
                ))
                for i, v in enumerate(shopping_cart):
                    production = shopping_cart[v]
                    price = production['pprice']
                    count = production['count']
                    total += count*price
                    print('%-20s%-20s%-20s%-20s%-20s' % (
                        i,
                        v,
                        price,
                        count,
                        count * price,

                    ))
                print('---------------------------------------------------')
                print('您总共消费：%s，余额：%s' % (total,userinfo[1]))

                # 是否确认购买
                while tag:
                    choice0003 = input('是否购买（y/n）').strip()
                    if choice0003 not in ['y','n']:
                        print('输入非法')
                        continue
                    if choice0003 == 'y':
                        # 更改文件中用户的数据
                        with open(db_file,'r',encoding='utf-8') as fr,\
                            open(r'%s.swap' % db_file,'w',encoding='utf-8') as fw:
                            for line in fr:
                                user = line.strip('\n').split('|')
                                if userinfo[0] == user[0]:
                                    user[2] ='%s\n' % userinfo[1]
                                    line = '|'.join(user)
                                fw.write(line)
                        os.remove(db_file)
                        os.rename(r'%s.swap' % db_file,db_file)
                    userinfo=[]
                    shopping_cart={}
                    tag = False

            else:
                print('输入非法')
            # 商品购买
            # 判断用户输入
            # 判断用户余额是否足够   扣钱 添加购物车 重新显示列表
            # q 退出
            # 显示用户购买列表
            # 清空全局存的信息
        pass

    else:
        print('非法输入')
