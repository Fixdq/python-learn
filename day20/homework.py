#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


# 4
# 月12日作业
# 1、类的属性和对象的属性有什么区别?、
#  类的数据属性是共享的，所有的实例化对象都能使用
#  类的函数属性是绑定给对象的使用的，谁调用就把谁当做函数的第一属性传入函数


# 2、面向过程编程与面向对象编程的区别与应用场景?
# 面向过程：核心是过程，就是按照步骤，先干什么，再干什么，流水线一样的编程方式，机械性的思维方式
# 优点：复杂的问题流程化，进而简单化
# 缺点：牵一发动全身，不容易扩展
# 应用场景：不经常改动的应用    linux 内核
# 面向对象：上帝的思维，使用类和对象来是实现编程
# 优点: 提高程序的扩展性
# 缺点： 编程的复杂程度提高，可控性差，无法像面向过程一样精准的预测问题的处理流程与结果
# 应用场景：互联网软件，游戏，经常需求变动的应用

# 3、类和对象在内存中是如何保存的。
# 类在定义的时候，就会创建名称空间
# 对象在实例化的时候，创建名称空间
# 对象的名称空间，可以使用类名称空间的名字

# 4、什么是绑定到对象的方法，、如何定义，如何调用，给谁用？有什么特性
# 对象调用类中定义的方法，
# 定义时必须添加一个参数
# 给对象调用的
# 绑定给谁就应该由谁来调用
# 谁调用就该把自身作为第一个参数传入
# 5、如下示例, 请用面向对象的形式优化以下代码

# 在没有学习类这个概念时，数据与功能是分离的, 如下
#
#
# def exc1(host, port, db, charset):
#     conn = connect(host, port, db, charset)
#
#
# conn.execute(sql)
# return xxx
#
#
# def exc2(host, port, db, charset, proc_name)
#     conn = connect(host, port, db, charset)
#
#
# conn.call_proc(sql)
# return xxx
# # 每次调用都需要重复传入一堆参数
# exc1('127.0.0.1', 3306, 'db1', 'utf8', 'select * from tb1;')
# exc2('127.0.0.1', 3306, 'db1', 'utf8', '存储过程的名字')
import pickle
from sqlite3 import connect


class Mysql:
    def __init__(self, host, port, db, charset):
        self.host = host
        self.port = port
        self.db = db
        self.charset = charset

    def get_conn(self):
        """
        返回数据连接对象
        :return: 
        """
        return connect(self.host, self.port, self.db, self.charset)


# 6、下面这段代码的输出结果将是什么？请解释。
# class Parent(object):
#     x = 1
#
#
# class Child1(Parent):
#     pass
#
#
# class Child2(Parent):
#     pass
#
#
# print(Parent.x, Child1.x, Child2.x)
# 全部 取得的是  基类的 x=1
# Child1.x = 2 给 Child1 添加 属性 x= 2
# print(Parent.x, Child1.x, Child2.x)
#
# Parent.x = 3 改修 基类属性  x= 3    不影响  Child1.x 的属性  子类中与父类中 重名的属性  以自身的属性为准
# print(Parent.x, Child1.x, Child2.x)
# 1,1,1，
# 121
# 323



# 7、多重继承的执行顺序，请解答以下输出结果是什么？并解释。
#
# class A(object):
#     def __init__(self):
#         print('A')
#         super(A, self).__init__()
#
#
# class B(object):
#     def __init__(self):
#         print('B')
#         super(B, self).__init__()
#
#
# class C(A):
#     def __init__(self):
#         print('C')
#         super(C, self).__init__()
#
#
# class D(A):
#     def __init__(self):
#         print('D')
#         super(D, self).__init__()
#
#
# class E(B, C):
#     def __init__(self):
#         print('E')
#         super(E, self).__init__()
#
#
# class F(C, B, D):
#     def __init__(self):
#         print('F')
#         super(F, self).__init__()
#
#
# class G(D, B):
#     def __init__(self):
#         print('G')
#         super(G, self).__init__()
#
#
# if __name__ == '__main__':
#     g = G()
#     f = F()
#
# GDAB
# FCABDA




# 8、什么是新式类，什么是经典类，二者有什么区别？什么是深度优先，什么是广度优先？


# 首先第一点是：新式类和经典类只有在Python2中有区分，python3全部为新式类
# 第二点是：python2中的新式类就是显示的继承object的类以及该类的子类
# python2的经典类没有显示继承object的类以及该类的子类
# python3只有新式类，默认继承object
#
#
# 在菱形继承的背景下
# 经典类 深度优先 名称空间的查找顺序 从当前类开始 到每条继承线的顶级类
# 新式类 广度优先

