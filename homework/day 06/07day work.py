# import random  # 导入模块
# num = random.choice(range(1, 7))
# print(num)
# import random  # 导入模块
# num = random.choice(range(1, 7))
# print(num)
# import random  # 导入模块
# num = random.choice(range(1, 7))
# print(num)
# import random
#
# num = random.random()
#
# print(num)
# seq = '12345'
# print(seq[:])
# import random
# stake = 5000#本金
# tatol = random.choice(range(3, 18))#随机数
# count = input('请选择押大押小:\nA押大\nB押小\n')#押大小
# if count == 'A':
#     print('你选择押大')#押大
#     day = int(input('请输入下注金额:\n'))#下注
#     if tatol >=11:
#         stake += day
#         print('你赢了,本金剩余:',stake)#赢了
#         print('点数{}'.format(tatol))#掷的点数
#     else:
#         stake -= day
#         print('你输了,本金剩余:',stake)
#         print('点数{}'.format(tatol))  # 掷的点数

import random
stake = 5000#本金
tatol = random.choice(range(3, 18))#随机数
i = 0
while i < 1000 and i% 50 == 0:



    count = input('请选择押大押小:\nA押大\nB押小\n')#押大小
    if count == 'A':
        print('你选择押大')#押大
        i = int(input('请输入下注金额:\n'))#下注
        # if tatol >=11:
        #     stake += i
        #     print('你赢了,本金剩余:',stake)#赢了
        #     print('点数{}'.format(tatol))#掷的点数
        # else:
        #     stake -= i
        #     print('你输了,本金剩余:',stake)
        #     print('点数{}'.format(tatol))  # 掷的点数
        if stake < i:
            day = input('请选择:\你A:充值\nB:重新下注\nC:退出\n')
            if day == 'A':
                print(' 请输入充值金额;')
            elif day == 'B':
                print('请重新下注')
            else:
                print('请退出')





