from tcpClient import tcpclient



def user_view():
    client = tcpclient.get_client()
    while True:
        print('''
            1 注册
            2 登录
            3 冲会员
            4 查看视频
            5 下载免费视频
            6 下载收费视频
            7 查看观影记录
            8 查看公告
        ''')
        choice = input('请选择功能：').strip()
        if choice == 'q': break
        if choice not in func_dic: continue
        func_dic[choice](client)
