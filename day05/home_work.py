# 作业
# 一、元组
#     1、列表与元组的区别的是什么
        #列表可变类型，可以读取，修改，添加数据
        #是不可变类型，只可以读取，不支持修改添加


#
# 二、for循环练习
#     1、循环取字符串、元组、列表内的元素，要求既取索引又取值
#字符串
str = '循环取字符串'
for i in range(len(str)):
    print(i,str[i])
for i, v in enumerate(str):
    print(i,v)

tup = ('循环','取字符串','元组','列表内的元素')
for i in range(len(tup)):
    print(i,tup[i])
for i, v in enumerate(tup):
    print(i,v)

lis= ['yite','fixd','yangli','al',]
for i in range(len(lis)):
    print(i,lis[i])
for i, v in enumerate(lis):
    print(i,v)


#     2、下面程序的执行结果是？并加以解释？
#         for item in enumerate({'name':'egon','age':18,'sex':'male'}):
#             print(item)
for item in enumerate({'name':'egon','age':18,'sex':'male'}):
    print(item)
#结果
# (0, 'name')
# (1, 'age')
# (2, 'sex')
#使用enmerate()内置函数，获得的对应元素的 索引值 和 key值

# 三、简单购物车,要求如下：（明天默写的代码）
#     实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入　　
#
#     msg_dic={
#     'apple':10,
#     'tesla':100000,
#     'mac':3000,
#     'lenovo':30000,
#     'chicken':10,
#     }
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}
goods=[]
while True:
    for item in msg_dic:
        print('名称：%s 价格：%s' % (item,msg_dic[item]))
    g_name = input('商品名称：').strip()
    if g_name not in msg_dic:
        print('名称输入的不正确，重新输入')
        continue
    price = msg_dic[g_name]
    while True:
        g_count = input('购买数量：').strip()
        if g_count.isdigit():
            g_count = int(g_count)
            break
        else:
            print('请正确输入数量：')
    info={
        'g_name':g_name,
        'price':price,
        'count':g_count,
    }
    goods.append(info)
    print(goods)




#
# 四、字典练习
#     1、字典是有序还是无序的
#           字典是无序的
#     2、有如下字典，要求循环取出字典中的key和value，用三种不同方式实现
#             msg_dic={
#             'apple':10,
#             'tesla':100000,
#             'mac':3000,
#             'lenovo':30000,
#             'chicken':10,
#             }
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}

for i in msg_dic:
    print(i,msg_dic[i])

for k in msg_dic.keys():
    print(k,msg_dic[k])

for k,v in msg_dic.items():
    print(k,v)




#     3、对于上述字典msg_dic,如果我想根据key来取对应的值，在值不存在的情况下会抛出异常KeyError，如何避免该问题？
        #使用 dict.get()方法
#     4、有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中
#     即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
list =  [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
dt = {'k1':[],'k2':[]}
for i in list:
    if i < 66:
        dt['k1'].append(i)
    if i >66:
        dt['k2'].append(i)
print(dt['k1'])
print(dt['k2'])

#     5、统计s='hello alex alex say hello sb sb'中每个单词的个数
#         结果如：{'hello': 2, 'alex': 2, 'say': 1, 'sb': 2}
s='hello alex alex say hello sb sb'
stus = s.split(' ')
dt = {}
for item in stus:
    dt.setdefault(item,stus.count(item))
print(dt)

# 五、集合练习（学完集合后做）
# 　一.关系运算
# 　　有如下两个集合，pythons是报名python课程的学员名字集合，linuxs是报名linux课程的学员名字集合
pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
linuxs={'wupeiqi','oldboy','gangdan'}
# 　　1. 求出即报名python又报名linux课程的学员名字集合
res = pythons & linuxs
print(res)
# 　　2. 求出所有报名的学生名字集合
res = pythons | linuxs
print(res)
# 　　3. 求出只报名python课程的学员名字
res = pythons - linuxs
print(res)
# 　　4. 求出没有同时这两门课程的学员名字集合
res = pythons ^ linuxs
print(res)
#
# 　二.去重（选做题）
# 　　 1. 有列表l=['a','b',1,'a','a']，列表元素均为可hash类型，去重，得到新列表,且新列表无需保持列表原来的顺序
l = ['a','b',1,'a','a']
l_new = []
for item in set(l):
    l_new.append(item)
print(l_new)
# 　　 2.在上题的基础上，保存列表原来的顺序
l = ['a','b',1,'a','a']
l_new = []
temp = set()
for item in l:
    if item not in temp:
        temp.add(item)
        l_new.append(item)
print(l_new)


# 　　 3.去除文件中重复的行，肯定要保持文件内容的顺序不变
# 　　 4.有如下列表，列表元素为不可hash类型，去重，得到新列表，且新列表一定要保持列表原来的顺序
#         l=[
#             {'name':'egon','age':18,'sex':'male'},
#             {'name':'alex','age':73,'sex':'male'},
#             {'name':'egon','age':20,'sex':'female'},
#             {'name':'egon','age':18,'sex':'male'},
#             {'name':'egon','age':18,'sex':'male'},
#         ]　　




