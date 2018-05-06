class Phone:
    phone_id = 0
    def __init__(self, brand, model, price, count, version):
        Phone.phone_id += 1
        self.phone_id = Phone.phone_id
        self.brand = brand
        self.model = model
        self.price = price
        self.count = count
        self.version = version


class Function:
    phone_list = []

    @classmethod
    def add_phone(cls, phone):
        # cls.add_brand = input('')
        cls.phone_list.append(phone)
    @classmethod
    def query_all_phone(cls):
        for phone_lists in cls.phone_list:
            print(phone_lists)

    @classmethod
    def query_phone(cls, brand):
        if cls.phone_list:
            for phone_lists in cls.phone_list:
                if phone_lists.brand.find(brand) != -1:
                    print(phone_lists)







if __name__ == '__main__':
    phone_brand = input('品牌')
    phone_model = input('类型')
    phone_price = float(input('价格'))
    phone_count = int(input('数量'))
    phone_version = input('版本')
    phone_lists = {'brand': phone_brand, 'model': phone_model, 'price': phone_price, 'count': phone_count, 'version': phone_version}
    Function.add_phone(phone_lists)
    # Function.query_all_phone()
    brand = input('输入查询的数据')
    Function.query_phone(brand)

    print(Function.phone_list)




