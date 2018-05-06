# class User:
#     __county = 'china'
#     def __init__(self,name, age):
#         self._name = name
#         self.__age = age
#
#
#     def outer(self):
#         print(self._name)
#
#     def inner(self):
#         print(self.__age)
#
# if __name__ == '__main__':
#     name = User('lipeng',38)
#
#     use = User('lipeng',38)
#     use.inner()

#     def __init__(self, name, road):
#         self.name = name
#         self.road = road
#
#
# class Cat(Heor):
#     def __init__(self, name, road, len):
#         Heor.__init__(self,name, road)
#         self.len = len
#
#
#     def catch(self):
#         print('捉老鼠')
#
# class Dog(Heor):
#     def __init__(self, name, road, jiao):
#         self.jiao = jiao
#         Heor.__init__(self, name, road)
#
#     def accack(self, jiao):
#         print(self.jiao)
#
# if __name__ == '__main__':
#     user = Cat('小猫','人',5.5)
#     dog = Dog('小狗', '狗', '汪汪')
#     user.catch()
#     print(user.len)
#     print(dog.name)
#     print(dog.jiao)
#     dog.accack(user)
#

name = ' aleX '
print(name.strip())
print(name.startswith('al'))
print(name.endswith('X'))
print(name.replace('l','p'))
print(type(name.split('l')))
print(name.upper())
print(name.lower())
print(name[1])
print(name[0:3])
print(name[-2:])
print(name.index('e'))
for i in name:
    print(i)




