# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/3/14 15:25'


# 必须参数与关键字参数
# 1. 必须参数
def add(x, y):
    result = 2*x + 3*y
    return result

# 函数调用的时候，必须传递的参数

# add(x, y)， x, y是形式参数，简称形参  函数定义过程中
# add(1, 2)   1， 2是实际参数，实参，实参是函数调用过程中


# 2. 关键字参数
# 关键字参数可以让程序员不用考虑函数参数传递的顺序，
# 可以任意指定函数参数的顺序，从而实现函数的调用

c = add(y=8, x=9)
print(c)
# 42
# 明确告诉python，实参是给哪个形参的

# 关键字参数没有改变函数的行为，也没有给函数添加强大的功能。
# 它的意义在于代码的可读性， 大大提高阅读代码的理解能力

# 必须参数和关键字参数的区别在于函数的调用上，而不是函数的定义上

