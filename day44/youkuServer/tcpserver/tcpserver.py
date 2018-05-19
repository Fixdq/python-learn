import socket
import json
import struct
import time
from lib import common
from concurrent.futures import ThreadPoolExecutor
from interface import common_interface, admin_interface, user_interface
from threading import Lock
from tcpserver import user_data

# session 生成规则
# (addr)
# 创建线程池
thread_pool = ThreadPoolExecutor(10)
# 在主线程创建锁
mutex = Lock()
user_data.mutex = mutex

menu_dic = {
    'register': common_interface.register,
    'login': common_interface.login,
    'notice': admin_interface.notice,
    'get_all_movie': admin_interface.get_all_movie,
    'check_movie_exists': admin_interface.check_movie_exists,
    'upload_movie': admin_interface.upload_movie,
    'get_movie_all': common_interface.get_movie_all,
    'delete_movie': admin_interface.delete_movie,
}


def dispatch(data,conn):
    if data['type'] not in menu_dic:
        res = {'flag': False, 'msg': '请求错误'}
        common.send_back(res, conn)
    else:
        menu_dic[data['type']](conn, data)

def work(conn, addr):
    while True:
        try:
            head_len = conn.recv(4)
            message = conn.recv(struct.unpack('i',head_len)[0])
            if not message: continue
            req = json.loads(message.decode('utf-8'))
            req['addr'] = addr
            dispatch(req,conn)
        except Exception as e:
            print(e)
            conn.close()
            # 用户断开链接 清除缓存在服务端的session
            user_data.mutex.acquire()
            # 判断 对应用户 是否存在缓存中
            if user_data.alive_user.get(addr):
                user_data.pop(addr)
            user_data.mutex.release()
            break


def get_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        thread_pool.submit(work, conn, addr)


def run():
    get_server()
