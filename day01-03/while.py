# count = 0
# tag = True
# while tag:
#     print(count)
#     if count > 5:
#         while tag:
#             print(count)
#             if count == 15:
#                 tag = False
#                 break
#             count += 1
#     count += 1
# else:
#     print('else')

# count = 0
# while count < 10:
#         if count == 5:  #count 值
#             break
#         print('循环正在运行中')
#         count += 1
# else:
#         print('循环终止了')
#
# count = 0
# while count <5:
#
#         if count == 3:  # count 值
#              break
#         print('循环正在运行中')
#         count+=1
# else:
#         print('循环终止了')

#
# description = '他是一个非常 "帅" 的小伙'              #双引号在内，单引号在外
# print(description)
#
# description = "他是一个非常 '帅' 的小伙"              #单引号在内，双引号在外
# print(description)
#
# description = """她的朋友说："他是一个非常 '帅' 的小伙"
# """
# print(description)                                  #单双引号在内，三引号在外

# str = 'abcdefg'
# print(str[:])
# print(str[2:])
# print(str[:4])
# print(str[2:4])
# print(str[1:4:2])
# print(str[-3:])  #提取后三位
# print(str[-1:])  #提取最后一位
# print(str[::-1]) #字符串反转
#
#
# str = "他的名字叫{name},年龄{age}".format(name='aaa',age=222)
# print(str)
#
# age = 20
# while True:
#     in_age = input('age==>')
#     if in_age.isdigit():
#         in_age = int(in_age)
#         if age == in_age:
#             print('恭喜您猜对了')
#             break
#         else:
#             print('猜错了')
#             continue
#     else:
#         print('您输入的不是数字')
#
# strs = ['aaaaa','bb','vv','cc','gh']
#
# print(strs)
# res0 = strs.append('pppppppppp')
# print(res0)
# print(strs)
# res1 = strs.remove('cc')
# print(res1)
# print(strs)
# res2 = strs.pop()
# print(res2)
#

#使用 %s 占位符的方式
# str = 'my name is %s,my age is %s' % ('Fixd',18)
# print(str)

#format的三种玩法
#使用 {} 占位符的方式
#format 参数个数 == 占位符个数
# str = 'my name is {},my age is {}'.format('Fixd',18) #一般的使用方法
# print(str)
#
# #format 参数个数 > 占位符个数
# str = 'my name is {},my age is {}'.format('Fixd',18,25,'yite')  #多余的参数不会显示，但不会报错
# print(str)
#
# #format 参数个数 < 占位符个数
# str = 'my name is {},my age is {}'.format('Fixd')   #这种情况就会报错
# print(str)


#使用 {索引} 占位符的方式

#format 对应参数
# str = 'my name is {0},my age is {1}'.format('Fixd',18)
# print(str)
# #format 多个参数，可根据索引取对应的参数
# str = 'my name is {0},my age is {1}'.format('Fixd',18,45,'yite')
# print(str)
# str = 'my name is {3},my age is {2}'.format('Fixd',18,25,'yite')
# print(str)


#format 对应参数
# str = 'my name is {name},my age is {age}'.format(name= 'Fixd',age = 18)
# print(str)


# 1--字母处理：
# str = 'aBcDef'
# print(str.upper())    # 全部大写
# print(str.lower())    # 全部小写
# print(str.swapcase())   # 大小写互换
# s = "this is a test string"
# print(s.capitalize())    # 首字母大写，其余小写
# print(s.title())    # 首字母大写
#
# str = 'linux:bin:etc'
# l = str.split(':')
# print(l)
# res = ''.join(l)
# print(res)
# res = ':'.join(l)
# print(res)

# old_str = ['name','jpg','rwx']
# new_str = ':'.join(old_str)
# print(new_str)

#5、is数字系列
num1=b'4' #bytes
num2=u'4' #unicode,python3中无需加u就是unicode
num3=u'肆' #中文数字
num4=u'Ⅳ' #罗马数字

# isdigit():bytes,unicode的阿拉伯数字
print(num1.isdigit())
print(num2.isdigit())
print(num3.isdigit())
print(num4.isdigit(),'\n')

# isdecimal():unicode的阿拉伯数字
print(num2.isdecimal())
print(num3.isdecimal())
print(num4.isdecimal(),'\n')

# isnumberic:unicode的阿拉伯数字\中文数字\罗马数字
print(num2.isnumeric())
print(num3.isnumeric())
print(num4.isnumeric())