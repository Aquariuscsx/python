class Shop:
    goods = [
        {"name": "电脑", "price": 1000},
        {"name": "Iphone", "price": 1200},
        {"name": "豪车", "price": 3280},
        {"name": "别墅", "price": 6500},
        {"name": "游艇", "price": 5800},
        {"name": "美女", "price": 2500}, ]
    good = []  # 购物车
    moneys = int(input('总金额:\n'))
    print('余额为: %s'%moneys)
    def __init__(self, name, price):
        self.name = name
        self.price = price



    # def balances(self, moneys):
    #     moneys = int(input('总资产:\n'))
    #     print('已有金额%s'% moneys)

    @classmethod
    def export(cls):
        money = int(input('请输入金额:\n'))
        for i in cls.goods:
            if int(i['price']) > money:
                print('输入有误,请重新输入')
            else:
                print('您输入的金额是:{}'.format(money))
            return
    @classmethod
    def show(cls):
        '''
        :return:
        '''
        if cls.goods:
            i = 0
            for shop in cls.goods:
                i += 1
                print(i, shop)
    @classmethod
    def shop_car(cls, shop_num):
        """

        :param shop_num: 商品列表的长度
        :return: 显示所有商品的数据
        """
        shop = cls.goods[shop_num - 1]
        cls.good.append(shop)
        count = 0
        #判断shopping是加入购物车的商品
        for shopping in cls.good:
            #如果商品的名称等于已加入的商品的名称
            if shopping['name'] == shop.get('name'):
                count += 1
        print(shopping,'*', count )

    @classmethod
    def bare(cls):
        if cls.good:
            print('已选择的商品有 %s ,是否结算?'% cls.good)

        else:
            print('请填充购物车!')
    # @classmethod
    # def delete(cls,del_shop):
    #
    #     for shop in cls.good:
    #         if shop.get('name') == del_shop.name:
    #             cls.good.remove(shop)












if __name__ == '__main__':
    Shop.export()
    Shop.shop_car(4)
    Shop.shop_car(4)
    Shop.bare()


    # shops.shop_car(4)
    # shops.shop_car(4)
    # shops.shop_car(6)
    # shops.shop_car(6)
    # shops.shop_car(6)





