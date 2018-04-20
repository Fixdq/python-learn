#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


class People:
    def __init__(self, name, weight, height):
        self.height = height
        self.weight = weight
        self.name = name

    @property
    def bmi(self):
        return self.weight / (self.height * self.height)


pl = People('kk', 80, 1.73)
print(pl.bmi)
