#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


from core import admin, student, teacher

menu = """
1.管理员视图
2.老师视图
3.学生视图
"""

menu_dic = {
    '1': admin.admin_view,
    '2': teacher.teacher_view,
    '3': student.student_view
}


def run():
    while True:
        print(menu)
        ch = input('请选择您的操作:').strip()
        if ch == 'q': break
        if ch not in menu_dic: continue
        menu_dic[ch]()
