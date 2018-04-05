# encoding: utf-8
# by fixdq


def wrapper(x):
    def inner():
        print(x)

    return inner


f = wrapper(9999)
f()
