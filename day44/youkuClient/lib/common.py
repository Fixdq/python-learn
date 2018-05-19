import json
import hashlib
import os
import struct
import sys

from tcpClient import cookie


def is_login(func):
    def wrapper(*args, **kwargs):

        if cookie.user_data['session']:
            func(*args, **kwargs)
        else:
            print('>>请先登录<<')
            return

    return wrapper


def send_back(client, send_dic, file=None):
    send_json = json.dumps(send_dic)
    send_bytes = send_json.encode('utf-8')
    client.send(struct.pack('i', len(send_bytes)))
    client.send(send_bytes)



    if file:
        file_size = send_dic['file_size']
        send_size = 0
        with open(file, 'rb') as f:
            for line in f:
                client.send(line)
                send_size += len(line)
                progress(send_size/file_size)

    back_bytes_len = client.recv(4)
    back_bytes = client.recv(struct.unpack('i', back_bytes_len)[0])
    back_dict = json.loads(back_bytes.decode('utf-8'))
    return back_dict


def progress(percent, width=50):
    if percent >= 1:
        percent = 1
    show_str = ('[%%-%ds]' % width) % (int(width * percent) * '#')
    print('\r%s %d%%' % (show_str, int(100 * percent)), file=sys.stdout, flush=True, end='')


def get_md5(data):
    md5 = hashlib.md5()
    md5.update(data.encode('utf-8'))
    return md5.hexdigest()


def get_all_files(path):
    files = os.listdir(path)
    if not files:
        return None
    return files


def get_file_size(path):
    return os.path.getsize(path)


def get_file_md5(path):
    if os.path.exists(path):
        md5 = hashlib.md5()
        file_size = get_file_size(path)
        file_list = [0, file_size // 4, (file_size // 4) * 2, (file_size // 4) * 3, file_size - 10]
        with open(path, 'rb') as f:
            for index in file_list:
                f.seek(index)
                md5.update(f.read(10))
            return md5.hexdigest()
