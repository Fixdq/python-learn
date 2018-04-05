# 1、python test.py执行的三个阶段是什么？在哪个阶段识别文件内的python语法？

    #1，启动解释器
    #2，将文件内容加载到内存
    #3，解释执行（这个过程中会检测代码的语法）


# 2、将下述两个变量的值交换

    # s1 = 'alex'
    # s2 = 'SB'
    # s1,s2 = s2,s1
    # print(s1,s2)

# 3、判断下述结果
    # msg1 = 'alex say my name is alex,my age is 73,my sex is female'
    # msg2 = 'alex say my name is alex,my age is 73,my sex is female'
    # msg1 is msg2      True
    # msg1 == msg2      False

# 4、什么是常量？在python中如何定义常量

    #不能改变的量
    #定义方式：字母全部大写
    #eg： ID_FIXD


# 5、有存放用户信息的列表如下，分别存放用户的名字、年龄、公司信息
# userinfo = {
#     'name': 'egon',
#     'age': 18,
#     'company_info': {
#         'cname': 'oldboy',
#         'addr': {
#             'country': 'China',
#             'city': 'Shanghai',
#         }
#     }
#
# }
# 要求取出该用户公司所在的城市

    # city = userinfo['company_info']['addr']['city']

# students = [
#     {'name': 'alex', 'age': 38, 'hobbies': ['play', 'sleep']},
#     {'name': 'egon', 'age': 18, 'hobbies': ['read', 'sleep']},
#     {'name': 'wupeiqi', 'age': 58, 'hobbies': ['music', 'read', 'sleep']},
# ]
# 取第二个学生的第二个爱好

    # hobby = students[1]['hobbies'][1]


# 6、
# students = [
#     {'name': 'egon', 'age': 18, 'sex': 'male'},
#     {'name': 'alex', 'age': 38, 'sex': 'fmale'},
#     {'name': 'wxx', 'age': 48, 'sex': 'male'},
#     {'name': 'yuanhao', 'age': 58, 'sex': 'fmale'},
#     {'name': 'liwenzhou', 'age': 68, 'sex': 'male'},]
#
# for item in students:
#     print("< name:%s\n age:%s\n sex:%s >"
#           %(item['name'],item['age'],item['sex']))
#

# 要求循环打印所有学生的详细信息，格式如下
# < name:egon
# age:18
# sex:male >
# < name:alex
# age:38
# sex:fmale >
# < name:wxx
# age:48
# sex:male >
# < name:yuanhao
# age:58
# sex:fmale >
# < name:liwenzhou
# age:68
# sex:male >
#
# 7、编写程序，  # 根据用户输入内容打印其权限
#
# '''
# egon --> 超级管理员
# tom  --> 普通管理员
# jack,rain --> 业务主管
# 其他 --> 普通用户
# '''


# name = input('username==>')
# if name == 'egon':
#     print('%s-->超级管理员' % name)
# elif name == 'tom':
#     print('%s-->普通管理员' % name)
# elif name == 'jack' or name == 'rain':
#     print('%s-->业务主管' % name)
# else:
#     print('%s-->普通用户' % name)


# 8、编写程序，实现如下功能
# 如果:今天是Monday,那么:上班
# 如果:今天是Tuesday,那么:上班
# 如果:今天是Wednesday,那么:上班
# 如果:今天是Thursday,那么:上班
# 如果:今天是Friday,那么:上班
# 如果:今天是Saturday,那么:出去浪
# 如果:今天是Sunday,那么:出去浪

# day = input("What day is today==>")
# while True:
#     if day == 'Monday'\
#             or day == 'Tuesday' \
#             or day == 'Wednesday' \
#             or day == 'Thursday' \
#             or day == 'Friday':
#         print('赶紧去上班！')
#     elif day == 'Saturday'\
#             or day == 'Sunday':
#         print('休息还不出去浪')
#     else:
#         print('您输入的不正确')

#
# # 9、while循环练习
# # 1. 使用while循环输出1 2 3 4 5 6 8 9 10
# c = 1
# while c <= 10:
#     print(c)
#     c += 1
#
# for i in range(1, 11):
#     print(i)
#
#
# # 2. 求1-100的所有数的和
# sum1 = 0
# c = 1
# while c <= 100:
#     sum1 += c
#     c += 1
# print('sum==>%s' % sum1)
#
# sum2 = 0
# for i in range(1, 101):
#     sum2 += i
# print('sum==>%s' % sum2)
#
#
# # 3. 输出 1-100 内的所有奇数
# c = 1
# while c <= 100:
#     if c % 2 != 0:
#         print(c)
#     c += 1
#
# for i in range(1,101):
#     if i % 2 != 0:
#         print(i)
#
#
# # 4. 输出 1-100 内的所有偶数
# c = 1
# while c <= 100:
#     if c % 2 == 0:
#         print(c)
#     c += 1
#
# for i in range(1,101):
#     if i % 2 == 0:
#         print(i)
#
#
# # 5. 求1-2+3-4+5 ... 99的所有数的和
sum = 0
c = 1
while c < 100:
    if c % 2 == 0:
        sum -= c
    else:
        sum += c
    c += 1
