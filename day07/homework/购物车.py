# encoding=utf-8
# #作业二：请闭眼写出购物车程序
# #需求:
# 用户名和密码存放于文件中，格式为：egon|egon123
# 启动程序后，先登录，登录成功则让用户输入工资,然后打印商品列表，失败则重新登录，超过三次则退出程序
# 允许用户根据商品编号购买商品
# 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
# 可随时退出，退出时，打印已购买商品和余额


msg_dic = [
    {'name': 'apple', 'price': 10},
    {'name': 'tesla', 'price': 100000},
    {'name': 'mac', 'price': 3000},
    {'name': 'lenovo', 'price': 30000},
    {'name': 'chicken', 'price': 10},
]

# #创建文件
# with open('user.txt','w',encoding='utf-8') as f:
#         f.write('egon|egon123')

# 输入 q 是退出
count = 0       # 错误登录次数
balance = 0     # 余额
goods = []      # 购物列表
flag = True     # 退出标记
while flag:
    if count == 3:
        print('登录次数太多了')
        break
    u_name = input('用户名：').strip()
    u_pwd = input('密码：').strip()
    with open('user.txt', 'r', encoding='utf-8') as f:
        for line in f:

            # 随时退出
            if not flag:
                break

            user = line.split('|')
            # 判断用户是否存在
            if u_name == user[0]:
                # 判断用户密码是否正确
                if u_pwd == user[1].strip('\n'):
                    print('登录成功')

                    # 用户工资输入与判断
                    while True:
                        salary = input('请输入工资：').strip()
                        if salary.isdigit():
                            balance = int(salary)
                            break
                        else:
                            print('工资输入不正确！')
                    # 用户购买商品
                    while True:
                        # 显示商品列表
                        for k, v in enumerate(msg_dic):
                            print('{id}--{name}----{price}'.format(
                                id=k + 1,
                                name=v['name'],
                                price=v['price'])
                            )
                        num = input('请输入商品编号：').strip()

                        # 随时退出
                        if num == 'q':
                            flag = False
                            # 显示已购买的商品
                            print('您的购物列表')
                            print('----------------------------------------')
                            for k, v in enumerate(goods):
                                print('{id}--{name}----{price}'.format(
                                    id=k + 1,
                                    name=v['name'],
                                    price=v['price'])
                                )
                            print('----------------------------------------')
                            print('您的余额：%s 元' % balance)
                            break

                        # 判断编号
                        if num.isdigit():
                            num = int(num)
                            # 判断编号是否在商品编号中
                            if num > 0 and num <= len(msg_dic):
                                price = msg_dic[num - 1]['price']
                                # 判断价格
                                if balance >= price:
                                    # 余额-价格
                                    balance = balance - price
                                    # 将商品存入 购物列表
                                    goods.append(msg_dic[num - 1])
                                else:
                                    print('\n您的余额不足！\n')
                                    continue
                                continue
                        print('商品输入不正确！')

                else:
                    print('密码不正确！')
                    count += 1
                    break
        else:
            count += 1
            print('用户名不存在')

