#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-20 下午3:43
# @Author  : fixdq
# @File    : setting.py
# @Software: PyCharm
import hashlib
import json
import struct
import time

from conf import setting
from tcpserver import userdata

def login_auth(func):
    def wrapper(*args,**kwargs):
        session = args[1]['session']
        # 判断用户是否在线
        for value in userdata.userdata.values():
            if value[0] == session:
                # 用户在线
                args[1]['user_id'] = value[1]
                # 授权
                func(*args, **kwargs)
                return
        # 用户不在线
        back_dic ={'flag':False,'msg':'非授权用户'}
        send(args[0],back_dic)
    return wrapper

def send(conn, dic, file=None):
    send_bytes = json.dumps(dic).encode(setting.charset)
    conn.send(struct.pack('i', len(send_bytes)))
    conn.send(send_bytes)


def recv(conn):
    head_len_bytes = conn.recv(4)
    head_bytes = conn.recv(struct.unpack('i', head_len_bytes)[0])
    return json.loads(head_bytes.decode(setting.charset))


def get_md5(data):
    md5 = hashlib.md5()
    md5.update(data.encode(setting.charset))
    return md5.hexdigest()


def get_uuid(data):
    md5 = hashlib.md5()
    md5.update(data.encode(setting.charset))
    md5.update(str(time.clock()).encode(setting.charset))
    return md5.hexdigest()


def get_nowtime():
    return time.strftime('%Y:%m:%d %X')
