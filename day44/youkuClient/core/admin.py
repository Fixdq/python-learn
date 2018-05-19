import os
from lib import common
from tcpClient import tcpclient
from tcpClient import cookie
from conf import setting


def admin_register(client):
    while True:
        name = input('请输入用户名:').strip()
        password = input('请输入密码').strip()
        cof_password = input('请确认密码:').strip()
        if password == cof_password:
            user_dic = {'type': 'register',
                        'name': name,
                        'password': common.get_md5(password),
                        'user_type': 'admin'}
            back_dic = common.send_back(client, user_dic)
            if back_dic['flag']:
                print(back_dic['msg'])
                break
            else:
                print(back_dic['msg'])


        else:
            print('两次密码不一致')


def admin_login(client):
    while True:
        name = input('请输入用户名：').strip()
        password = input('请输入密码').strip()
        send_dic = {'type': 'login',
                    'name': name,
                    'password': common.get_md5(password)}
        back_dic = common.send_back(client, send_dic)
        if back_dic['flag']:

            # 登录成功  接收 session  保存在本地
            cookie.user_data['session'] = back_dic['session']

            print(back_dic['msg'])
            break
        else:
            print(back_dic['msg'])


@common.is_login
def upload_movie(client):
    while True:
        movies = common.get_all_files(setting.BASE_UPLOAD_MOVIE)
        if not movies:
            print('没有可以上传的视频')
            break
        for i, movie in enumerate(movies):
            print(i, movie)

        choice = input('请选择上传的视频》》》》').strip()
        if choice == 'q': break
        if not choice.isdigit():
            print('请正确选择')
            continue
        choice = int(choice)
        if choice < 0 or choice >= len(movies):
            print('请正确选择')
            continue

        file_path = os.path.join(setting.BASE_UPLOAD_MOVIE, movies[choice])
        file_md5 = common.get_file_md5(file_path)
        send_data = {
            'type': 'check_movie_exists',
            'session': cookie.user_data['session'],
            'file_md5': file_md5,
        }
        # 判断服务器上视频是否存在
        back_data = common.send_back(client, send_data)
        if back_data['flag']:
            print(back_data['msg'])
            break
        # 服务器上不存在 继续
        while True:
            is_free = input('视频是否收费：（y/n）').strip()
            if is_free not in ['y', 'n']:
                print('请正确选择')
                continue
            if is_free == 'y':
                movie_is_free = 1
            else:
                movie_is_free = 0
            break
        # 文件信息
        send_data = {
            'type': 'upload_movie',
            'session': cookie.user_data['session'],
            'name': movies[choice],
            'file_size': common.get_file_size(file_path),
            'file_md5': file_md5,
            'is_free': movie_is_free
        }
        back_data = common.send_back(client, send_data, file_path)
        if back_data['flag']:
            print(back_data['msg'])
            break
        else:
            print(back_data['msg'])


@common.is_login
def delete_movie(client):
    while True:
        send_data = {
            'type': 'get_movie_all',
            'session': cookie.user_data['session'],
        }
        back_data = common.send_back(client, send_data)

        if not back_data['flag']:
            print(back_data['msg'])
            break
        for k ,v in enumerate(back_data['msg']):
            print('%s--名字：%s' % (k,v[1]))

        choice = input('请选择删除的视频编号》》》》').strip()
        if choice == 'q': break
        if not choice.isdigit():
            print('请正确选择')
            continue
        choice = int(choice)
        if choice < 0 or choice >= len(back_data['msg'][choice]):
            print('请正确选择')
            continue
        is_free = input('是否删除：（y/n）').strip()
        if is_free not in ['y', 'n']:
            print('请正确选择')
            continue
        if is_free == 'y':
            send_data = {
                'type': 'delete_movie',
                'session': cookie.user_data['session'],
                'movie_id': back_data['msg'][choice][0],
            }
            back_data = common.send_back(client, send_data)
            print(back_data['msg'])

        break





@common.is_login
def notice(client):
    while True:
        title = input('请输入公告标题：').strip()
        content = input('请输入公告内容：').strip()

        send_data = {
            'type': 'notice',
            'session': cookie.user_data['session'],
            'title': title,
            'content': content,
        }
        back_data = common.send_back(client, send_data)
        if back_data['flag']:
            print(back_data['msg'])
            break
        else:
            print(back_data['msg'])


func_dic = {
    '1': admin_register,
    '2': admin_login,
    '3': upload_movie,
    '4': delete_movie,
    '5': notice,
}


def admin_view():
    client = tcpclient.get_client()
    while True:
        print('''
        1 注册
        2 登录
        3 上传视频
        4 删除视频
        5 发布公告
        ''')
        choice = input('请选择功能：').strip()
        if choice == 'q': break
        if choice not in func_dic: continue
        func_dic[choice](client)
