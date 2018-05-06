# with open('home.txt', 'w', encoding = 'utf-8') as fw:
#     list = [22, 4, 6, 8, 10, 334, 779, 234, 54, 666]
#     list.sort()
#     # for nums in list:
#     fw.write(str(list))
#     fw.flush()
# with open('home.txt', 'w', encoding = 'utf-8') as fw:
#     string = '入夜渐微凉 繁花落地成霜 你在远方眺望 耗尽所有暮光 不思量自难相忘'
#     fw.write(string)
#     fw.flush()
# with open('home.txt', 'w', encoding = 'utf-8') as fw:
#     tuple = ('python','java','php','Android','IOS')
#     # for nums in tuple:
#     fw.write(str(tuple))
#     fw.flush()

# with open('home.txt', 'w', encoding = 'utf-8') as fw:
#     list = {}
#     for key, value in list.items():
#         fw.write(str(key))
#         fw.write(str(value))

# dict = {'a': 34, 'd': 66, 'cd': 99, 'b': 70}
# list = []
# for key, value in dict.items():
#     list.append(key)
#     list.append(value)
# print(tuple(list))
# for key in dict:
#     list.append(key)
# print(list)
# dict1 = {'a': 34, 'd': 66, 'cd': 99, 'b': 70}
# dict2 = {'c': 55, 'm': 77, 'e': 99}
#
# complex(dict1, dict2)


# def compute():
#     s = 'python8832  def中文 afdafsd'
#     num_count = 0
#     pha_count = 0
#     space_count = 0
#     split_count = 0
#     for i in s:
#         if i.isdigit():#判断是否是数字
#             num_count += 1
#         elif i.isalpha():#判断是否是 字母
#             pha_count += 1
#         elif i.isspace():#判断是否是空格
#             space_count += 1
#         else:#如果都不是就
#             split_count += 1
#     print(num_count)
#     print(pha_count)
#     print(space_count)
#     print(split_count)
# compute()
# def outer(num):
#     def inner():
#        for key,value in num.items():
#            if len(value) > 2:
#                 print(value[2:])
#     return inner
#
# nums = outer({'a': '341213', 'd': '66', 'cd': '99', 'b': '70'})
# nums()
#
#
grade ={'zhangsan':50, 'zhangsa':5, 'zhangs':64, 'zhang':464, 'zhan':64, 'chengsa':58, 'chengs':34, 'cheng':95, 'chen':86, 'chengsan':50}
# def comepare():
#    nums = list(grade.values())#把value的字符串转成列表
#    nums.sort(reverse = True)
#    print(nums)
# comepare()
# def outer():
#     nums = grade.values()
#     value = min(nums)
#     for key in grade.keys():
#         if grade[key] == value:
#             print('分数最高的人是{},分数是{}'.format(key, value))
# outer()
#
# def average():
#     values = 0#总分
#     person = 0#总人数
#     total = 0#平均分
#     for key,value in grade.items():
#          if key:#不为空就进入下一步
#              person += 1
#              values += value
#     total = values / person
#     print(total)
with open('home.txt', 'r', encoding='utf-8') as fr:
    while True:
        a = fr.readline()
        if a:
            if 'pass' in a:
                print(a)
            else:
                pass
        else:
            break