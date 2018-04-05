tuples = tuple(range(5))
print(tuples)



#计算元组长度
tuples = (0, 1, 2, 3, 4)
print(len(tuples)) #结果: 5

# in 和not in
tuples = ('a','b','c','d')
print('a' in tuples)        #结果：True
print('z' in tuples)        #结果：False
print('x' not in tuples)    #结果：True
print('d' not in tuples)    #结果：False


#元组的取值
tuples = ('a','b','c','d')

item = tuples[0]
print(item)                 #结果：a
item = tuples[2]
print(item)                 #结果：c

#while循环
c = 0
while c < len(tuples):
    print(tuples[c])
    c+=1
#for循环
for item in tuples:
    print(item)


dic={'name':'fixd','age':18}
print(dic)
res=dic.pop('name')
print(res)              #fixd
print(dic)              #{'age': 18}

dic={'name':'fixd','age':18}
res=dic.pop('sex',None)
print(res)              #one

dic={'name':'fixd','age':18}
res = dic.popitem()
print(res)              #('age', 18)  这个值不是确定的，一般会从结果删除



dic={'name':'fixd','age':18}
dic2={'name':'yite','age':18,'hobby':'music'}
dic.update(dic2)
print(dic)      #{'name': 'yite', 'age': 18, 'hobby': 'music'}
#对与老字典来说，更新指的是，新字典中有而老字典中没有则添加，新有而老有，则覆盖

dic={'name':'fixd','age':18}
print('name' in dic)        #True
print('age' in dic)         #True
print('hobby' in dic)       #False
print('hobby' not in dic)   #True
print()
print()
print()


#三种不同方式的取值
dic={'name':'fixd','age':18}
print(dic.keys())
#keys()
for x in dic.keys():
    print(x)
    print(x,dic[x])
#values()
for value in dic.values():
    print(value)
#items()
print(dic.items())
for k,v in dic.items(): #k,v=('name', 'egon')
    print(k,v)

print(type(dic.items()))






