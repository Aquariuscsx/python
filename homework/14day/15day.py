# class User:
#     cunty = 'china'
#     def __init__(self, name):
#         self.name = name
#     @classmethod
#     def cls_method(cls, test):
#        print(test)
# #在类方法中是无法使用实例变量的  可以使用静态方法
# if __name__ == '__main__':
#     User.cls_method('23424255')
#     user = User('qiuming san')
#     user.cls_method('999999')
class BankCard:  # 银行卡
    def __init__(self, account, balance, ):  # 余额
        self.account = account  # 帐户名
        self.balance = balance

    def deposits(self, money):  # 存款
        if money > 0:  # 存款大于0,存款成功
            self.balance += money
            print('存款金额{},存款成功'.format(self.money))
        else:
            print('输入有误')


    def withdrawals(self, money):
        if 0 < money <= self.balance:  # 当取款金额小于等于余额
            self.balance -= money
            print('取款金额{},取款成功'.format(self.money))
        else:
            print('请重新输入')


    def transfer(self, money,):
        if 0 < money <= self.balance:  # 当转账金额小于等于余额
            self.balance -= money
            every1.balance += money
            print('转账金额{},转账成功'.format(self.money))
            print(self.balance)








if __name__ == '__main__':
    every = BankCard(123, 5000)
    every1 = BankCard(234, 5000)
    every.transfer()