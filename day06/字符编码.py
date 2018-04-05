#coding:utf-8






max_layer = 50
for current_layer in range(1,max_layer+1):
    # print(current_layer)
    # 打印空格
    for i in range(max_layer - current_layer):
        print(' ',end='')

    # 打印星号
    for j in range(2*current_layer-1):
        print('*',end='')

    print()
