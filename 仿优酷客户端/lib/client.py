#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Fixdq
# @File    : client.py
# @Software: PyCharm
import socket


class TCPClient(object):
    address_family = socket.AF_INET

    socket_type = socket.SOCK_STREAM

    request_queue_size = 5

    def __init__(self, server_address):
        self.server_address = server_address
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        self.socket.connect_ex(self.server_address)
    def get_request(self):
        return self.socket
