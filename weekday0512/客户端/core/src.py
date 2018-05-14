from core import admin, user

menu = """
1 管理员视图
2 用户视图
"""

menu_dic = {
    '1': admin.admin_view,
    '2': user.user_view
}


def run():
    while True:
        print(menu)
        choose = input('选择用户视图>>:').strip()
        if 'q' == choose: break
        if choose not in menu_dic: continue
        menu_dic[choose]()
