menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
b = 'b'#返回
q = 'q'#退出
flag = True

# 选择进入第一级（省）
while flag:
    for item in menu:
        print(item)
    # 用户输入
    ch1 = input('输入选择(q：退出，b：返回)==>').strip()
    # 判断是否退出
    if ch1 == q:
        flag = False
        break
    # 判断是否返回
    if ch1 == b:
        continue
    # 判断输入是否正确
    if ch1 not in menu:
        print('输入不正确！')
        continue
    # 选择进入第二级（市）
    while flag:
        for item in menu[ch1]:
            print(item)
        # 用户输入
        ch2 = input('输入选择(q：退出，b：返回)==>').strip()
        # 判断是否退出
        if ch2 == q:
            flag = False
            break
        # 判断是否返回
        if ch2 == b:
            break
        # 判断输入是否正确
        if ch2 not in menu[ch1]:
            print('输入不正确！')
            continue
        # 选择进入第三级（县）
        while flag:
            for item in menu[ch1][ch2]:
                print(item)
            # 用户输入
            ch3 = input('输入选择(q：退出，b：返回)==>').strip()
            # 判断是否退出
            if ch3 == q:
                flag = False
                break
            # 判断是否返回
            if ch3 == b:
                break
            # 判断输入是否正确
            if ch3 not in menu[ch1][ch2]:
                print('输入不正确！')
                continue
            # 显示第四级
            while flag:
                for item in menu[ch1][ch2][ch3]:
                    print(item)
                # 用户输入
                ch4 = input('最后一层(q：退出，b：返回)==>').strip()
                # 判断是否退出
                if ch4 == q:
                    flag = False
                    break
                # 判断是否返回
                if ch4 == b:
                    break
                print('输入不正确')

























#
# exit_flag = False
#
# while not exit_flag:
#     for i in menu:
#         print(i)
#     choice = input("选择进入1>>:")
#     if choice in menu:
#         while not exit_flag:
#             for i2 in menu[choice]:
#                 print("\t",i2)
#             choice2 = input("选择进入2>>:")
#             if choice2 in menu[choice]:
#                 while not exit_flag:
#                     for i3 in menu[choice][choice2]:
#                         print("\t\t", i3)
#                     choice3 = input("选择进入3>>:")
#                     if choice3 in menu[choice][choice2]:
#                         for i4 in menu[choice][choice2][choice3]:
#                             print("\t\t",i4)
#                         choice4 = input("最后一层，按b返回>>:")
#                         if choice4 == "b":
#                             pass
#                         elif choice4 == "q":
#                             exit_flag = True
#                     if choice3 == "b":
#                         break
#                     elif choice3 == "q":
#                         exit_flag = True
#             if choice2 == "b":
#                 break
#             elif choice2 == "q":
#                 exit_flag = True