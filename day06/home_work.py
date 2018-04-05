# 1、什么是字符编码？

# 2、保证不乱码的核心法则是？
#用什么编码存，就用什么编码取
# 3、循环读取文件内容

# 4、编写用户注册程序，

# 用户选择注册功能则：
# 将用户输入用户名、性别、年龄等信息存放于文件中
# 用户选择查看功能：
# 则将用户的详细信息打印出来
#

# z_name = input('name==>')
# z_age = input('age==>')
# z_sex = input('sex==>')
with open('user.txt','r',encoding='utf-8') as f:
    res = f.readline()
    print(eval(res))
    # print(type(dict(res)))
    print(type(eval(res)))


z_pwd = input('pwd==>')
#判断用户是否存在





# 5、编写用户认证接口，其中用户的账号密码是存放文件中的。

# name = input('name==>')
# pwd = input('pwd==>')
# with open('user.txt','r',encoding='utf-8') as f:
#     pass
#


#默写
# 1、python3中的unicode转成其他编码称为编码还是解码，使用的方法是什么，得到的结果是什么类型
    #编码 encode  bytes

# 2、python3中的bytes类型转成unicode的过程称为编码还是解码，使用的方法是什么，得到的结果是什么类型
    #解码 decode  unicode

# 3、默认处理文件的房是t文本模式，操作文件的三种纯静模式是r，w，a，请分别介绍三种模式的作用，以及在文件存在和不存在的两种情况下有何特殊之处？
#                   存在                          不存在
# r 只读          不报错                            报错
# w 只写          直接覆盖                      创建空文档，写入内容
# a 在末尾追加     直接在末尾追加                   创建空文档，写入内容

# 4、打开文件写入，保证新写入的内容总是置于文件末尾

with open('w.txt',mode='a',encoding='utf-8') as f :
    f.write('ssssssssssssssssss')

# 5、循环读取文件每一行内容

with open('w.txt',mode='r',encoding='utf-8') as f :
   for item in f:
       print(item)