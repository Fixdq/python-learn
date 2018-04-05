# encoding: utf-8
# by fixdq


#
# def muji():
#     print('------------->>>>>>>>>>11')
#     yield 1
#     print('------------->>>>>>>>>>22')
#     yield 2
#     print('------------->>>>>>>>>>33')
#     yield 3
#     # print('------------->>>>>>>>>44')
#
# gend = muji()
#
# print(gend.__next__())
# print(gend.__next__())
# print(gend.__next__())
# # print(gend.__next__())
#
#
#
#
#
# def pt():
#     n = 0
#     while True:
#         yield n
#         n+=1
#
#
# generrator = pt()
#
# print(generrator.__next__())
# print(generrator.__next__())
# print(generrator.__next__())
# print(generrator.__next__())
# print(generrator.__next__())


# def my_ragnge(start, stop, step=1):
#     n = start
#     while n < stop:
#         yield n
#         n += step
#
#
# for i in range(100):
#     print(i)





def dog(name):

    while True:
        food = yield
        print("%s正在吃%s" % (name,food))

dog=dog('jjjj')
dog.__next__()
print(dog.send('ddd'))
print(dog.send('fff'))

