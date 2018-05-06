li = []
dict = {}
count = 0
while count < 2:
    username = input('添加帐户:\n')
    password = input('添加帐户密码:\n')
    dict = {'name': username, 'word': password}
    li.append(dict)
    print(li)
    count += 1


def end(fun):
    def speed():
        print('还是自己去输密码吧,无能为力!')
        fun()
    return speed


@end
def inner():
    name1 = input('输入银行卡帐户:\n')
    word1 = input('请输入银行卡密码')
    if name1 == username and word1 == password:
       print('登陆成功')
    else:
        print('账号密码错误!!')
    return inner

inner()


@end
def add():
    name1 = input('输入银行卡帐户:\n')
    word1 = input('请输入银行卡密码')
    if name1 == username and word1 == password:
       print('登陆成功')
    else:
        print('账号密码错误!!')
    return add

add()


@end
def eat():
    name1 = input('输入银行卡帐户:\n')
    word1 = input('请输入银行卡密码')
    if name1 == username and word1 == password:
       print('登陆成功')
    else:
        print('账号密码错误!!')
    return eat

eat()