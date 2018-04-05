# encoding: utf-8
# by fixdq

users = [
    {'name': 'fixd', 'pwd': '123456'},
    {'name': 'fixd1', 'pwd': '789'},
]
path_lock = r'lock_name.txt'
count = 0
tag = True
while tag:
    uname = input('username:').strip()
    with open(path_lock, 'r', encoding='utf-8')as f:
        for line in f:
            if uname == line.strip('\n'):
                print('您被锁定了，退出！')
                break
        else:
            pwd = input('password:').strip()
            for user in users:
                if uname == user['name'] and pwd == user['pwd']:
                    print('登录成功')
                    tag = False
                    break
            else:
                print('验证失败')
                count += 1
    if count == 3:
        print('输入错误3次，退出！')
        with open(path_lock, 'a', encoding='utf-8') as f:
            f.write(uname)
            break
