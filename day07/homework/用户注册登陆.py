while True:
    msg='''
    1，注册
    2，查看
    '''
    print(msg)   # 打印信息
    choice = input('请选择你的操作：').strip()
    if choice == '1':
        phone = input('手机号：').strip()
        name = input('名字：').strip()
        pwd = input('密码：').strip()
        sex = input('性别：').strip()
        with open('db.txt','a',encoding='utf-8') as f:
            f.write('%s,%s,%s,%s\n' %(phone,name,pwd,sex))
    elif choice == '2':
        #根据phone查询用户的信息
        phone = input('你的手机号:').strip()
        with open('db.txt','r',encoding='utf-8') as f:
            for line in f:
                if line.startswith(phone):
                    print(line,end='')
                    break

    else:
        print('你输入的不正确，重新输入')
