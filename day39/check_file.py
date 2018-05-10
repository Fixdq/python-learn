#-*- coding:utf-8 -*-

import os
import sys
import pandas as pd
import openpyxl
path = os.path.dirname(__file__)



file_path_list = os.listdir(path)
print(file_path_list)




data_dic = {}
file_list = []
count_list = []
i = 0
list = []
for file_path in file_path_list:
    if os.path.isfile(file_path) and file_path !=  'check_file.py':
        i += 1
        file_list.append(file_path)
        with open(file_path,'r',encoding='utf-8') as f:
            count = 0
            for line in f:
                if line != '\n' and '#' not in line:
                    count += 1
            count_list.append(count)

        list.append(i)



data_dic['姓名'] = file_list
data_dic['行数'] = count_list





writer = pd.ExcelWriter('/home/fixd/workspace/python_learn/day39/行数.xlsx')
df = pd.DataFrame(data_dic,columns=['姓名','行数'],index=list)
df.to_excel(writer,'sheet1')
writer.save()
print(df)



