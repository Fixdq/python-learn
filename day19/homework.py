#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


# 4月11日
#
# 1、定义学校类，实例化出：北京校区、上海校区两个对象
# 校区独有的特征有：
# 校区名 =“xxx”
# 校区地址 = {'city': "所在市", 'district': '所在的区'}
# 多们课程名 = ['xxx', 'yyy', 'zzz']
# 多个班级名 = ['xxx', 'yyy', 'zzz']

# 校区可以：
# 1、创建班级
# 2、查看本校区开设的所有班级名
# 3、创建课程
# 4、查看本校区开设的所有课程名
#
# 2、定义出班级类，实例化出两个班级对象
# 班级对象独有的特征：
# 班级名 =‘xxx’
# 所属校区名 =‘xxx’
# 多门课程名 = ['xxx', 'yyy', 'zzz']
# 多个讲师名 = ['xxx', 'xxx', 'xxx']
#
# 班级可以：
# 1、查看本班所有的课程
# 2、查看本班的任课老师姓名
#
# 3、定义课程类，实例化出python、linux、go三门课程对象
# 课程对象独有的特征：
# 课程名 =‘xxx’
# 周期 =‘3
# mons’
# 价格 = 3000
#
# 课程对象可以：
# 1、查看课程的详细信息
#
# 4、定义学生类，实例化出张铁蛋、王三炮两名学生对象
# 学生对象独有的特征：
# 学号 = 10
# 名字 =”xxx“
# 班级名 = ['xxx', 'yyy']
# 分数 = 33
#
# 学生可以：
# 1、选择班级
# 3、注册，将对象序列化到文件
#
# 5、定义讲师类，实例化出egon，lqz，alex，wxx四名老师对象
# 老师对象独有的特征：
# 名字 =“xxx”
# 等级 =“xxx”
#
# 老师可以：
# 1、修改学生的成绩
#
#
import json
import os


class School:
    """
    学校类
    """

    def __init__(self, name=None, address=None, class_list=None, course_list=None):
        """
        
        :param name: 校区名字
        :param address: 地址
        :param class_list:班级列表
        :param course_list: 课程列表
        """
        self.name = name,
        self.address = address,
        self.class_list = class_list,
        self.course_list = course_list,

    def create_class(self, class_name):
        """
        创建班级
        :param class_name: 
        :return: 
        """
        self.class_list.append(class_name)

    def show_class_names(self):
        """
        查看本校区开设的所有班级名
        :return: 
        """
        for item in self.class_list:
            print(item)

    def create_course(self, course_name):
        """
        创建课程
        :param course_name: 
        :return: 
        """

        self.course_list.append(course_name)

    def show_course_titles(self):
        """
        查看本校区开设的所有课程名
        :return: 
        """
        for item in self.course_list:
            print(item)


# 实例化

school_bejing = School(
    '北京校区',
    {
        'city': '北京',
        'district': '昌平',
    },
    ['Python', 'Linux'],
    ['Python一期', 'Linux十期']
)

school_shanghai = School(
    '上海校区',
    {
        'city': '上海',
        'district': '浦东新区',
    },
    ['Python', 'go'],
    ['Python十期', 'go二十期']
)


class Class:
    """
    班级类
    """

    def show_classes(self):
        """
        查看本班所有的课程
        :return: 
        """
        for item in self.classes:
            print(item)

    def __init__(self, class_name=None, par_school=None, classes=None, teachers=None):
        """
        
        :param class_name: 班级名字
        :param par_school: 所属校区名
        :param classes: 多门课程名
        :param teachers: 多个讲师名
        """
        self.class_name = class_name
        self.par_school = par_school
        self.classes = classes
        self.teachers = teachers

    def show_teacher(self ):
        """
        查看本班的任课老师姓名
        :return: 
        """
        for teacher in self.teachers:
            print(teacher)



# 实例化班级对象
python_class = Class(
    class_name='python',
    par_school='北京校区',
    classes=['python', 'go'],
    teachers=['egon', 'alex'],
)

linux_class = Class(
    class_name='python',
    par_school='北京校区',
    classes=['linux', 'go'],
    teachers=['egon', 'alex'],
)


class Course:
    """
    课程类
    """

    def __init__(self, name=None, cl=None, price=None):
        """
        
        :param name: 课程名
        :param clycle: 周期
        :param price: 价格
        """
        self.name = name
        self.cl = cl
        self.price = price

    def show_course(self):
        """
        查看课程的详细信息
        :return: 
        """
        temp = '课程：%s  周期：%s  价格：%s' % (self.name, self.cl, self.price)
        print(temp)


python_course = Course(
    name='python',
    cl='5',
    price='20000',
)

linux_course = Course(
    name='linux',
    cl='5',
    price='20000',
)

go_course = Course(
    name='go',
    cl='5',
    price='20000',
)


class Student:
    """
    学生类
    """

    def __init__(self, stu_id=None, name=None, class_name=None, score=None):
        self.stu_id = stu_id
        self.name = name
        self.class_name = class_name
        self.score = score

    def register(self):
        path = os.path.dirname(os.path.dirname(__file__))
        with open(path, 'wb') as f:
            json.dump(self, f)

    def choose(self):
        pass


stu1 = Student(12, '张铁蛋', ['python'], 59)
stu1 = Student(12, '王三炮', ['linux'], 60)


class Teacher:
    """
    老师类
    """

    def __init__(self, name=None, level=None):
        self.name = name
        self.level = level

    def update_student_score(self, student):
        pass


t_egon = Teacher('egon', level=5)
t_lqz = Teacher('lqz', level=5)
t_alex = Teacher('alex', level=5)
t_wxx = Teacher('wxx', level=5)
