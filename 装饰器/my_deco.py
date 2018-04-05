#!/usr/bin/env python3
# encoding: utf-8
# by fixdq



def auth(func):
    def wrapper(*args, **kwargs):
        print("您还没登录！")
        return func(*args, **kwargs)
        print("您还没登录！")
    return wrapper