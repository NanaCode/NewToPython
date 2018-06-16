# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/15 22:50'

# 函数式编程 闭包的概念
# 不建议在业务代码里大量的使用闭包
# 写框架或者类库，可以尝试使用闭包

# map 这个类  注意不是函数，而是class类
# class map(func, *iterables)

# 适用场景

# 简化版的抛物线
a = 2

list_x = [1, 2, 3, 4, 5, 6]


def square(x):
    return a * x * x

list_y = []
for x in list_x:
    y = square(x)
    list_y.append(y)
print(list_y)
# [2, 8, 18, 32, 50, 72]

r = map(square, list_x)
print(r)
# <map object at 0x00000296E217B320>
print(list(r))
# [2, 8, 18, 32, 50, 72]

# map 数学层面映射
# 映射的结果是通过函数来决定的


