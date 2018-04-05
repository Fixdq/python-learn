# encoding: utf-8
# by fixdq

import os
product_list=[
    ['ak ',1000],
    ['m16',2000],
    ['m14',3000],
    ['awm',4000],
    ['rpg',10000],

]
shopping_list=[] #定义变量存入用户值
shopping_list2={} #定义变量存入用户购买的商品名称价格数量
file='db.txt'
tag3=True

while tag3:
    print("""
    1.登录
    2.注册
    3.购物 
    4.退出程序
    """)

    num=input('请输入编号：').strip()

    if num=='1':
        count=0
        tag = True
        while tag:
            count+=1
            inp_name=input('请输入账号：').strip()
            inp_paw=input('请输入密码：').strip()

            with open(r'%s' %file,mode='r',encoding='utf-8') as f:
                for i in f:
                    a=i.split(',')
                    if inp_name==a[0] and inp_paw==a[1].strip('\n'):
                        print('登录成功')
                        print('账户:%s,余额:%s' %(a[0],a[2]),end='')
                        tag=False
                        shopping_list=[a[0],a[2]]
                        break
                else:
                    print('账号或密码错误！')
                    if count==3:
                        print('错误次数过多，退出。。。')
                        break

    elif num=='2':
        tag1=True
        while tag1:
            with open(r'%s' %file,mode='r',encoding='utf-8') as f1,\
                open(r'%s' %file,mode='a',encoding='utf-8') as f2:
                name=input('输入注册账户：').strip()
                for i in f1:
                    a = i.split(',')
                    if name == a[0]:
                        print('重复用户名请重新输入！')
                        break
                    paw=input('输入注册密码：').strip()
                    paw2=input('重复输入密码：').strip()
                    if not paw2==paw:
                        print('重复密码输入错误！请从新输入!')
                        continue
                    money=input('请输入购物资金：').strip()

                    f2.write('%s,%s,%s\n' %(name,paw,money))
                    print('注册成功！')
                    tag1=False
                    break

    elif num=='3':
        tag2 = True
        if len(shopping_list)==0:
            print('请登录购买！')
            break
        else:
            print('尊敬的用户%s,您的余额为%s,祝您购物愉快！' %(shopping_list[0],shopping_list[1]))
            nm3=shopping_list[0]
            money3=int(shopping_list[1])#定义余额变量
            while tag2:
                for x,y in enumerate(product_list):
                    print('商品编号：%s   商品名,单价：%s' %(x+1,y))
                num3=input('请输入商品编号，退出请输入q:').strip()
                if num3.isdigit():
                    num3=int(num3)
                    num3-=1
                    if num3<0 or num3>len(product_list):continue

                    name3=product_list[num3][0] #定义商品名变量
                    my3=product_list[num3][1] #定义商品价格变量

                    if money3 > product_list[num3][1]: #判断余额是不是大于商品价格
                        if name3 in shopping_list2:  #判断商品在不在商品购买列表中
                            shopping_list2[name3]['数量：']+=1
                        else:
                            shopping_list2[name3]={'价格：':my3,'数量：':1}


                        money3-=my3   #扣钱
                        shopping_list[1]=money3 #扣钱值返回到用户列表
                        print('用户：%s,您已购买商品%s,价格为%s，余额%s' %(shopping_list[0],name3,my3,money3))
                    else:
                        print('您的余额为%s,无法购买此商品，请重新选择购买！' %money3)

                elif num3=='q':
                    print('''
                    --------------------------已购买商品列表--------------------------
                    id          商品              数量          单价          总价                 
                    ''')
                    mus=0
                    for x,y in enumerate(shopping_list2):
                        print('%21s%14s%16s%15s%15s'
                              %(x+1,y,shopping_list2[y]['数量：'],shopping_list2[y]['价格：'],
                                shopping_list2[y]['数量：']*shopping_list2[y]['价格：']
                                )
                              )
                        mus+= shopping_list2[y]['数量：']*shopping_list2[y]['价格：']
                    print('''
                    您的总花费为：%s
                    您的余额为：%s
                    ----------------------------------------------------------------
                    ''' %(mus,money3))
                    file2='db2.txt'
                    while tag2:
                        yn=input('确认购买（yes/no）：').strip()
                        if yn not in ['Y','y','yes','N','n','no']:continue
                        if yn in ['Y','y','yes']:
                            with open(r'%s' %file,mode='r',encoding='utf-8') as f1,\
                                open(r'%s' %file2,mode='w',encoding='utf-8') as f2:
                                for i in f1:
                                    if i.startswith(nm3):
                                        qie=i.strip('\n').split(',')
                                        qie[2]=str(money3)
                                        i=','.join(qie)+'\n'
                                    f2.write(i)
                            os.remove(file)
                            os.rename(file2,file)
                            print('购买完成，请等待收货！')
                        shopping_list=[]
                        shopping_list2={}
                        tag2=False
                else:
                    print('请输入正确指令！')
    elif num=='4':
        tag3=False
        break
    else:
        print("请输入正确的指令！")