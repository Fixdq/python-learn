
dic = {'name':'Fixd','age':18}

dic={'name':'Fixd'}
dic['age']=10       #增加操作
print(dic)
dic['name']='Fixd'  #重新赋值
print(dic)
print('name')       #取值操作


dic = {'name':'Fixd','age':18}
print(len(dic))     #获取长度 结果：2

# setdefaul的用处：
# 1、字典有中有key，则不修改，返回原key对应的原值
dic={'name':'Fixd','age':18}
res=dic.setdefault('name','FIXD')
print('返回值',res)        #结果：返回值 Fixd
print(dic)                 #结果：{'name': 'Fixd', 'age': 18}

# 2、没有对应的key，则添加，返回添加的key对应的value
dic={'age':18}
res=dic.setdefault('name','FIXD')
print('返回值',res)        #结果：
print(dic)                #结果： {'age': 18, 'name': 'FIXD'}


