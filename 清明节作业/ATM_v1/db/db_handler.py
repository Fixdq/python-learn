from conf import settings

import json

import os

def select(name):
    path=r'%s/%s.json'%(settings.BASE_DB,name)
    if os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return False
