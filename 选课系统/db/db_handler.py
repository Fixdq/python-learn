#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
import os
import pickle

from conf import settings


def save(obj):
    path = os.path.join(settings.BASE_DB, obj.__class__.__name__.lower())
    if not os.path.isdir(path):
        os.mkdir(path)
    path_file = os.path.join(path, obj.name)
    with open(path_file, 'wb') as f:
        pickle.dump(obj, f)
        f.flush()


def select(name, type):
    path = os.path.join(settings.BASE_DB, type)
    if not os.path.isdir(path):
        os.mkdir(path)
    path_file = os.path.join(path, name)
    if not os.path.exists(path_file):
        return False
    with open(path_file, 'rb') as f:
        return pickle.load(f)
