#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from core import admin
from core import student
from core import teacher

"""
业务逻辑
"""
user_data = {
    'account_id': None,
    'is_auth': False,
    'account_date': None,
}


def view_student():
    menu_str = """
            1: 学员注册
            2: 进入选课
            3: 查看个人信息
            """

    menu_dic = {
        '1': student.register_student,
        '2': student.choice_course,
        '3': student.show_info,
    }
    action(menu_str, menu_dic)


def view_teacher():

    menu_str = """
            1: 查看学员信息
            2: 修改学员成绩
            3: 查看个人信息
            """
            # 4: 修改个人信息
            # """

    menu_dic = {
        '1': teacher.show_student_info,
        '2': teacher.update_student_score,
        '3': teacher.show_teacher_info,
        # '4': teacher.update_teacher_info,
        # '2': teacher.show_student_info,
        # '3': teacher.update_student_score,
        # '4': teacher.show_teacher_info,
        # '5': teacher.update_teacher_info,
        # '6': teacher.show_school_info,
    }
    action(menu_str, menu_dic)


def view_manager():
    menu_str = """
    
            1: 创建学校
            2: 创建课程
            3: 创建班级
            4: 创建讲师
            """
            # 5: 创建学员
            # """

    menu_dic = {
        '1': admin.create_school,
        '2': admin.create_course,
        '3': admin.create_classes,
        '4': admin.create_teacher,
        # '5': admin.create_student,
    }
    action(menu_str, menu_dic)


def start():
    """
    入口
    :return: 
    """
    menu_str = """
        1: 学生视图
        2: 老师视图
        3: 管理员视图
        """

    menu_dic = {
        '1': view_student,
        '2': view_teacher,
        '3': view_manager,
    }
    action(menu_str, menu_dic)


def action(menu_str, menu_dic):
    flag = False
    while flag != "b":  # 返回上一层
        print(menu_str)
        choice = input('>>:').strip()
        if "b" == choice:
            flag = "b"
            continue
        if choice not in menu_dic:
            print("输入错误")
            continue
        menu_dic[choice]()


def run():
    start()
