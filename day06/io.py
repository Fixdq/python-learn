#
#
# f = open('user.txt',mode='r',encoding='utf-8')
#
# res = f.read()
# print(res)
# print('==================>')
# print(f.readline())
# f.close()
#

#
# with open('user.txt','r',encoding='utf-8') as f:
#     for i in f:
#         print(i)
#
# with open('a2.txt','w',encoding='utf-8') as  f:
#     f.write("aaaaaaaaaaaaaaaaaaa\nssssssssssssssssss\n")
#
#     f.writelines(['xxxxxx','xxxxssssssss','kkkkkkkkk'])

# f=open('user.txt',mode='r',encoding='utf-8')
# # f.write('哈哈啊哈哈啊啊 啊啊123213213123\n') #抛出异常，不能写
# # print(f.readable())
# print('=============>1')
# print(f.read())
#
# print('=============>2')
# print(f.read())
#
# f.close()

#打开文件(前提 user.txt 存在)
# f = open('user.txt',mode='r',encoding='utf-8')
# print(f.read())
# f.close()

# f = open('user.txt',mode='r',encoding='utf-8')
# print(f.readline())

# f = open('user.txt',mode='r',encoding='utf-8')
# print(f.readlines())

#
# f = open('user.txt',mode='r',encoding='utf-8')
# for i in f:
#     print(i)
# f.close()

# f = open('user.txt',mode='r',encoding='utf-8')
#
# print(f.readline(),end='')
# print(f.readline(),end='')
# print(f.readline(),end='')
# print(f.readline(),end='')
# print(f.readline(),end='')
#
# f.close()

# f = open('user.txt',mode='r',encoding='utf-8')
# f.write()

f=open(r'a1.txt',mode='w',encoding='utf-8') #默认是wt
f.write('第一行\n')
f.write('第二行\n')
f.writelines(['1111\n','2222\n','3333\n'])
f.write('aaaaa\nbbbb\nccccc\n')
