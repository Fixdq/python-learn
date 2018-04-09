#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
import json
import os

from conf import setting


def select(uname):
    path = r'%s%s.json' % (setting.BASE_DB, uname)
    if os.path.isfile(path):
        with open(path, encoding=setting.UTF8) as f:
            return json.load(f)
    else:
        return False


def update(update_dic):
    path = r'%s%s.json' % (setting.BASE_DB, update['name'])
    with open(path, 'w', encoding=setting.UTF8) as f:
        j = json.dump(update_dic, f)
        f.flush()
