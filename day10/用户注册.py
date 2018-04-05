# encoding: utf-8
# by fixdq
path_db = r"db.txt"

def get_uname():
    while True:
        uname = input('请输入用户名：').strip()
        if len(uname)==0:
            print('用户名不能为空')
            continue
        if not uname.isalpha():
            print('用户名必须为字母组成')
            continue
        with open(path_db,'r',encoding='utf-8') as f:
            for line in f:
                if uname == line.split("|")[0]:
                    print('用户已存在')
                    break
            else:
                return uname

def get_pwd():
    while True:
        pwd1 = input('请输入密码：').strip()
        pwd2 = input('请再次输入密码：').strip()
        if len(pwd1) == 0:
            print('密码不能为空')
            continue
        if pwd2 == pwd1:
            return pwd1
        else:
            print('两次密码输入不一致')

def get_balance():
    while True:
        balance = input('请输入充值金额：').strip()
        if len(balance)==0:
            print('输入不能为空')
            continue
        if balance.isdigit():
            balance = int(balance)
            if balance<0:
                print('金额输入不正确')
                continue
            else:
                return balance
        else:
            print('金额输入不正确')
def db_write(uanme,pwd,balance):
    with open(path_db,'a',encoding='utf-8') as f:
        f.write('%s|%s|%s\n' % (uanme,pwd,balance))

def register():
    uname = get_uname()
    pwd = get_pwd()
    balance = get_balance()
    db_write(uname,pwd,balance)
    print('注册成功')

register()