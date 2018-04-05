# encoding: utf-8
# by fixdq

def login():
    print('login ..')


def pay():
    print('pay..')


def checkin():
    print('checkin')


dic = {'1': login, '2': pay, '3': checkin}


def interactive():
    while True:
        print('''
        1 login
        2 pay
        3 checkin
        ''')
        choice = input('choose the no:')
        if choice in dic:
            dic[choice]()
        else:
            print('error')


interactive()
