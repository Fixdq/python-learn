import os
# #方式一 全部都到内存进行修改
#
# with open('db.txt','r',encoding='utf-8') as f:
#     data = f.read()
#     data = data.replace('123456','456789')
#
# with open('db.txt','w',encoding='utf-8') as f:
#     f.write(data)


#方式二
with open('db.txt','r',encoding='utf-8') as fr,\
    open('db.txt.swap','w',encoding='utf-8') as fw:
    for line in fr:
        if '456789'in line:
            line = line.replace('456789','123456')
            fw.write(line)
os.remove('db.txt')
os.rename('db.txt.swap','db.txt')
