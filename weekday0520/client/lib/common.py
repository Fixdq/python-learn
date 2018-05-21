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

from conf import setting


def outter(type):
    from core import user, admin
    def is_login(func):
        def wrapper(*args, **kwargs):
            if type == 'user':
                if user.cookie['session']:
                    func(*args, **kwargs)
                else:
                    user.login(*args, **kwargs)
            elif type == 'admin':
                if admin.cookie['session']:
                    func(*args, **kwargs)
                else:
                    admin.login(*args, **kwargs)
            else:
                raise Exception("出错了啊")

        return wrapper

    return is_login


def send_back(conn, data, file=None):
    send_bytes = json.dumps(data).encode(setting.charset)
    conn.send(struct.pack('i', len(send_bytes)))
    conn.send(send_bytes)

    if file:
        file_size = data['file_size']
        send_size = 0
        with open(file, 'rb') as f:
            for line in f:
                conn.send(line)
                send_size += len(line)
                progress(send_size / file_size)


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
    show_str = ('[%%-%ds]' % width) % (int(percent * width )* '#')
    print('\r%s %s%%' % (show_str, int(100 * percent)), file=sys.stdout, end='')
