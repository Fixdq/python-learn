# encoding: utf-8
# by fixdq


# 编写用户注册函数，实现功能
# 	1、在函数内接收用户输入的用户名、密码、余额
# 		要求用户输入的用户名必须为字符串，并且保证用户输入的用户名不与其他用户重复
# 		要求用户输入两次密码，确认输入一致
# 		要求用户输入的余额必须为数字
# 	2、要求注册的用户信息全部存放于文件中
#
#fixd|pwd|1332
db_path = r'/home/fixd/project/oldboy/day09/db.txt'
def register(uname,pwd,balance):
    user = '%s|%s|%s\n' % (uname,pwd,balance)
    with open(db_path,'a',encoding='utf-8') as f:
        f.write(user)
        return True
def validata():
    while True:
        uname = input('用户名：').strip()
        # 判断用户是否存在
        with open(db_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip('\n')
                u_list = line.split('|')
                if uname == u_list[0]:
                    print('用户已存在')
                    break
            else:
                while True:
                    pwd1 = input('新密码：').strip()
                    pwd2 = input('确认密码:').strip()
                    if pwd1 == pwd2:
                        break
                    else:
                        print('两次密码输入不一致')

                while True:
                    balance = input('请输入您的工资：').strip()
                    if balance == '':
                        print('输入不能为空')
                        continue
                    if balance.isdigit():
                        balance = int(balance)
                        if balance > 0:
                            return uname, pwd2, balance
                    else:
                        print('输入非法')

user_list = validata()
res = register(user_list[0],user_list[1],user_list[2])
if res:
    print('注册成功')

# 编写用户转账函数，实现功能
# 	1、传入源账户名（保证必须为str）、目标账户名（保证必须为str）、转账金额（保证必须为数字）
# 	2、实现源账户减钱，目标账户加钱
#

def transfer(u_out,u_in,u_money):
    u_out_balance = 0
    u_in_balance = 0

    # 判断用户账户余额是否足够
    with open(db_path,'r',encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')
            u_list = line.split('|')
            u_out_balance = u_list[3]
            if int(u_out_balance) >= u_money:
                # 可以转账
                break
            else:
                print('穷逼，就%s块钱，转毛' % u_out_balance)
                return False





# 编写用户验证函数，实现功能
# 	1、用户输入账号，密码，然后与文件中存放的账号密码验证
# 	2、同一账号输错密码三次则锁定
#
# 	3、这一项为选做功能：锁定的账号，在五分钟内无法再次登录
# 		提示：一旦用户锁定，则将用户名与当前时间写入文件,例如: egon:1522134383.29839
# 			实现方式如下：
#
# 			import test_time
#
# 			current_time=test_time.test_time()
# 			current_time=str(current_time) #当前的时间是浮点数，要存放于文件，需要转成字符串
# 			lock_user='%s:%s\n' %('egon',current_time)
#
# 			然后打开文件
# 			f.write(lock_user)
#
# 			以后再次执行用户验证功能，先判断用户输入的用户名是否是锁定的用户，如果是，再用当前时间time.test_time()减去锁定的用户名后
# 			的时间，如果得出的结果小于300秒，则直接终止函数，无法认证，否则就从文件中清除锁定的用户信息，并允许用户进行认证