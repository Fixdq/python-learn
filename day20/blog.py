#!/usr/bin/env python3
# encoding: utf-8
# by fixdq



# class ParentClass1: # 定义父类1
#     pass
#
# class ParentClass2: # 定义父类2
#     pass
#
# class Subclass1(ParentClass1): # 单继承 父类一
#     pass
#
# class Subclass2(ParentClass1,ParentClass2):  # 多继承多个父类  父类1 父类2
#     pass
#
# print(Subclass1.__bases__)  # 查看所有父类信息
# print(Subclass2.__bases__)  # 查看所有父类信息


# # 父类
# class People:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#
# # 子类 "指名道姓" 调用父类的属性
# class Teacher(People):
#     def __init__(self, name, age, sex, level, salary):
#         People.__init__(self, name, age, sex)
#         super().__init__(name, age, sex)
#         self.level = level
#         self.salary = salary
#
#
# # 实例化
# tea1 = Teacher('fixd', 18, 'male', 9, 3.1)
# print(tea1.name, tea1.age, tea1.sex, tea1.level, tea1.salary)



#super()会严格按照mro列表从当前查找到的位置继续往后查找
class A:
    def test(self):
        print('A.test')
        super().f1()
class B:
    def f1(self):
        print('from B')
class C(A,B):
    pass

c=C()
print(C.mro()) #C->A->B->object


c.test()