#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


# 定义一个People类
class People:
    country = 'China'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def run(self):
        print('%s is running' % self.name)

# 实例化三个对象
people1 = People('fixd01', 18, 'male')
people2 = People('fixd02', 25, 'male')
people3 = People('fixd03', 30, 'male')
# 调用 run（）方法
people1.run()
people2.run()
people3.run()
# 查看run 的内存地址
print(people1.run)
print(people2.run)
print(people3.run)
#

# 实例化三个对象
people1 = People('fixd01', 18, 'male')
people2 = People('fixd02', 25, 'male')
people3 = People('fixd03', 30, 'male')

# 查看country属性对应的 内存地址
print(id(People.country))
print(id(people1.country))
print(id(people2.country))
print(id(people2.country))



# # 实例化一个对象  obj
# obj = People('fixd',18,'male')
#
#
# print(obj.name) #查看 属性name的值
# obj.education='哈佛'  # 添加属性
# del obj.name    # 删除属性
# obj.age=19      # 修改属性值
# print(obj.__dict__) # 查看实例化对象的名称空间
