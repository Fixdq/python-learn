# encoding: utf-8
# by fixdq


egg_list = []
egg_list = ['鸡蛋%s' % i for i in range(10)]

print(type(egg_list))

egg_gen = ('鸡蛋%s' % i for i in range(10))

print(type(egg_gen))

print(pow(3, 3, 4))
print(round(3, 5))
print('----------------')

sc = slice(2, 2, 2)
l = ['ssss', 'sssss', 'sssssss', 231, 8, 78, 5, 4, 5, 8, 4, 5, 6, ]
print(l[::2])
print(l[sc])

# l = ['这是要上天啊：已经走%s步了' % s for s in range(1000)]
# print(l)
l1 = ['这是要上天啊：已经走%s步了' % s for s in range(10000) if s % 2 != 0]
print(l1)

with open('db.txt', 'r', encoding='utf-8') as f:
    print(max(len(line) for line in f))







