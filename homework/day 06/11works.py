# 函数只有在调用的时候才会执行函数里的代码
# 函数也是一等对象


def fun():
    print('1111')


def fun1(fun):
    fun()
    print(2222)
"""
函数作为参数传递


"""
fun1(fun)

