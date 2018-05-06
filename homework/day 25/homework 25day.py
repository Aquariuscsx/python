# import time
#
# def outer(fun):
#     def inner():
#         fun()
#         time2 = time.strftime('%Y-%m-%d %X')
#         with open('log.txt', 'w', encoding='utf-8') as fw:
#             fw.write(time2)
#             fw.flush()
#     return inner
# @outer
# def func():
#     print('努力学习,一定要学好')
#
# func()
import time
class Bank:
    account = {'1001': {'name': 'xiaoming', 'pw': 123, 'money': 150000, 'balance': 150000},
               '1002': {'name': 'xiaohua', 'pw': 123, 'money': 150000, 'balance': 150000}}

    def __init__(self, id,  name, pw):
        self.id = id
        self.name = name
        self.pw = pw
        self.moneys = 15000
        self.balance = 15000
        self.log = [{'月份': '04' , '消费时间': '2018-03-31 10:54:59', '消费金额': 90}]

    def show(self):
        """
        :return: 验证用户信息
        """
        for key, value in self.account.items():
            if self.id == key:#帐户编号正确进入下一步
                print('验证用户成功!正在验证账号密码是否正确!')
                #判断账号密码是否匹配 ,正确
                if self.name == value['name'] and self.pw == value['pw']:
                    print('账号密码正确!!登陆成功!')
                else:
                    print('账号或密码错误')
                break
            else:
                print('无此用户信息!!')

    def withdraw(self,money):#money是提现的金额
        """

        :param money: 提现的金额
        :return: 实现提现的操作
        """
        if money <self.moneys:
            moneys = money - money * 0.05
            self.balance = self.moneys - money
            print('实际提现金额{},余额{},手续费{}'.format(moneys,self.balance, money * 0.05))
        else:
            print('输入金额有误!!')

    def consume(self,money):#money每次消费的金额
        """

        :param money: 每次消费的金额
        :return: 记录每次提现的金额与时间
        """
        all_money = 0#消费的总金额
        all_money += money
        li = {}#记录每次消费的时间与消费金额
        if 0 < money <= self.balance:
            self.balance -= all_money
            consume_time = time.strftime('%Y-%m-%d %X')
            consume_month = time.strftime('%m')
            li = {'月份':consume_month ,'消费时间': consume_time, '消费金额': money}
            self.log.append(li)
            # print(self.log)
        else:
            print('余额不足!!余额{}'.format(self.balance))

    def find_bill(self):
        """

        :return: 输入月份 输出该月份账单
        """
        time = input('请输入要查询的月份')

        #遍历出月份所在的字典,如果字典没有创建,就需要创建一个字典判断它是不是在这个列表里面
        for logs in self.log:
            #如果字典里的月份数据与输入月份相符合
            if logs.get('月份') == time:
                #输出 月份,消费的时间,消费的金额  字典锁定是get,不要遍历出字符串再去比较
                    print(time, logs.get('消费时间'),logs.get('消费金额'))
            else:
                print('本月没有消费信息!!')

    def record(self):
        pass














if __name__ == '__main__':
    wi = Bank('1003','xiaoming', 123)
    # wi.show()
    # wi.withdraw(10000)


    wi.consume(50)
    wi.consume(20)
    wi.consume(90)
    wi.find_bill()
    # wi.consume(20000)

