#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
import json
import os

from conf import setting


def select(name):
    path = os.path.join(setting.BASE_DB, "%s.json" % (name))
    if not os.path.exists(path):
        return False
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def update(user_dic):
    path = os.path.join(setting.BASE_DB, "%s.json" % (user_dic['name']))
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f)
