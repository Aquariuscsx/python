shops = []#所有的商品数据
shop_car = []#保存用户购买的商品信息
def add_shop(name, price, inc):#添加商品
    shop = {'name':name,'price':price,'inc':inc}
    shops.append(shop)
    return shops

def delete_shop(name):#删除商品
    #判断是否存在商品信息
    if shops:
        #遍历所有的商品信息
        for shop in shops:
            #如果商品存在
            if name == shop.get('name'):
                shops.remove(shop)
                break

def show_shop():#选择要加入购物车的商品
    print('请选择您要购买的商品编码')
    i = 0
    for shop in shops:
        i += 1
        print(i, shop)

def choose_shop(shop_num):#加入购物车
    shop = shops[shop_num - 1]
    shop_car.append(shop)

def pay():#结算
    money = 0
    if shop_car:
        for shop in shop_car:
            money += shop.get('price')
    print('商品的总价{}'.format(money))


add_shop('iphoneX',8000,'张碧状元')