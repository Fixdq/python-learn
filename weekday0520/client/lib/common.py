#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-20 下午3:09
# @Author  : fixdq
# @File    : common.py
# @Software: PyCharm
import hashlib
import json
import os
import struct
import sys

from client.conf import setting
from client.tcpclient import cookies


def outter(type):
    from client.core import user, admin
    def is_login(func):
        def wrapper(*args, **kwargs):
            if cookies.userdata['session']:
                func(*args, **kwargs)
            else:
                if type == 'user':
                    pass
                elif type == 'admin':
                    admin.login(*args, **kwargs)
                else:
                    raise Exception("出错了啊")

        return wrapper

    return outter


def send_back(conn, dic, file=None):
    send_bytes = json.dumps(dic).encode(setting.charset)
    conn.send(struct.pack('i', len(send_bytes)))
    conn.send(send_bytes)

    # 发送视频
    if file:
        send_size = 0
        with open(file, 'rb') as f:
            for line in f:
                send_size += len(line)
                conn.send(line)
                progress(send_size / dic['file_size'])

    head_len_bytes = conn.recv(4)
    head_bytes = conn.recv(struct.unpack('i', head_len_bytes)[0])
    return json.loads(head_bytes.decode(setting.charset))


def get_filesize(file):
    return os.path.getsize(file)


def get_file_all():
    files = os.listdir(setting.BASE_DIR_MOVIE)
    return files


def get_file_md5(file):
    md5 = hashlib.md5()
    file_size = get_filesize(file)
    file_list = [0, file_size // 3, (file_size // 3) * 2, file_size - 10]
    for index in file_list:
        with open(file, 'rb') as f:
            f.seek(index)
            md5.update(f.read(10))

    return md5.hexdigest()


def progress(percent, width=50):
    if percent > 1:
        percent = 1
    show_str = (['%%-%ds'] % width) % (percent * width) * '#'
    print('\r%s %s%%' % (show_str, int(100 * percent)), file=sys.stdout, end='')
