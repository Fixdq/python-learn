#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


class Foo:
    n = 0

    def __init__(self):
        Foo.n += 1


f1 = Foo()
print(f1.n)
f2 = Foo()
print(f1.n)
print(f2.n)
f3 = Foo()
print(f1.n)
print(f2.n)
print(f3.n)