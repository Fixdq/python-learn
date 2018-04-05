#一：
name = ' aleX'
print(name.strip())
print(name.startswith('al'))
print(name.endswith('X'))
print(name.replace('l','p'))
print(name.split('l'))
print(name.upper())
print(name.lower())
print(name[1:])
print(name[:3])
print(name[-2:])
print(name.find('e'))
print(name[:-1])

#二
#1
data=['alex',49,[1900,3,18]]
name = data[0]
age = data[1]
y,m,d = data[2]
print(name)
print(age)
print(y)
print(m)
print(d)

#2
#队列
ls = [1,2,4,5,6]
ls.append(1)
ls.append(2)
ls.append(3)
print(ls.pop(0))
print(ls.pop(0))
print(ls.pop(0))

ls = [1,2,4,5,6]
ls.insert(5,'s')
ls.insert(len(ls),'2')
ls.insert(len(ls),'3')
ls.insert(len(ls),'4')
ls.insert(len(ls),'5')
print(ls.pop(0))
print(ls.pop(0))
print(ls.pop(0))
print(ls.pop(0))
print(ls.pop(0))

#堆栈
ls = [1,2,4,5,6]
ls.insert(5,'s')
ls.insert(len(ls),'2')
ls.insert(len(ls),'3')
ls.insert(len(ls),'4')
ls.insert(len(ls),'5')
print(ls.pop())
print(ls.pop())
print(ls.pop())
print(ls.pop())
print(ls.pop())


#3
#
# for i in range(1,10):



# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={} '.format(j,i,i*j),end='')
#     print()

h =50
for i in range(h):
    for j in range(i,h-1):
        print(' ',end = '')
    for k in range(2*i+1):
        print('*',end = '')
    print()


