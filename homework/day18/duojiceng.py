# # class A:
# #     pass
# #
# # class B(A):
# #     pass
# #
# # class C:
# #     pass
# #
# # class D(C):
# #     pass
# #
# # class E( B, D):
# #     pass
# class Person(object):
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self._height = height
#
#
# class Father(Person):
#     def __init__(self,name, age, height, money):
#         super().__init__(name, age, height)
#         self.money = money
#
#     def work(self):
#         print('你老爸在拼命工作供你上学')
#
# class Mother(Person):
#     def __init__(self,money, name, age, height ):
#         super().__init__(name, age, height)
#         # self.name = name
#         # self.age = age
#         # self._height = height
#         self.money = money
#
#     def work(self):
#         print('你老妈在拼命工作供你上学')
#
#     def boy(self):
#         print('生育')
# # super 在继承中,重写了父类方法时,调用父类时用
# #super().父类方法(参数...)
# class Chind(Father, Mother):
#     def __init__(self,money, name= None, age = 1, height = 175):
#        super().__init__(money)
#
#     def show(self):
#         print('我是')
#
# if __name__== '__main__':
#     chind = Chind(1000)
#     chind.show()
'''
1.重写 __new__()
2.创建一个私有的静态变量 __instance = None
3.判断(类变量)静态变量是否为None 如果为None 表示第一次执行该对象NEW方法
4.new  底层创建新的对象


'''

class  Play(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, source):
        self.source = source

    def play(self):
        print(self.source)

if __name__ == '__main__':
    mp1 = Play('凉凉')
    mp1.play()
    print(id(mp1))

    mp2 = Play('远走高飞')
    mp2.play()
    print(id(mp2))
    # print(mp1 is mp2)