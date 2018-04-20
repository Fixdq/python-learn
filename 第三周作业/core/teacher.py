#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

from core import admin


def show_student_info():
    school = admin.choice_school()
    flag = True
    while flag:
        teacher_name = input("请输入您的名字：").strip()
        # 查询老师
        if teacher_name not in school.teachers:
            print("名字不存在！")
            continue
        stu_dic = school.students
        if stu_dic is None:
            print('本校还没有学生')
            break
        for k in stu_dic:
            print("姓名：%s ,成绩：%s" % (k, stu_dic[k].score))
        break


def update_student_score():
    school = admin.choice_school()
    flag = True
    while flag:
        teacher_name = input("请输入您的名字：").strip()
        # 查询老师
        if teacher_name not in school.teachers:
            print("名字不存在！")
            continue
        stu_dic = school.students
        if stu_dic is None:
            print('本校还没有学生')
            break
        while flag:
            stu_name = input("请输入学生名字：").strip()
            if stu_name not in stu_dic:
                print('名字不正确！')
                continue
            stu = stu_dic[stu_name]
            while flag:
                print('%s现在分数：%s' % (stu.name, stu.score))
                score = input('分数改为:').strip()
                if not score.isdigit():
                    print('请输入正确的分数')
                    continue
                stu.score = score
                stu_dic[stu_name] = stu
                school.students = stu_dic
                school.save()
                print('分数修改成功！')
                flag = False
                break


def show_teacher_info():
    """
    查看老师信息
    :return: 
    """
    school = admin.choice_school()
    flag = True
    while flag:
        teacher_name = input("请输入您的名字：").strip()
        # 查询老师
        if teacher_name not in school.teachers:
            print("名字不存在！")
            continue
        # 获取老师
        teacher = school.teachers[teacher_name]
        teacher.show_info()
        break


def get_teacher(school):
    flag = True
    while flag:
        teacher_name = input("请输入您的名字：").strip()
        # 查询老师
        if teacher_name not in school.teachers:
            print("名字不存在！")
            continue
        # 获取老师
        teacher = school.teachers[teacher_name]
        return teacher

# def update_teacher_info():
#     print(update_teacher_info)
#
#
# def show_school_info():
#     print(show_school_info)
