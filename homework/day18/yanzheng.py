# import random
# class Code(object):
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def show(self):
#         num = random.randint(1, 10)
#         print(num, end = ' ')
#
# if __name__ == '__main__':
#     num= Code()
#     for i in range(0,4):
#         num.show()
#
# class Log:
#     obj = []
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def show(cls, stu):
#         cls.obj.append(stu.name)
#         print(cls.obj)
#
# if __name__ == '__main__':
#     ni = Log('yu ')
#     ni.show(ni)
#     li = Log('猫')
#     li.show(li)
class Zoology:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('你是%s'% self.name)

class Pig(Zoology):
    def __init__(self,name):
        self.name = name

class Cat(Zoology):
    def __init__(self,name):
        self.name = name

class Dog(Zoology):
    def __init__(self,name):
        self.name = name

# class Person(Zoology):
#     def __init__(self,name):
#         self.name = name

# def feed_animal(Zoology):
#     print('%需要喂养'%(feed_animal.eat()))
    # feed_animal.eat()
    # feed_animal.eat()


class Test:

    @staticmethod
    def eat(dog):
        dog.eat()

    @staticmethod
    def eat(dog):
        dog.eat()




if __name__ == '__main__':
    dog = Dog('狗')
    dog.eat()
    Test.eat(dog)
    pig = Pig('zhu')
    Test.eat(pig)