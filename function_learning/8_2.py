# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/3/14 13:56'


# 1. 参数列表可以没有
# 2. 函数一般返回值return value, 如果没有return value，python认为你返回的是None

# 1. 实现两个数字的相加；
# 2. 打印输入的参数

def add(x, y):
    result = x + y
    return result


def print_word(word):
    print(word)


# 参数取值是按照传入顺序

result = add(520, 530)
print(result)
print('I love python')

# 1050
# I love python

# 先定义再调用，不能先调用再定义

# def print(code):
#     print(code)
# print('hey')
#   File "C:/Users/Administrator/PycharmProjects/NewToPython/function_learning/8_2.py", line 35, in <module>
#     print('hey')
#   File "C:/Users/Administrator/PycharmProjects/NewToPython/function_learning/8_2.py", line 34, in print
#     print(code)
#   File "C:/Users/Administrator/PycharmProjects/NewToPython/function_learning/8_2.py", line 34, in print
#     print(code)
#   File "C:/Users/Administrator/PycharmProjects/NewToPython/function_learning/8_2.py", line 34, in print
#     print(code)
#   [Previous line repeated 995 more times]
# RecursionError: maximum recursion depth exceeded
# 自己调用自己，命名规范的问题
# Previous line repeated 995 more times python可以设置最大递归次数

# import sys
#
# sys.setrecursionlimit(1111)
#
#
# def print(code):
#     print(code)


# print('hey')
#   File "C:/Users/Administrator/PycharmProjects/NewToPython/function_learning/8_2.py", line 53, in print
#     print(code)
#   File "C:/Users/Administrator/PycharmProjects/NewToPython/function_learning/8_2.py", line 53, in print
#     print(code)
#   File "C:/Users/Administrator/PycharmProjects/NewToPython/function_learning/8_2.py", line 53, in print
#     print(code)
#   [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded
# 为什么这里变成996？？？

# 原因：定义了一个和python内置函数同名的函数
# 注意：自定义变量 函数，都要避免和python内置的变量和函数同名

a = add(1, 3)
b = print_word('oh no python')
print('--------')
print(a, b)
# oh no python
# --------
# 4 None
# print_word()内部是没有return的，所以它会把函数的结果设置成None


# print(a, b, c, d, e)
