#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : common.py
# @Software: PyCharm
import json
import os

import struct
from day29.homework import settings


def send(conn, data):
    """
    发送简单的bytes
    :param conn: 
    :param data: bytes
    :return: 
    """

    data = data.encode('utf-8')
    # 把真实数据的相关信息,包装成字典
    head = {
        'len': len(data)
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
    # 反解出 报头的长度
    head_len = int(struct.unpack('i', head_head)[0])
    # 接收  自定义报头
    head = conn.recv(head_len)
    # 拿到  自定义报头的长度
    body_len = json.loads(head.decode('utf-8'))['len']
    # 接收  真实的数据
    res = conn.recv(body_len)
    return res.decode('utf-8')


def send_obj_json(conn, data):
    """
    发送可以被json序列化的数据
    :param conn: 
    :param data: 
    :return: 
    """
    data = json.dumps(data)
    send(conn, data)


def recv_obj_json(conn):
    """
    接收被json序列化的数据
    :param conn: 
    :return: 数据原类型
    """
    data = recv(conn)
    return json.loads(data)


def send_file(conn, path):
    """
    
    :param conn: 连接对象
    :param path: 文件的路径
    :return: 
    """

    # 获取文件的长度
    file_size = os.path.getsize(path)

    # 把真实数据的相关信息,包装成字典
    head = {
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
            print('%s%' % (send_size/file_size))
        else:
            print('发送完毕')


def recv_file(conn, path):
    """
    
    :param conn: 连接对象
    :param path: 保存文件的路径
    :return: 
    """
    # 接收  报头的报头  (固定长度 4 字节)
    head_head = conn.recv(4)
    # 反解出 报头的长度
    head_len = int(struct.unpack('i', head_head)[0])
    # 接收  自定义报头
    head = conn.recv(head_len)
    # 拿到  自定义报头
    data_dic = json.loads(head.decode('utf-8'))

    file_name = data_dic['file_name']
    file_size = data_dic['file_size']

    file_path = os.path.normpath(os.path.join(
        path,
        file_name
    ))

    recv_size = 0
    print('----->', file_path)
    with open(file_path, 'wb') as f:
        while recv_size < file_size:
            recv_data = conn.recv(settings.max_buffer_size)
            f.write(recv_data)
            recv_size += len(recv_data)
            print(recv_size)
