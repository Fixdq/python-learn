#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : common.py
# @Software: PyCharm
import json
import os

import struct
from conf import settings


def get_all_file(type):
    path = os.path.join(settings.BASE_DB, type)
    if not os.path.isdir(path):
        os.mkdir(path)
    return os.listdir(path)


def send(conn, data, type=None):
    """
    发送简单的bytes
    :param type: 请求类型  router判断用
    :param conn: 
    :param data: str
    :return: 
    """

    data = data.encode('utf-8')
    # 把真实数据的相关信息,请求类型，包装成字典
    head = {
        'size': len(data),  # 真实数据 大小
        'type': type  # 请求类型
    }
    # json 序列化 字典信息
    head_str = json.dumps(head)
    # 只包含报头长度 (报头的报头)
    # i 模式,产生一个固定4字节长度bytes
    head_head = struct.pack('i', len(head_str))
    # 发送   (报头的报头)
    conn.send(head_head)
    # 报头数据
    conn.send(head_str.encode('utf-8'))
    # 真实数据
    conn.send(data)


def recv(conn):
    """
    接收简单的bytes
    :param conn: 
    :return: str
    """

    # 接收  报头的报头  (固定长度 4 字节)
    head_head = conn.recv(4)
    # 解析 报头的长度
    head_len = int(struct.unpack('i', head_head)[0])
    # 接收  自定义报头
    head = conn.recv(head_len)
    # 解析  自定义报头 dic
    dic = json.loads(head.decode('utf-8'))
    # 请求类型
    type = dic['type']
    # 真实数据大小
    size = dic['size']
    # 接收  真实的数据
    res = conn.recv(size)

    if type:
        return type, res.decode('utf-8')
    return res.decode('utf-8')


def send_obj_json(conn, data, type=None):
    """ 
    发送可以被json序列化的数据
    :param type:  请求类型  router判断用
    :param conn: 
    :param data: 可以被json序列化的对象
    :return: 
    """
    data = json.dumps(data)
    send(conn, data, type)


def recv_obj_json(conn):
    """
    接收被json序列化的数据
    :param conn: 
    :return: 数据原类型
    """
    res = recv(conn)
    # 判断返回值 是否是元组
    if isinstance(res, tuple):
        type, data = res
        return type, json.loads(data)
    return json.loads(res)


def send_file(conn, author, path):
    """
    发送文件
    :param author: 
    :param conn: 连接对象
    :param path: 文件的路径
    :return: 
    """

    # 获取文件的长度
    file_size = os.path.getsize(path)

    # 把真实数据的相关信息,包装成字典
    head = {
        'author': author,
        'file_name': os.path.basename(path),
        'file_size': file_size,
    }
    # json 序列化 字典信息
    head_str = json.dumps(head)
    # 只包含报头长度 (报头的报头)
    # i 模式,产生一个固定4字节长度bytes
    head_head = struct.pack('i', len(head_str))
    # 发送   (报头的报头)
    conn.send(head_head)
    # 报头数据
    conn.send(head_str.encode('utf-8'))
    # 真实数据
    send_size = 0
    with open(path, 'rb') as f:
        for line in f:
            conn.send(line)
            send_size += len(line)
            print('%s%%' % (int(send_size / file_size * 100)))
        else:
            print('发送完毕')


def recv_file(conn):
    # 接收  报头的报头  (固定长度 4 字节)
    head_head = conn.recv(4)
    # 反解出 报头的长度
    head_len = int(struct.unpack('i', head_head)[0])
    # 接收  自定义报头
    head = conn.recv(head_len)
    # 拿到  自定义报头
    data_dic = json.loads(head.decode('utf-8'))

    author = data_dic['author']
    file_name = data_dic['file_name']
    file_size = data_dic['file_size']
    # 如果目录不存在，创建目录
    if not os.path.isdir(settings.BASE_VIDEOS):
        os.mkdir(settings.BASE_VIDEOS)
    file_path = os.path.normpath(os.path.join(
        settings.BASE_VIDEOS,
        file_name
    ))

    recv_size = 0
    print('----->', file_path)
    with open(file_path, 'wb') as f:
        while recv_size < file_size:
            recv_data = conn.recv(settings.max_buffer_size)
            f.write(recv_data)
            recv_size += len(recv_data)
            print(recv_size/file_size)

    return author, file_name, file_size, file_path
