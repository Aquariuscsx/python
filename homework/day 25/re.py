# 用来匹配字符串的
# str.find()


"""
元字符 (通用的)
普通字符
特殊
限定符
"""
import re

content = r'fsababf243536#$7sg ><||  fgfeg\n  ___sfSF好人哦呵呵DSGEHetgfeg'


# . 表示匹配除了\n 之外的任意字符


def print_re(re_str):
    print(re.findall(re_str, content))


if __name__ == '__main__':
    # ceshi  '.'
    # print_re('.')
    # []匹配一位数字
    # print_re('[0-9]')
    # 匹配小写的字母
    # print_re('[a-z]')
    # 配大写
    # print_re('[A-Z]')
    # 匹配汉字
    # print_re('[\u4e00-\u9fa5]')
    # 匹配大小写的字母 数字
    # print_re('[0-9a-zA-Z]')
    # 匹配 重复 1到多次
    # print_re('[0-9]+')
    # 匹配0到多次
    # print_re('[0-9]*')
    # 匹配0次或1词
    # print_re('[0-9]?')
    print_re('[^a-z]')
