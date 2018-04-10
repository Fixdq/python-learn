from interface import user

user_data = {
    'name': None,
    'is_auth': False,
}


def login():
    """
     登录函数，密码输错三次锁定，用户名输错可以一直输入
    :return: 
    """
    print('登录')
    count = 0
    while True:
        name = input('请输入用户名>>：').strip()
        if 'q' == name: break
        user_dic = user.get_userinfo_interface(name)
        if count > 3:
            # 锁定用户
            user.lock_user(name)
            print('您尝试次数太多了，被锁定')
            break
        if user_dic:
            pwd = input('请输入密码：').strip()
            if pwd == user_dic['password'] and not user_dic['locked']:
                user_data['name'] = name
                user_data['is_auth'] = True
                print('登录成功！')
                break
            else:
                print('密码错误，或您已被锁定！')
                count += 1
                continue

        else:
            print('用户不存在')
            continue


def register():
    '''
    注册函数，登陆了不能继续注册，已存在的用户不能再次注册
    :return:
    '''
    if user_data['is_auth']:
        print('您已登录！')
        return
    print('注册：')
    while True:
        name = input('请输入用户名>>: ').strip()
        if 'q' == name: break
        user_dic = user.get_userinfo_interface(name)
        if user_dic:
            print('用户名已经存在！')
            continue
        else:
            pwd1 = input('请输入密码>>:').strip()
            pwd2 = input('请确认密码>>:').strip()
            if pwd1 == pwd2:
                user.register_user(name, pwd1)
                break
            else:
                print('两次密码输入不一致！')
                continue


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


func_dic = {'1': login,
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
        # for i in func_dic:
        #     print('%s  %s' % (i,func_dic[i].__name__))
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
        choice = input('choose>>: ').strip()
        if choice not in func_dic:
            continue
        func_dic[choice]()
