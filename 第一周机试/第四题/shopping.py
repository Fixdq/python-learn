# encoding: utf-8
# by fixdq
import os

product_list = [
    ['ipone', 8000],
    ['xiaomi', 2000],
    ['chuizi', 1500],
    ['car', 100],
    ['pen', 10],
]
userinfo = []
product_car = {}
path_db = r'db.txt'
msg = '''
1.注册
2.登录
3.购物
'''

while True:
    print(msg)

    choice = input('请选择您的操作：').strip()
    if choice == '1':
        # 注册
        tag = True
        while tag:
            uname = input('请输入用户名：').strip()
            if len(uname) == 0:
                print('用户名不能为空！')
                continue
            if not uname.isalpha():
                print('用户名不必须为字母！')
                continue
            with open(path_db, 'r', encoding='utf-8') as f:
                for line in f:
                    if uname == line.split('|')[0]:
                        print('用户名已经存在了')
                        break
                else:
                    while tag:
                        # 用户名不存在  验证密码
                        pwd1 = input('请输入密码：').strip()
                        pwd2 = input('请确认密码：').strip()
                        if len(pwd1) == 0 or len(pwd2) == 0:
                            print('密码不能为空')
                            continue
                        if pwd1 == pwd2:
                            # 输入充值金额验证
                            while tag:
                                balance = input('请输入充值金额:').strip()
                                if len(balance) == 0:
                                    print('金额不能为空')
                                    continue
                                if balance.isdigit():
                                    balance = int(balance)
                                    if balance < 0:
                                        print("您输入的金额有误！")
                                        continue
                                    else:
                                        # 存入用户信息
                                        with open(path_db, 'a', encoding='utf-8') as fw:
                                            fw.write('%s|%s|%s\n' % (uname, pwd1, balance))
                                            print('注册成功！')
                                            tag = False
                                            break
                                else:
                                    print("您输入的金额有误！")
                        else:
                            print('两次密码输入不一致')

    elif choice == '2':
        # 登录
        tag = True
        while tag:
            uname = input('用户名：').strip()
            pwd = input('密码：').strip()
            if len(uname) == 0 or len(pwd) == 0:
                print('用户名和密码不能为空')
                continue
            with open(path_db, 'r', encoding='utf-8') as fr:
                for line in fr:
                    user = line.strip('\n').split('|')
                    balance = int(user[2])
                    if uname == user[0] and pwd == user[1]:
                        # 登录成功 保存用户信息
                        userinfo = [uname, balance]
                        print('-----------------------------------')
                        print('登录成功！')
                        print('-----------------------------------')
                        tag = False
                        break
                else:
                    print('用户名或密码错误～！～！～！')

    elif choice == '3':
        # 验证
        if not userinfo:
            print('请先登录！！！！')
            continue
        tag = True
        while tag:
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
            print('%s你好，您的余额为：%s' % (userinfo[0], userinfo[1]))
            print('--------------------------------------')

            # 开始买了

            choice11 = input('请输入商品编号购买（q退出）：').strip()
            if len(choice11) == 0:
                print('请正确输入您的选择！')
                continue
            if choice11.isdigit():
                choice11 = int(choice11)
                if choice11 >= 0 and choice11 < len(product_list):
                    production = product_list[choice11]
                    # 检测是否购买过
                    pname = production[0]
                    pprice = production[1]
                    # 判断用户余额是否足够
                    if userinfo[1] < pprice:
                        print('您的余额不足，还有：%s' % userinfo[1])
                        continue
                    if pname in product_car:
                        product_car[pname]['count'] += 1
                    else:
                        product_car[pname] = {'pprice': pprice, 'count': 1}

                    # 扣钱
                    userinfo[1] -= pprice

                    # 提示
                    print(' %s 已经添加到购物车！～！' % pname)
                else:
                    print('请正确输入您的选择！')
                    continue
            elif choice11 == 'q':
                # 退出操作
                while tag:
                    # 显示购物车信息
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
                    while tag:
                        choice22 = input('%s你好，您一共消费了%s，是否够买(y/n)' % (userinfo[0], totals))
                        if len(choice22) == 0:
                            print('输入不能为空')
                            continue
                        if choice22 not in ['y', 'n']:
                            print('输入不正确')
                            continue
                        if choice22 == 'y':
                            # 确认购买，修改用户信息
                            # 修改db.txt数据
                            with open(path_db, 'r', encoding='utf-8') as fr, \
                                    open(r'%s.swap' % path_db, 'w', encoding='utf-8') as fw:
                                for line in fr:
                                    user = line.split('|')
                                    if user[0] == userinfo[0]:
                                        user[2] = '%s\n' % userinfo[1]
                                        line = '|'.join(user)
                                    fw.write(line)
                                os.remove(path_db)
                                os.renames(r'%s.swap' % path_db, path_db)
                                print('结算成功！')
                        # 退回首页
                        # 清空本地临时数据
                        userinfo = []
                        product_car = {}
                        tag = False
                        break

            else:
                print('请正确输入您的选择！')
    else:
        print('你的选择不正确！！')
