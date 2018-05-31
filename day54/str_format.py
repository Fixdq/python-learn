#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-31 下午2:51
# @Author  : fixdq
# @File    : str_format.py
# @Software: PyCharm


# % 和format的区别
c = (233, 132)
# print('敌人现在的位置%s' % c)
print('敌人现在的位置%s' % [c])
print(''.format())
print('常规用法'.center(50, '-'))
# format 的常见用法
l1 = ['pangzi', 20]

print('他的名字{}，年龄{}'.format(l1[0], l1[1]))
print('他的名字{}，年龄{}'.format(*l1))
print('他的名字{0}，年龄{1}'.format(*l1))
print('他的名字{0[0]}，年龄{0[1]}'.format(l1))
print('他的名字{v[0]}，年龄{v[1]}'.format(v=l1))

print('关键字用法'.center(50, '-'))

# 关键字用法
d1 = {'name': 'pangzi', 'age': 20}
print('他的名字{}，年龄{}'.format(d1['name'], d1['age']))
print('他的名字{0}，年龄{1}'.format(d1['name'], d1['age']))
print('他的名字{name}，年龄{age}'.format(**d1))
print('他的名字{0[name]}，年龄{0[age]}'.format(d1))
print('他的名字{v[name]}，年龄{v[age]}'.format(v=d1))

print('通过对象属性'.center(50, '-'))

# 通过对象属性

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '[{self.name}-{self.age}]'.format(self=self)


p = Person('vs', 90)
print(p)

print('通过下标'.center(50, '-'))
# 通过下标
l2 = ['pz', 18]
print('他的名字{}，年龄{}'.format(l2[0], l2[1]))
print('他的名字{0}，年龄{1},{0}有点傻'.format(l2[0], l2[1]))
print('他的名字{0[0]}，年龄{0[1]},{0[0]}有点傻'.format(l2))

print('填充和对齐'.center(50, '-'))
# 填充与对齐
print('FIXD'.center(30,'^'))

# 左填充
print('{:#>20},{:#>20}'.format('FIXD','qewe'))
print('{:>20}'.format('FIXD'))


# 右填充
print('{:#<20}'.format('FIXD'))

# 内容居中
print('{:#^20}'.format('FIXD'))

print('FIXD'.zfill(10))

print("{:.2f}".format(3.141592653))
print("{:b}".format(10))
print("{:d}".format(10))
print("{:o}".format(10))
print("{:x}".format(10))


print("{:,}".format(1000000000))

