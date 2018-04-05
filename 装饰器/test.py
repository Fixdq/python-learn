#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


import my_deco


@my_deco.auth
def test_deco():
    print('ssssssssssss')


test_deco()