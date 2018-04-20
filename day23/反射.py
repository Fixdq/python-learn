#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

#
# class People:
#     country = "China"
#
#     def __init__(self, name):
#         self.name = name
#
#     def say_hi(self):
#         print('hello word!')
# p = People('lxx')
#
# print(hasattr(People, 'country'))
# print(setattr(People, 'city', 'shanghai'))
# say = getattr(p, 'say_hi')
# say()
# delattr(People, 'country')
# print(People.__dict__)

#
# class Foo:
#     def run(self):
#         cmd = input('cmd===>')
#         if hasattr(self, cmd):
#             func = getattr(self, cmd)
#             func()
#
#     def download(self):
#         print('downloading.......')
#
#     def upload(self):
#         print('uploading.......')
#
# foo = Foo()
# foo.run()



class BlackMedium:
    feature = "ugly"

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def sell_house(self):
        print("%s黑中介买房子" % self.name)

    def rent_house(self):
        print("%s黑中介买房子" % self.name)


b1 = BlackMedium("挽歌地产", '天空之城')

# 获取属性
print(hasattr(b1, 'name'))
res = hasattr(b1, 'name')
print(res)
if hasattr(b1, 'sell_house'):
    func = getattr(b1, 'sell_house')
    func()
# 报错
# getattr(b1,'sdfsdf')

if hasattr(b1, 'name'):
    name = getattr(b1, 'name')
    name = 3
print(b1.__dict__)

setattr(b1, 'city', 'zux')
setattr(b1, 'name', '黑心')

print(b1.__dict__)

setattr(b1, 'show_name', lambda self: self.name + 'sb')

b1.show_name(b1)
print(b1.show_name(b1))
print(b1.__dict__)

if hasattr(b1, 'show_name'):
    delattr(b1, 'show_name')
print(b1.__dict__)

print(BlackMedium.__dict__)
if hasattr(BlackMedium, 'feature'):
    setattr(BlackMedium, 'feature', 'charming')
print(BlackMedium.__dict__)
