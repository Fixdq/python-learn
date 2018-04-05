# a = 1
# b = 1
# c = 1
# #对于这种变量值都是相同的变量，可以采用下面的连试赋值方式一起赋值
#
# a= b= c= 1
#
# print(id(a),a)
# print(id(b),b)
# print(id(c),c)

# m=1
# n=2
#
# # temp=m
# # m=n
# # n=temp
# # print(m,n)
#
# m,n=n,m
# print(m,n)

#这里是一个列表
# nums = [1,2,3,4]
# a,b,c,d = nums
# print(a,b,c,d)
#
# nums = [1,2,3]
# a,b,c,d = nums

nums = [1,2,3,4,5]
a,*_,b = nums
print(a,b)
print(a)