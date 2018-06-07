# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/6 22:28'

# 带参数的情况
import time


# def decorator(func):
#     def wrapper():
#         print(time.time())
#         func()
#
#     return wrapper  #  注意不是wrapper()
#
#
# @decorator
# def f1(func_name):
#     print("This is a function name" + func_name)
# #
# #
# f1('test func')
# Traceback (most recent call last):
#   File "C:/Users/Administrator/PycharmProjects/NewToPython/decorator_leanrning/12_11.py", line 22, in <module>
#     f1('test func')
# TypeError: wrapper() takes 0 positional arguments but 1 was given

# def decorator(func):
#     def wrapper(func_name):
#         print(time.time())
#         func(func_name)
#
#     return wrapper
#
#
# @decorator
# def f1(func_name):
#     print("This is a function name " + func_name)
#
#
# f1('test func')

# 1528325842.0947573
# This is a function name test func

# 两个参数 多个参数的情况

# 装饰器具有通用性

# 可变参数解决参数个数不一样的问题
# args 很多编程语言里用来代表一组参数 没有具体意义 通用叫法

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

f1('a')
f2('b', 'c')
# 1528326362.0807755
# This is a function name a
# 1528326362.0807755
# This is a function name b
# This is a function name c

# 可变参数，可以传入任意数量的参数

