import os

from lib import common
from db.modles import *
from conf import setting


@common.login_auth
def notice(conn, data):
    notice = Notice(name=data['title'],
                    content=data['content'],
                    user_id=data['user_id'],
                    create_time=common.get_nowtime())

    notice.save()
    back_dic = {'flag': True, 'msg': '发布公告成功'}
    common.send_back(back_dic, conn)


@common.login_auth
def get_all_movie(conn, data):
    pass

@common.login_auth
def upload_movie(conn, data):
    file_name = common.get_uuid(data['name']) + data['name']
    file_path = os.path.join(setting.BASE_DIR_MOVIES, file_name)
    file_size = data['file_size']
    recv_size = 0
    # 接收视频数据
    while recv_size < file_size:
        with open(file_path, 'wb') as f:
            recv_data = conn.recv(1024)
            f.write(recv_data)
            recv_size += len(recv_data)

    movie = Movie(name=file_name,
                  path=file_path,
                  file_md5=data['file_md5'],
                  is_free=data['is_free'],
                  is_delete=0,
                  create_time = common.get_nowtime(),
                  user_id=data['user_id'],
                  )
    movie.save()
    back_dic = {'flag': True, 'msg': '上传成功 '}
    common.send_back(back_dic, conn)


@common.login_auth
def check_movie_exists(conn, data):
    movie = Movie().select_one(file_md5=data['file_md5'])
    if movie:
        back_dic = {'flag': True, 'msg': '视频已存在'}
        common.send_back(back_dic, conn)
    else:
        back_dic = {'flag': False, 'msg': ''}
        common.send_back(back_dic, conn)


@common.login_auth
def delete_movie(conn,data):
    movie = Movie().select_one(id=data['movie_id'])
    movie.is_delete = 1
    movie.update()
    back_dic = {'flag': True, 'msg': '视频已删除'}
    common.send_back(back_dic, conn)