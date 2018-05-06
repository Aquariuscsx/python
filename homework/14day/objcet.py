# class Employee:
#
#     def __init__(self,name,job, salary):
#         self.name = name
#         self.job = job
#         self.salary = salary
#
#     def show(self):
#         print('{}是认真工作的人\n'.format(self.name),'{}是公司的牌号\n'.format(self.job),'{}是每个月的工资\n'.format(self.salary))
#
#
# if __name__ == '__main__':
#     employee = Employee('周勇',123,4500)
#     employee.show()
# class Shop:
#     def __init__(self, shop_id,name, price):
#         self.shop_id = shop_id
#         self.name = name
#         self.price = price
#
#     def show(self):
#         print(self.shop_id, self.name, self.price)
#
# class BankCard:  # 银行卡
#     def __init__(self, account_name, balance, deposit, withdrawal, transfer):  # 余额
#         self.account_name = account_name  # 帐户名
#         self.balance = balance
#         self.deposit = deposit
#         self.withdrawal = withdrawal
#         self.transfer = transfer
#
#
#     def deposits(self):  # 存款
#         if self.deposit > 0:  # 存款大于0,存款成功
#             print('存款金额{},存款成功'.format(self.deposit))
#         else:
#             print('请输入存款金额')
#
#     def withdrawals(self):
#         if self.withdrawal <= self.balance:  # 当取款金额小于等于余额
#             print('取款金额{},取款成功'.format(self.withdrawal))
#         else:
#             print('请重新输入取款金额')
#
#     def transfer_accounts(self):
#         if self.transfer <= self.balance:  # 当转账金额小于等于余额
#             print('转账金额{},转账成功'.format(self.transfer))
#         else:
#             print('请重新输入转账金额')
#
#
# if __name__ == '__main__':
#     cunkuan = BankCard(88888888, 1000000, 1000000,20000000,1000)
#     cunkuan.deposits()
#     cunkuan.withdrawals()
#     cunkuan.transfer_accounts()
# class Phone:
#     def __init__(self, brand, model, phonenumber):
#         self.brand = brand
#         self.model = model
#         self.phonenumber = phonenumber
#
#     def show_info(self):
#         print('手机品牌{}\n'.format(self.brand), '手机型号{}'.format(self.model))
#
#     def call(self):
#         print('请拨打您要拨打的电话号码{}'.format(self.phonenumber))
#
#
# if __name__ == '__main__':
#     phone = Phone('华为', 'meat900000',13356783421)
#     # phone = Phone(13356783421)
#     phone.show_info()
#     phone.call()
# class Sdutends:
#
#
#     def __init__(self, name, age, schoolname):
#
#
#         self.name = name
#         self.age = age
#         self.schoolname = schoolname
#
#
#     def eat(self):
#         print('{}在学校吃饭'.format(self.name))
#
#
#     def call(self):
#         print('姓名{}\n'.format(self. name), '年龄{}\n'.format(self.age), '学校名字{}\n'.
#         format(self.schoolname))
#
#     def sduty(self):
#         print('{}在学校学习'.format(self.name))
#
# if __name__ == '__main__':
#     eats = Sdutends('小明', '98', '清华小学')
#     eats.eat()
#     eats.call()
#     eats.sduty()
count = 0
while count < 3:
   username = input('请输入用户名:')
   password = input('请输入密码:')
   if username == 'admin' and password == '123':
       print('登录成功!!!')
       break
   else:
       count += 1
       print('第%s次的机会' % (3 - count))
else:
   print('请三个小时后再试')