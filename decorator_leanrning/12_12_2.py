# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/6 22:29'

import time


def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)

    return wrapper


@decorator
def f1(func_name):
    print("This is a function name " + func_name)


@decorator
def f2(func_name1, func_name2):
    print("This is a function name " + func_name1)
    print("This is a function name " + func_name2)


@decorator
def f3(func_name1, func_name2, **kw):
    print("This is a function name " + func_name1)
    print("This is a function name " + func_name2)
    print(kw)


f1('a')
f2('b', 'c')
f3('d', 'e', f=1, g=2, h='123')

# 1528326969.2526817
# This is a function name a
# 1528326969.2526817
# This is a function name b
# This is a function name c
# 1528326969.2526817
# This is a function name d
# This is a function name e
# {'f': 1, 'g': 2, 'h': '123'}

# 小技巧： 当你想要去调用一个函数，但是不知道函数是怎么定义的，可以使用如下形式：
# func(*args, **kw)

# 实际使用，建议明确传参

# 抽象参数 ，建议这样的调用方式
# func(*args, **kw)
