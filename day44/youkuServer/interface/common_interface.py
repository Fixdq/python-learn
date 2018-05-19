from db.modles import *
from lib import common
from tcpserver import user_data


def register(conn, data):
    name = data['name']
    user = User.select_one(name=name)
    if user:
        back_dic = {'flag': False, 'msg': '用户存在'}
        common.send_back(back_dic, conn)
    else:

        password = data['password']
        user_type = data['user_type']
        user = User(name=name, password=password, is_vip=0, locked=0, user_type=user_type)
        user.save()
        back_dic = {'flag': True, 'msg': '注册成功'}
        common.send_back(back_dic, conn)


def login(conn, data):
    user = User.select_one(name=data['name'])
    if user:
        if user.password == data['password']:
            back_dic = {'flag': True, 'msg': '登录成功'}

            # 生成session
            session = common.get_uuid(data['name'])
            back_dic['session'] = session
            # 加锁
            user_data.mutex.acquire()
            # 在服务器端保存 用户信息
            user_data.alive_user[data['addr']] = [session, user.id]
            # 释放锁
            user_data.mutex.release()
            # 响应信息
            common.send_back(back_dic, conn)
        else:
            back_dic = {'flag': False, 'msg': '密码错误'}
            common.send_back(back_dic, conn)
    else:
        back_dic = {'flag': False, 'msg': '用户不存在'}
        common.send_back(back_dic, conn)


@common.login_auth
def get_movie_all(conn, data):
    movies = Movie.select_many(is_delete=0)
    if movies:
        back_movies = [[v['id'], v['name']] for v in movies]
        back_dic = {'flag': True, 'msg': back_movies}
    else:
        back_dic = {'flag': False, 'msg': '暂无电影'}
    common.send_back(back_dic, conn)
