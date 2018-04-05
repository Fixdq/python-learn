# encoding: utf-8
# by fixdq
#

# 文件中用户信息格式
# uname|pwd|balance
path_db = r"db.txt"


# 用户名
def get_uname():
    while True:
        u_name = input("请输入用户名:").strip()
        if len(u_name) == 0:
            print('用户名不能为空')
            continue
        if not u_name.isalpha():
            print('用户名只能为字母')
            continue

        with open(path_db, 'r', encoding='utf-8') as f:
            for line in f:
                if u_name == line.split('|')[0]:
                    print('用户名已存在')
                    break
            else:
                return u_name


# 密码
def get_pwd():
    while True:
        pwd1 = input('请输入密码：').strip()
        pwd2 = input('再次输入密码：').strip()
        if len(pwd1) == 0:
            print('用户名不能为空')
            continue
        if pwd1 != pwd2:
            print('两次密码输入不一致')
            continue
        return pwd2
# 余额
def get_balance():
    while True:
        balance = input('请输入充值金额：')
        if len(balance) == 0:
            print('充值金额不能为空')
            continue
        if balance.isdigit():
            balance = int(balance)
            if balance <=0:
                print('充值金额输入不正确')
                continue
            else:
                return balance
        else:
            print('充值金额输入不正确')
            continue

# 文件写入
def db_write(uname, pwd, balance):
    with open(path_db,'a',encoding='utf-8') as f:
        f.write('%s|%s|%s\n' % (uname,pwd,balance))

    pass


# 注册
def register():
    uname = get_uname()
    pwd = get_pwd()
    balance = get_balance()
    db_write(uname, pwd, balance)
    print('注册成功！')

register()