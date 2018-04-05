msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}

# gds=[]
# while True:
#     for i in msg_dic:
#         print('%s---%s' % (i,msg_dic[i]))
#     gds_name = input('请输入商品名称:').strip()
#     gds_count = input('请输入购买数量:').strip()
#     if not gds_name or gds_name not in msg_dic:
#         print("你输错了,再输一次")
#         continue
#     if not gds_count:
#         print("你输错了,重新输一次")
#         continue
#     gds.append((i,msg_dic[i],gds_count))
#     print(gds)

# str = '1122334455'
#
# print(str[1:5:3])

for i in msg_dic:
    print(i)

print('------------------------')

for i in msg_dic:
    print(i,msg_dic[i])

print('------------------------')

for i in msg_dic.items():
    print(i)
    print(i[0],i[1])
print('------------------------')
for i in msg_dic.keys():
    print(i)
print('------------------------')
for i in msg_dic.values():
    print(i)

print('------------------------')
for k,v in msg_dic.items():
    print(k,v)

print('------------------------')

print(msg_dic.get('mac'))
print(msg_dic.get('sssssssssssss'))
print(msg_dic['mac'])
print('------------------------')
res = msg_dic.setdefault('mac',8000)
print(res)
res = msg_dic.setdefault('tt')
print(res)
print(msg_dic.setdefault('tt'))
print(msg_dic.setdefault('yy','yy'))


for k,v in msg_dic.items():
    print(k,v)
print('------------------------')
print('------------------------')
