#!/usr/bin/env python3
# encoding: utf-8
# by fixdq



class Dog:
    def __init__(self, name, d_t, aggresivity, life_value):
        self.name = name
        self.d_t = d_t
        self.aggresivity = aggresivity
        self.life_value = life_value

    def bite(self, dog):
        dog.life_value -= self.aggresivity
        info = ('''
        {dog_name} 发起了攻击，
        {dog2_name} 收到攻击，损失{life_value} 点生命
        {dog2_name} 还有 {ban_value} 点生命
        ''').format(
            dog_name=self.name,
            dog2_name=dog.name,
            life_value=self.life_value,
            ban_value=dog.life_value,
        )
        print(info)


dog1 = Dog('YL','雪原冰犬',20,34563456)
dog2 = Dog('HHK','丧心病狂犬',30,500456630)






while True:
    if dog1.life_value < 0:
        print('%s已经阵亡' % dog1.name)
        break
    if dog2.life_value < 0:
        print('%s已经阵亡' % dog2.name)
        break
    dog1.bite(dog2)
    dog2.bite(dog1)