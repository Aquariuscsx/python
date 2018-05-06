# 第一题
# import random #导入模块
# def throw():
#     print('开始掷骰子')
#     sun = 3#骰子数3个
#     tatol = 0#声明总点数
#     tatol1 = random.choice(range(1,6))
#     tatol2 = random.choice(range(1,6))
#     tatol3 = random.choice(range(1,6))
#     tatol= int(tatol1 + tatol2 + tatol3) #随机数
#     if tatol > 10:
#         print('结果为大{}'.format(tatol))#掷的数大于10,就是开大
#     else:
#         print('结果为小{}'.format(tatol))#掷的数小于等于10,就是开大
#
# throw()
#第二题
#  def judge(num):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 print(num, '不是质数')
#                 print(i, '*',num // i, '是',num,)
#                 break
#         else:
#             print(num,'是质数')
# judge(int(15))
def count(num1, num2):
    sun = 0#质数之和
    if num1 > 1 and num2 > 1:
        for num in range(num1, num2):
            # for i in range(2, num):
                if (num % 2) == 0:
                   print(num, '不是质数')

        else:
            print(num,'是质数')
            sun+=num
        print(sun)
print(count(2, 18))
