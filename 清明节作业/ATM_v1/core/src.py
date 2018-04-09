from interface import user

def login():
    pass

def register():
    '''
    注册函数，登陆了不能继续注册，已存在的用户不能再次注册
    :return:
    '''
    print('注册：')
    while True:
        name=input('please input username>>: ').strip()
        user_dic=user.get_userinfo_interface(name)
        if user_dic:
            print('user is exist')
            continue
        else:
            print('准备注册，即写入文件')

def check_balance():
    pass

def transfer():
    pass

def repay():
    pass

def withdraw():
    pass

def check_records():
    pass

def shopping():
    pass

def check_shopping_cart():
    pass

func_dic={'1':login,
'2': register,
'3': check_balance,
'4': transfer,
'5': repay,
'6': withdraw,
'7': check_records,
'8': shopping,
'9': check_shopping_cart
}


def run():
    while True:
        print('''
        1 login
        2 register
        3 check_balance
        4 transfer
        5 repay
        6 withdraw
        7 check_records
        8 shopping
        9 check_shopping_cart  
        ''')
        choice=input('choose>>: ').strip()
        if choice not in func_dic:
            continue
        func_dic[choice]()