# 9、用面向对象的形式编写一个老师类, 老师有特征：编号、姓名、性别、年龄、等级、工资，老师类中有功能
# 1、生成老师唯一编号的功能，可以用hashlib对当前时间加上老师的所有信息进行校验得到一个hash值来作为老师的编号
#
#
# def create_id(self):
#     pass
#
#
# 2、获取老师所有信息
#
#
# def tell_info(self):
#     pass
#
#
# 3、将老师对象序列化保存到文件里，文件名即老师的编号，提示功能如下
#
#
# def save(self):
#     with open('老师的编号', 'wb') as f:
#         pickle.dump(self, f)
#
#
# 4、从文件夹中取出存储老师对象的文件，然后反序列化出老师对象, 提示功能如下
#
#
# def get_obj_by_id(self, id):
#     return pickle.load(open(id, 'rb'))
#
# 编号、姓名、性别、年龄、等级、工资，

class Teacher:
    def __init__(self, id=None, name=None, gender=None, age=None, level=None, salary=None):
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age
        self.level = level
        self.salary = salary

    def create_id(self, id):
        self.id = id

    def tell_info(self):
        print(self.id,
              self.name,
              self.gender,
              self.age,
              self.level,
              self.salary
              )

    def save(self):
        with open(self.id, 'wb') as f:
            pickle.dump(self, f)

    def get_obj_by_id(self, id):
        with open(id, 'rb') as f:
            pickle.load(f)


# 10、按照定义老师的方式，再定义一个学生类
#

class Studnet:
    def __init__(self, id=None, name=None, gender=None, age=None):
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age

    def create_id(self, id):
        self.id = id

    def tell_info(self):
        print(self.id,
              self.name,
              self.gender,
              self.age,
              )

    def save(self):
        with open(self.id, 'wb') as f:
            pickle.dump(self, f)

    def get_obj_by_id(self, id):
        with open(id, 'rb') as f:
            pickle.load(f)


# 11、抽象老师类与学生类得到父类，用继承的方式减少代码冗余
#

class Person:
    def __init__(self, id=None, name=None, gender=None, age=None):
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age

    def create_id(self, id):
        self.id = id

    def tell_info(self):
        print(self.id,
              self.name,
              self.gender,
              self.age,
              )

    def save(self):
        with open(self.id, 'wb') as f:
            pickle.dump(self, f)

    def get_obj_by_id(self, id):
        with open(id, 'rb') as f:
            pickle.load(f)


class Teacher(Person):
    def __init__(self, id, name, gender, age, level, salary):
        super().__init__(id, name, gender, age)
        self.level = level
        self.salary = salary

    def tell_info(self):
        print(self.id,
              self.name,
              self.gender,
              self.age,
              )
        print(self.level,
              self.salary,
              )

    class Studnet:
        def __init__(self, id, name, gender, age):
            super().__init__(id, name, gender, age)

        def tell_info(self):
            print(self.id,
                  self.name,
                  self.gender,
                  self.age,
                  )


# 12、基于面向对象设计一个对战游戏并使用继承优化代码，参考博客
# http: // www.cnblogs.com / linhaifeng / articles / 7340497.
# html  # _label1
#


class Hero:
    def __init__(self, nickname,
                 aggressivity,
                 life_value,
                 money,
                 armor):
        self.nickname = nickname
        self.aggressivity = aggressivity
        self.life_value = life_value
        self.money = money
        self.armor = armor

    def attack(self, enemy):
        damage_value = self.aggressivity - enemy.armor
        enemy.life_value -= damage_value


class Riven(Hero):
    camp = 'Noxus'

    def __init__(self, nickname,
                 aggressivity=54,
                 life_value=414,
                 money=1001,
                 armor=3):
        super().__init__(nickname,
                         aggressivity,
                         life_value,
                         money,
                         armor)


class Garen(Hero):
    camp = 'Demacia'

    def __init__(self, nickname,
                 aggressivity=58,
                 life_value=455,
                 money=100,
                 armor=10):
        super().__init__(nickname,
                         aggressivity,
                         life_value,
                         money,
                         armor)


class BlackCleaver:
    def __init__(self, price=475, aggrev=9, life_value=100):
        self.price = price
        self.aggrev = aggrev
        self.life_value = life_value

    def update(self, obj):
        obj.money -= self.price  # 减钱
        obj.aggressivity += self.aggrev  # 加攻击
        obj.life_value += self.life_value  # 加生命值

    def fire(self, obj):  # 这是该装备的主动技能,喷火,烧死对方
        obj.life_value -= 1000  # 假设火烧的攻击力是1000


r1 = Riven('草丛伦')
g1 = Garen('盖文')
b1 = BlackCleaver()

print(r1.aggressivity, r1.life_value, r1.money)  # r1的攻击力,生命值,护甲

if r1.money > b1.price:
    r1.b1 = b1
    b1.update(r1)

print(r1.aggressivity, r1.life_value, r1.money)  # r1的攻击力,生命值,护甲

print(g1.life_value)
r1.attack(g1)  # 普通攻击
print(g1.life_value)
r1.b1.fire(g1)  # 用装备攻击
print(g1.life_value)  # g1的生命值小于0就死了
