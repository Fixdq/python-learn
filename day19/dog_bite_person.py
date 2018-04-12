#!/usr/bin/env python3
# encoding: utf-8
# by fixdq


class Person:
    def __init__(self, name, agg, health=100):
        self.name = name
        self.agg = agg
        self.health = health

    def bite(self, enemy):
        enemy.health -= self.agg
        print('人：%s bite 狗：%s  品种：%s  伤害：%s   狗剩余生命：%s' %
              (self.name, enemy.name, enemy.breed, self.agg, enemy.health))


class Dog:
    def __init__(self, name, agg, breed, health=100):
        self.name = name
        self.breed = breed
        self.agg = agg
        self.health = health

    def bite(self, enemy):
        enemy.health -= self.agg
        print('狗：%s 品种：%s bite 人：%s  伤害：%s   狗剩余生命：%s' %
              (self.name, self.breed, enemy.name, self.agg, enemy.health))


p = Person(name = 'Yxx', agg = 5)
d = Dog(name = 'Yxx', agg = 10, breed='雪中豹')

while True:
    p.bite(d)
