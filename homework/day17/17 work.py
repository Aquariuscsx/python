class Tang:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('{}吃饭'.format(self.name))

    def learn(self):
        print('%s去取经'% self.name)



class Wukong(Tang):
    def __init__(self, name, age, weapon):
        Tang.__init__(self, name, age)
        self.weapon = weapon

    def dark(self):
        print('悟空除妖!!')



class Pig(Tang):
    def __init__(self, name, age, wife):
        self.wife = wife
        Tang.__init__(self,name, age)

    def horse(self):
        print('{}是牵马的'.format(self.name))



class Monksand(Tang):
    def __init__(self,name, age, home):
        Tang.__init__(self,name, age)
        self.home = home

    def coolie(self):
        print('%s是挑行李的'% self.name)


if __name__ == '__main__':
    tang = Tang('唐僧', 20)
    sun = Wukong('孙悟空', 500, '如意金箍棒')
    pig = Pig('猪八戒', 38, '高老庄第一美')
    sha = Monksand('沙和尚', 89, '流沙河')
    sha.coolie()
    sun.eat()
    pig.learn()
    pig.horse()
