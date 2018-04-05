# encoding: utf-8
# by fixdq

path_db = r'db.txt'
list_stu = []

with open(path_db, 'r', encoding='utf-8') as f:
    for line in f:
        stu = line.strip('\n').split(' ')
        name = stu[0]
        sex = stu[1]
        age = stu[2]
        salary = stu[3]
        stu_dict = {'name': name, 'sex': sex, 'age': age, 'salary': salary}
        list_stu.append(stu_dict)

# 2 根据1得到的列表,取出薪资最高的人的信息

res = max(list_stu, key=lambda x: x['salary'])
print(res)
# 3 根据1得到的列表,取出最年轻的人的信息
res = min(list_stu, key=lambda x: x['age'])
print(res)
# 4 根据1得到的列表,将每个人的信息中的名字映射成首字母大写的形式
res = map(lambda x: x['name'].capitalize(), list_stu)
print(list(res))
# 5 根据1得到的列表,过滤掉名字以a开头的人的信息
res = filter(lambda x: not x['name'].startswith('a'), list_stu)
print(list(res))


# 6 使用递归打印斐波那契数列(前两个#注意：内置函数id()可以返回一个对象的身份，
# 返回值为整数。这个整数通常对应与该对象在内存中的位置，但这与python的具体实现有关，
# 不应该作为对身份的定义，即不够精准，最精准的还是以内存地址为准。is运算符用于比较两个对象的身份，
# 等号比较两个对象的值，
# 内置函数type()则返回一个对象的类型#更多内置函数：https://docs.python.org/3/library/functions.html?highlight=built#ascii 数的和得到第三个数，如：0 1 1 2 3 4 7...)

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#
# fib(10)

def fib(a, b, stop):
    if a > stop:
        return
    print(a, end='')
    fib(b, a + b, stop)


fib(0, 1, 10)

# 7 一个嵌套很多层的列表，如l=［1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]］，
# 用递归取出所有的值
l = [1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15]]]]]]]


def get_item(lists):
    for item in lists:
        if type(item) is not list:
            print(item)
        else:
            get_item(item)


get_item(l)
