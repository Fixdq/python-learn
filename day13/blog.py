# encoding: utf-8
# by fixdq


# def max2(x,y):
#     if x > y:
#         return x
#     else:
#         return y
#
# res=max2(10,11)
# print(res)
#
# x=12
# y=11

#三元表达式仅应用于：
#1、条件成立返回 一个值
#2、条件不成立返回 一个值
# res=x if x > y else y
# print(res)


# def max2(x,y):
#     return x if x > y else y
#
# print(max2(10,11))




# 直接调用
def foo():
    print('from foo')
    foo()

foo()

# 间接调用
def bar():
    print('from bar')
    foo()

def foo():
    print('from foo')
    bar()

foo()

# 递归分为两个阶段
#1、回溯:
    # 注意：一定要在满足某种条件结束回溯，否则的无限递归
#2、递推

# 总结：
#1、递归一定要有一个明确地结束条件
#2、没进入下一次递归，问题的规模都应该减少
#3、在python中没有尾递归优化


# age(5)=age(4)+2
# age)4)=age(3)+2
# age(3)=age(2)+2
# age(2)=age(1)+2
# age(1)=18

# age(n)=age(n-1)+2 # n > 1
# age(n)=18            #n=1
#

# def age(n):
#     if n == 1:
#         return 18
#     return age(n-1)+2 #age(4)+2
#
# age(5)



items=[1,[2,[3,[4,[5,[6,[7,[8,[9,[10,]]]]]]]]]]
def tell(l):
    for item in l:
        if type(item) is not list:
            print(item)
        else:
            tell(item)

tell(items)


