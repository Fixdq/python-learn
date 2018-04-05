# encoding: utf-8
# by fixdq

# variable = [out_exp_res for out_exp in input_list if out_exp == 2]
#   out_exp_res:　　列表生成元素表达式，可以是有返回值的函数。
#   for out_exp in input_list：　　迭代input_list将out_exp传入out_exp_res表达式中。
#   if out_exp == 2：　　根据条件过滤哪些值可以。

var =[item for item in range(10) if item % 2 == 0]
print(var)

gen=('egg%s' %i for i in range(10) if i > 5)
print(gen)
print(list(gen))
