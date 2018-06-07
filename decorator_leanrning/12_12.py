# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/6 22:29'

import time


def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)

    return wrapper


@decorator
def f1(func_name):
    print("This is a function name " + func_name)


@decorator
def f2(func_name1, func_name2):
    print("This is a function name " + func_name1)
    print("This is a function name " + func_name2)


# @decorator
def f3(func_name1, func_name2, **kw):
    print("This is a function name " + func_name1)
    print("This is a function name " + func_name2)
    print(kw)


# 不加装饰器的返回结果
# This is a function name d
# This is a function name e
# {'f': 1, 'g': 2, 'h': '123'}


f1('a')
f2('b', 'c')
f3('d', 'e', f=1, g=2, h='123')
# 1528326695.7518702
# Traceback (most recent call last):
# This is a function name a
#   File "C:/Users/Administrator/PycharmProjects/NewToPython/decorator_leanrning/12_12.py", line 34, in <module>
# 1528326695.7528667
#     f3('d', 'e', f=1, g=2, h='123')
# This is a function name b
# TypeError: wrapper() got an unexpected keyword argument 'f'
# This is a function name c
# *args不能兼容f3这种情况
