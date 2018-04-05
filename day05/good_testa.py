# 三、简单购物车,要求如下：（明天默写的代码）
#     实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入　　
#
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}


goods = []
while True:
    for k,v in msg_dic.items():
        print('商品名称：%s ---- 价格：%s' %(k,v))
        goodname = input('请输入名称：').strip()
        if goodname not in msg_dic:
            print('商品名称不存在；重新输入')
            continue
        price = msg_dic[goodname]
        while True:
            count = input('请输入购买数量').strip()
            if count.isdigit():
                count = int(count)
                break
            else:
                print('输入的数量不正确，重新输入')

        info ={
            'name':goodname,
            'price':price,
            'count':count,
        }
        goods.append(info)
        print(goods)