#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

import socket
import subprocess
ip_prot = ('127.0.0.1', 8884)
buffer = 1024
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind(ip_prot)
socket_server.listen(5)

print('-----start----')
while True:

    print('-----listening----')
    conn, address = socket_server.accept()
    print('-----处理一次---ip%s-' % list(address))
    while True:
        try:
            print('-----recving------')
            cmd = conn.recv(buffer)
            print('-----%s----' % cmd.decode('utf-8'))

            res = subprocess.Popen(cmd,
                                   shell=True,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            msg_success = res.stdout.read()
            msg_error = res.stdout.read()
            print('发送-----')
            conn.send(msg_success)
            conn.send(msg_error)
            print('--发送成功--')
        except Exception:
            conn.send('error')
    conn.close()
socket_server.close()
