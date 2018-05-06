def func():
    def func(x):

        return 'a' in x

    # 自己实现的方式

    def filter1(fun, seq):

        li = []

        for item in seq:

            if fun(item):

                li.append(item)

        return li

        li = filter1(fun, li)

        print(li)
li = ('abc', 'java', 'PHP', 'Python')
f = filter(func, li)

#使用lambda表达式实现

f = filter(lambda x: 'a' in x, li)

print(list(f))