print('sum==>%s' %sum)

# sum1=0
# for i in range(1,100):
#     if i % 2 == 0:
#         sum1 -= i
#     else:
#         sum1 += i
# print('sum==>%s' % sum1)

# 6. 用户登陆（三次机会重试）
# name = 'a'
# pwd = 'b'
# c = 0
# while True:
#     if c == 3:
#         print('sorry,login too many times')
#         break
#     in_name = input('username==>')
#     in_pwd = input('password==>')
#     if name == in_name and pwd == in_pwd:
#         print('login success')
#         break
#     else:
#         print('Username or password incorrect')
#     c += 1

# 7：猜年龄游戏
# 要求：
# 允许用户最多尝试3次，3
# 次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出

# c = 0
# age = 50
# while True:
#     if c == 3:
#         print('您猜的次数太多了。')
#         break
#     in_age = input('age==>')
#     if age == int(in_age):
#         print('恭喜您，猜对了')
#         break
#     else:
#         print('没猜对，继续努力！')
#     c += 1

# # 8：猜年龄游戏升级版
# 要求：
# 允许用户最多尝试3次
# 每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
# 如何猜对了，就直接退出

c = 0
age = 50
while True:
    if c == 3:
        choice = input('是否还想继续（继续Y/y,退出N/n）')
        if choice == 'Y' or choice == 'y':
            print('新的开始，加油吧')
            c = 0
            continue
        elif choice == 'N' or choice == 'n':
            break
        else:
            print('输入错误。')
            continue


    in_age = input('age==>')
    if age == int(in_age):
        print('恭喜您，猜对了')
        break
    else:
        print('没猜对，继续努力！')
    c += 1



# 10、编写计算器程序，要求
# 1、用户输入quit则退出程序
# 2、程序运行，让用户选择具体的计算操作是加法or乘法or除法。。。然后输入数字进行运算
# 3、简单示范如下，可以在这基础上进行改进
# while True:
#     msg = '''
# 		    1 加法
# 		    2 减法
# 		    3 乘法
# 		    4 除法
# 		    '''
#     print(msg)
#     choice = input('>>: ').strip()
#     num1 = input('输入第一个数字：').strip()
#     num2 = input('输入第二个数字：').strip()
#     if choice == '1':
#         res = int(num1) + int(num2)
#         print('%s+%s=%s' % (num1, num2, res))
#
# msg = '''
# 1 加法
# 2 减法
# 3 乘法
# 4 除法
# '''
# tag = True
# while tag:
#     print(msg)
#
#     choice = input('请选择操作：').strip()
#     if choice == '1':
#         print('加法----------------')
#     elif choice == '2':
#         print('减法----------------')
#     elif choice == '3':
#         print('乘法----------------')
#     elif choice == '4':
#         print('除法----------------')
#     else:
#         print('您的输出不正确！，请重新选择：')
#         continue
#     num1 = input('输入第一个数字：').strip()
#     num2 = input('输入第二个数字：').strip()
#     res = 0
#     if choice == '1':
#         res = int(num1) + int(num2)
#         print('%s+%s=%s' % (num1, num2, res))
#     elif choice == '2':
#         res = int(num1) - int(num2)
#         print('%s-%s=%s' % (num1, num2, res))
#     elif choice == '3':
#         res = int(num1) * int(num2)
#         print('%s*%s=%s' % (num1, num2, res))
#     elif choice == '4':
#         res = int(num1) / int(num2)
#         print('%s/%s=%s' % (num1, num2, res))
#
#     is_quit = input('继续任意键,退出（quit）').strip()
#     if is_quit == "quit":
#         break

# 11、选择题，预习字符串内置方法，做如下练习题
# 写代码,有如下变量,请按照要求实现每个功能 （共6分，每小题各0.5分）
name = " Fixd "
# 1)    移除 name 变量对应的值两边的空格,并输出处理结果
name = name.strip()
print(name)
# 2)    判断 name 变量对应的值是否以 "al" 开头,并输出结果 
print(name.startswith('al'))
# 3)    判断 name 变量对应的值是否以 "X" 结尾,并输出结果 
print(name.endswith('X'))
# 4)    将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
print(name.replace('l','p'))
# 5)    将 name 变量对应的值根据 “l” 分割,并输出结果。
print(name.split('l'))
# 6)    将 name 变量对应的值变大写,并输出结果 
print(name.upper())
# 7)    将 name 变量对应的值变小写,并输出结果 
print(name.lower())
# 8)    请输出 name 变量对应的值的第 2 个字符?
print(name[1])
# 9)    请输出 name 变量对应的值的前 3 个字符?
print(name[0:3])
# 10)    请输出 name 变量对应的值的后 2 个字符? 
print(name[-2:])
# 11)    请输出 name 变量对应的值中 “e” 所在索引位置? 
print(name.index('e'))
# 12)    获取子序列,去掉最后一个字符。如: oldboy 则获取 oldbo。
print(name[:-1])
