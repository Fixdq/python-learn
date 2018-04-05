# encoding: utf-8
# by fixdq

# x = 10
# y = 1000
#
# res = x if x > y else y
#
# print(res)

#
# def max2(x, y):
#     return x if x > y else y
#
#
# print(max(100000, 2345245245245325))
#


# count = 0
# def foo():
#     global count
#     count +=1
#     print('hts%s' % count)
#
#     foo()
#
# foo()
#
#
#
# def age(n):
#     if n == 100:
#         return 2
#     return age(n - 1) + 3
#
#
# res = age(1000)
# print(res)
from functools import reduce

# f = lambda n: n ** 2
# print(f(100))

names = ['yangli', 'shudong', 'yite', 'fixd']
#
# # res = map(lambda x: '%s_SB' % x, names)
# # print(list(res))
#
# res1 = map(lambda x: '%s_NB' % x if x == 'fixd' else '%s_SB' % x, names)
# print(list(res1))


res3 = reduce(lambda x, y: x + ' ' + y, names)

print(res3)

#
# res = filter(lambda x: x.endswith('e'), names)
# print(list(res))
