import hashlib
import json
import struct
import time
from tcpserver import user_data


def login_auth(func):
    def wrapper(*args, **kwargs):
        # 判断用户 是否在线
        for value in user_data.alive_user.values():
            if value[0] == args[1]['session']:
                # 将用户id 放入参数字典
                args[1]['user_id'] = value[1]

        if not args[1].get('user_id'):
            # 用户不存在 非授权用户
            back_data = {'flag': False, 'msg': '你不是授权用户'}
            send_back(back_data, args[0])
            return
        # 授权用户
        func(*args, **kwargs)
    return wrapper



def send_back(back_dic, conn):
    back_bytes = json.dumps(back_dic).encode('utf-8')
    conn.send(struct.pack('i',len(back_bytes)))
    conn.send(back_bytes)


def get_uuid(data):
    md = hashlib.md5()
    md.update(data.encode('utf-8'))
    md.update(str(time.clock()).encode('utf-8'))
    return md.hexdigest()


def get_nowtime():
    now_time = time.strftime('%Y:%m:%d %X')
    return now_time
