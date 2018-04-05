#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


import logging

lg = logging.getLogger('tt')
lg_h = logging.FileHandler('a.txt', encoding='utf-8')
lg_sh = logging.StreamHandler()

lg_fmt = logging.Formatter(
    fmt='s:%(message)s',
    datefmt="%Y-%m-%d %H:%M:%S")

lg.addHandler(lg_h)
lg.addHandler(lg_sh)

lg_h.setFormatter(lg_fmt)
lg_sh.setFormatter(lg_fmt)

lg.setLevel(10)
lg_h.setLevel(10)
lg.debug('坎坎坷坷扩扩扩扩扩扩')
