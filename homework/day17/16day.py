class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def open(self):
        print('餐厅正在营业')

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)




if __name__ == '__main__':
    name = Restaurant('永平酒家', '小白菜')
    name.describe_restaurant()
    ope =Restaurant('永平酒家', '小白菜')
    ope.open()