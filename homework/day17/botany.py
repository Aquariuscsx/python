class Botany:
    def __init__(self, kind , len, color):
        self.kind = kind
        self.len = len
        self.color = color

    def show(self):
        print(self.kind, self.len, self.color)

class Flower(Botany):
    def __init__(self, kind, len, color, flowers):
        Botany.__init__(self, kind, len, color)
        self.flowers = flowers

    def bioom(self):
        print('%s 可以开花'% self.kind)

class Grass(Botany):
    def __init__(self,kind , len, color, life):
        Botany.__init__(self,kind , len, color)
        self.life = life

    def weed(self):
        print('除草!')

if __name__ == '__main__':
    botany = Botany('植物', '3m' ,'红色')
    flower = Flower('油菜花', '1.5m', '黄色', '花朵')
    grass = Grass('狗尾草', '0.5m', '绿色', '生命')
    grass.weed()
    flower.show()
    grass.show()