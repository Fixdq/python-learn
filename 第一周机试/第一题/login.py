# encoding: utf-8
# by fixdq


users = [
    {'name':'fixd','pwd':'123'},
    {'name':'aaa','pwd':'123'}
]
count = 0
path_lock_file = r"lock.txt"
tag = True
while tag:
    uname = input("用户名：").strip()
    pwd = input("密码：").strip()
    with open(path_lock_file,'r',encoding='utf8') as f:
        for line in f:
            line = line.strip('\n')
            if uname == line:
                print('您已被锁定')
                tag = False
                break
        else:
            for item in users:
                if uname == item['name'] and pwd == item['pwd']:
                    print('login success')
                    tag =False
                    break
            else:
                print("用户名密码错误")
                count += 1
            if count ==3:
                print('登录次数过多，被锁定')
                # 写入文件
                with open(path_lock_file,'a',encoding='utf8') as f:
                    f.write('%s\n' % uname)
                    tag = False