from conf import settings

import json

import os


def select(name):
    path = r'%s/%s.json' % (settings.BASE_DB, name)
    if os.path.isfile(path):
        with open(path, 'r', encoding=settings.ENCODING) as f:
            return json.load(f)
    else:
        return False


def update(user_dic):
    path = r'%s/%s.json' % (settings.BASE_DB, user_dic['name'])
    with open(path, 'w', encoding=settings.ENCODING) as f:
        json.dump(user_dic, f)
        f.flush()
