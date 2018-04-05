# encoding: utf-8
# by fixdq


# 文件中数据格式
# 用户名|密码|余额|信用额度
# qwer|qwer|1400|15000
#
import os
import time

# 当前路径
path = os.getcwd()

product_list = [
    ['ipone', 8000],
    ['xiaomi', 2000],
    ['chuizi', 1500],
    ['car', 100],
    ['pen', 10],
]
# atm操作log
path_log_atm = r'%s%satm%satm.log' % (path, os.path.sep, os.path.sep)
# 用户流水log
path_log_users = r'%s%saccounts%s' % (path, os.path.sep, os.path.sep)
# 用户信息
path_db_users = r'%s%sdb_user.txt' % (path, os.path.sep)
# 锁定信息
path_db_lock = r'%s%sdb_lock.txt' % (path, os.path.sep)

# 默认信用额度
credit = 15000

# 当前登录用户
current_user = []

# 临时购物车
product_car = {}

# 首页信息
msg_home = '''
1.登录
2.注册
3.购物
4.ATM服务
'''
# Atm信息
msg_atm = '''
1.查询
2.取现
3.还款
4.转账
'''


# 记录atm操作日志
def atm_records_deco(operate):
    def atm_records(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            db_atm_records(operate)
            return res
        return wrapper
    return atm_records


# atm操作日志 写入
def db_atm_records(operate):
    uname = current_user[0]
    # 格式化成2018-04-01 11:45:39形式
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(path_log_atm, 'a', encoding='utf-8') as fw:
        fw.write('uname:%s__operate:%s__time:%s\n' % (
            uname, operate, current_time
        ))


# 记录用户流水日志
def user_records(func):
    def wrapper(*args, **kwargs):
        # 默认操作
        account = 'balance'
        mode = '-'
        if args:
            uname = args[0]
            money = args[1]
        if kwargs:
            for key in kwargs:
                if key == 'account':
                    account = kwargs['account']
                if key == 'mode':
                    mode = kwargs['mode']
        db_user_records(uname, money, account, mode)
        res = func(*args, **kwargs)
        return res

    return wrapper


# 用户流水log 写入
def db_user_records(uname, money, account, mode):
    # 格式化成2018-04-01 11:45:39形式
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(r'%s%s.log' % (path_log_users, uname), 'a', encoding='utf-8') as fw:
        fw.write('uname:%s__money:%s__account:%s__mode:%s__time:%s\n' %
                 (uname, money, account, mode, current_time))


# 用户认证装饰器
def auth(func):
    def wrapper(*args, **kwargs):
        # 判断用户是否通过认证
        if not current_user:
            # 用户没有登录
            print('请您先登录再进行相关操作！！！')
            login()
        res = func(*args, **kwargs)
        return res

    return wrapper


# 用户登录
def login():
    # 登录
    while True:
        global current_user
        uname = input('用户名：').strip()
        pwd = input('密码：').strip()
        if len(uname) == 0 or len(pwd) == 0:
            print('用户名和密码不能为空')
            continue
        if db_serch_user(uname, pwd):
            money = db_get_user_money(uname)
            user_credit = db_get_user_money(uname,account='credit')
            current_user = [uname, money, user_credit]
            print('登录成功')
            break
        else:
            print('用户名或密码错误！')


# 用户注册
def register():
    uname = get_uname()
    pwd = get_pwd()
    money = get_money()
    db_write_user(uname, pwd, money)
    print('注册成功')


# 获取用户名
def get_uname():
    while True:
        uname = input('请输入用户名：').strip()
        if len(uname) == 0:
            print('用户名不能为空')
            continue
        if not uname.isalpha():
            print('用户名必须为字母组成')
            continue
        # 验证用户名是否存在
        if db_serch_name(uname):
            print('用户名已存在')
        else:
            return uname


# 获取密码
def get_pwd():
    while True:
        pwd1 = input('请输入密码：').strip()
        pwd2 = input('请再次输入密码：').strip()
        if len(pwd1) == 0 or len(pwd2) == 0:
            print('密码不能为空')
            continue
        if pwd2 == pwd1:
            return pwd1
        else:
            print('两次密码输入不一致')


# 获取金额
def get_money():
    while True:
        balance = input('请输入充值金额：').strip()
        if len(balance) == 0:
            print('输入不能为空')
            continue
        if balance.isdigit():
            balance = int(balance)
            if balance < 0:
                print('金额输入不正确')
                continue
            else:
                return balance
        else:
            print('金额输入不正确')


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
    if pname in product_car:
        product_car[pname]['count'] += 1
    else:
        product_car[pname] = {'pprice': pprice, 'count': 1}
    # 扣钱
    current_user[2] -= pprice
    # 提示
    print(' %s 已经添加到购物车！～！' % pname)


# 结算
def shop_settle(product_car_list):
    while True:
        # 显示购物车信息
        totals = show_car_list(product_car)
        choice = input('%s你好，您一共消费了%s，是否够买(y/n)' % (current_user[0], totals))
        if len(choice) == 0:
            print('输入不能为空')
            continue
        if choice not in ['y', 'n']:
            print('输入不正确')
            continue
        if choice == 'y':
            # 确认购买
            # 更新用户余额 使用信用
            db_update_money(current_user[0], totals, account='credit', mode='-')
            print('结算成功！')

        break


# 购物
@auth
def shopping():
    global current_user, product_car
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
            if choice < 0 or choice > len(product_list):
                print('请正确输入您的选择！')
                continue
            production = product_list[choice]
            # 检测是否购买过
            pname = production[0]
            pprice = production[1]
            # 判断用户余额是否足够
            # 可用信用额度
            user_credit = current_user[2]
            if user_credit < pprice:
                print('您的信用额度不足，还有：%s' % user_credit)
                continue
            # 添加商品到购物车
            car_add(pname, pprice)
        elif choice == 'q':
            if not product_car:
                break
            # 结算
            shop_settle(product_car)
            # 清空本地临时数据
            current_user = []
            product_car = {}
            break


# 查看用户信息
@atm_records_deco(operate='查询')
@auth
def show_user_info():
    userinfos = db_get_user_money(current_user[0], account='all')
    print('尊敬的%s，余额：%s，信用额度：%s' % (
        current_user[0],
        userinfos[0],
        userinfos[1]))


# 转账
@atm_records_deco(operate='转账')
@auth
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
        if not db_serch_name(account_target):
            print('目标账户不存在')
            continue
        while tag:
            transfer_money = input('请输入转账金额：').strip()
            if len(transfer_money) == 0:
                print('金额不能为空！')
            if transfer_money.isdigit():
                transfer_money = int(transfer_money)
                current_user_balance = db_get_user_money(current_user[0])
                if transfer_money >= current_user_balance:
                    print('您的账户余额不足，余额为：%s' % current_user_balance)
                    continue
                else:
                    # 所有条件满足 账户转账
                    # 扣款账户    扣款
                    db_update_money(current_user[0], transfer_money)
                    # 目标账户    加钱
                    db_update_money(account_target, transfer_money, mode='+')
                    print('转账成功！')
                    tag = False
            else:
                print('金额输入不正确！')


# 还款
@atm_records_deco(operate='还款')
@auth
def pay_back():
    # 检测需要还款金额
    current_user_credit_money = db_get_user_money(current_user[0], account='credit')
    pay_back_money = credit - current_user_credit_money
    if pay_back_money <= 0:
        print('您的信用额度为%s，现在剩余%s，无需还款！' %
              (credit, current_user_credit_money))
    elif pay_back_money > 0:
        print('您的信用额度为%s，现在剩余%s，需还款%s' %
              (credit, current_user_credit_money, pay_back_money))
    while True:
        pay_inp = input('请输入还款额度：').strip()
        if len(pay_inp) == 0:
            print('输入不能为空！')
            continue
        if pay_inp.isdigit():
            pay_inp = int(pay_inp)
            # 检测账户余额是否足够
            balance = db_get_user_money(current_user[0])
            if pay_inp > balance:
                print('余额不足')
                continue
            else:
                # 余额账户扣钱
                db_update_money(current_user[0], pay_inp)
                # 信用账户加钱
                db_update_money(current_user[0], pay_inp, account='credit', mode='+')
                print("还款成功！")
                break
        else:
            print('输入不正确！')

    # 还款
    pass


# 取现
@atm_records_deco(operate='取现')
@auth
def with_draw():
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
            balance = db_get_user_money(current_user[0])
            if (money + charge_money) > balance:
                print('余额不足！')
                continue
            else:
                # 余额账户扣钱
                db_update_money(current_user[0], (money + charge_money))
                print('成功取款%s，手续费%s，余额%s' %
                      (money, charge_money, db_get_user_money(current_user[0])))
                break
        else:
            print('输入不正确！')


# 数据源相关操作
# 添加新用户
def db_write_user(uname, pwd, money):
    """
    添加新用户
    :param uname: 用户名
    :param pwd: 密码
    :param money:充值金额
    :return:None
    """
    with open(path_db_users, 'a', encoding='utf-8') as fw:
        fw.write('%s|%s|%s|%s\n' % (uname, pwd, money, credit))


# 根据用户名更新用户金额,信用额度
@user_records
def db_update_money(uname, money, account='balance', mode='-'):
    """

    :param uname: 用户名
    :param money: 变动金额
    :param account: 'balance' 余额账户， 'credit' 信用账户
    :param mode: '-' 扣钱操作， '+' 加钱操作
    :return:None
    """
    with open(path_db_users, 'r', encoding='utf-8') as fr, \
            open(r'%s.swap' % path_db_users, 'a', encoding='utf-8') as fw:
        for line in fr:
            user = line.strip('\n').split('|')
            if user[0] == uname:
                if account == 'balance':
                    if mode == '-':
                        money = int(user[2]) - money
                    elif mode == '+':
                        money = int(user[2]) + money
                    user[2] = '%s' % money
                elif account == 'credit':
                    if mode == '-':
                        money = int(user[3]) - money
                    elif mode == '+':
                        money = int(user[3]) + money
                    user[3] = '%s' % money

                line = '|'.join(user) + '\n'
            fw.write(line)

    os.remove(path_db_users)
    os.renames(r'%s.swap' % path_db_users, path_db_users)


# 验证用户名，密码
def db_serch_user(uname, pwd):
    """
    根据 uname，pwd  判断用户是否存在
    :param uname:用户名
    :param pwd: 密码
    :return:boolean
    """
    with open(path_db_users, 'r', encoding='utf-8') as fr:
        for line in fr:
            user = line.split('|')
            if uname == user[0] and pwd == user[1]:
                return True
        else:
            False


# 根据用户名，获取用户余额
def db_get_user_money(uname, account='balance'):
    """
    根据 uname 获取用户余额
    :param uname:用户名
    :param account: 'balance' 余额账户， 'credit' 信用账户,'all' 两个账户都返回
    :return:int
    """
    with open(path_db_users, 'r', encoding='utf-8') as fr:
        for line in fr:
            user = line.strip('\n').split('|')
            if uname == user[0]:
                if account == 'balance':
                    return int(user[2])
                elif account == 'credit':
                    return int(user[3])
                elif account == 'all':
                    return int(user[2]), int(user[3])


# 验证用户名是否存在
def db_serch_name(uname):
    """
    uname 存在 True   不存在  False
    :param uname:
    :return:boolean
    """
    with open(path_db_users, 'r', encoding='utf-8') as fr:
        for line in fr:
            user = line.split('|')
            if uname == user[0]:
                return True
        else:
            return False


# Atm服务
def atm():
    while True:
        print(msg_atm)
        inp = input('请选择您的服务(q:返回上一级)：').strip()
        if inp == '1':  # 查看
            show_user_info()
        elif inp == '2':  # 取现
            with_draw()
        elif inp == '3':  # 还款
            pay_back()
        elif inp == '4':  # 转账
            transfer()
        elif inp == 'q':
            break
        else:
            print('输入错误！')


# 入口程序
def main():
    while True:
        print(msg_home)
        inp = input('请选择您的服务(q:退出)：').strip()
        if inp == '1':
            login()
        elif inp == '2':
            register()
        elif inp == '3':
            shopping()
        elif inp == '4':
            atm()
        elif inp == 'q':
            break
        else:
            print('输入错误！')


main()
