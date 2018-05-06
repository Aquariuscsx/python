"""
1. 每个类提供显示的方法
2. 使用统一的管理类(Manager)
   用户类
   图片类
   品牌类
   意见类
用列表来装
提供一下方法
增  批量添加,单个添加
删 单个删除 ,批量删除
改  修改单个对象
查  根据id查询单个对象 查询所有的信息
"""

class Managers(object):
    list_manager = []
    def __init__(self, type, type2, type3, type4):
        self.type = type
        self.type2 = type2
        self.type3 = type3
        self.type4 = type4
        self.manager = {}

    def show(self):
        self.manager = {'type': self.type,'type2': self.type2,'type3': self.type3,'type4': self.type4}
        self.list_manager.append(self.manager)
        print('管理类%s'%self.list_manager)

    def delete(self,get_type):
        for typ in self.list_manager:
            if typ.get('type') == get_type.type:
                self.list_manager.remove(typ)

    def up_manager(self, up_man, up_men):
        for managers in self.list_manager:
            if managers == up_man.type:
                managers.update(type = up_men.type,type2 = up_men.type2,type3 = up_men.type3,type4 = up_men.type4)
                print('修改后的类型1是{},类型2是{},类型3是{},类型4是{}'.format(type=up_men.type,type2 = up_men.type2,type3=up_men.type3,type4=up_men.type4,))


class Users:
    list_user=[]
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.guan = {}


    def show(self,):
        self.user = {'name': self.name,'sex': self.sex,'age': self.age}
        self.list_user.append(self.user)
        print('用户类%s'%self.list_user)

    def delete(self, lad_user):
        for users in self.list_user:
            if users.get('name') == lad_user.name:
                self.list_user.remove(users)

    def up_user(self, up_us, up_er):
        for pat in self.list_user:
            if pat.get('name') == up_us.name:
                pat.update(name= up_er.name, sex= up_er.sex, age= up_er.age)
                print('修改后的名字是{},性别是{},年龄是{}'.format(up_er.name,up_er.sex,up_er.age))

    def find(self, quran):
        for finds in self.list_user:
            if finds.get('name') == quran.name:
                print('名字是{},性别是{},年龄是{}'.format(quran.name,finds.get('sex'),finds.get('age')))
            break
class Picturys:
    list_pictury = []
    def __init__(self, kind, size,):
        self.kind = kind
        self.size = size
        self.pictury = {}

    def show(self):
        self.pictury = {'name': self.kind,'sex': self.size}
        self.list_pictury.append(self.pictury)
        print('用户类%s'%self.list_pictury)

    def delete(self, lad_pictury):
        for jap in self.list_pictury:
            if jap.get('name') == lad_pictury:
                self.list_pictury.remove(jap)






class Brands:
    list_brand = []

    def __init__(self, kind, name, age):
        self.kind = kind
        self.name = name
        self.age = age
        self.brand = {}

    def show(self):
        self.brand = {'name': self.kind, 'sex': self.name,'age':self.age}
        self.list_brand.append(self.brand)
        print('用户类%s' % self.list_brand)

    def delete(self,lad_brand):
        for brand in self.list_brand:
            if brand.get('name') == lad_brand:
                self.list_brand.remove(brand)

class Ideas:
    list_idea = []

    def __init__(self, kind):
        self.kind = kind
        self.idea = {}

    def show(self):
        self.idea = {'name': self.kind}
        self.list_idea.append(self.idea)
        print('用户类%s' % self.list_idea)

    def delete(self, lad_idea):
        for idea in self.list_idea:
            if idea.get('name') == idea.name:
                self.list_idea.remove(idea)



if __name__ == '__main__':
    user = Users('用户',18, 'nu')
    user1 = Users('用户',18, 'nu')
    user.show()
    user1.show()
    #添加
    manager = Managers('用户类','图片类','品牌类','意见类')
    manager.show()
    user.delete(user)
    print(Users.list_user)
    user.find(user)









