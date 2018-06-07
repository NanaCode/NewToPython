# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/3/14 15:12'

# 序列解包与链式赋值

# a = 1
# b = 2
# c = 3

# 简洁的写法
a, b, c = 1, 2, 3

# 也可以一个变量，接收三个数值
d = 1, 2, 3
print(d)
print(type(d))
# (1, 2, 3)
# <class 'tuple'>

# 序列解包就是反过来
e, f, g = d
print(e, f, g)
# 1 2 3

# 序列解包，元素的个数要相等
# h, i = d
# Traceback (most recent call last):
#   File "C:/Users/Administrator/PycharmProjects/NewToPython/function_learning/8_4.py", line 27, in <module>
#     h, i = d
# ValueError: too many values to unpack (expected 2)
# 期望是2， 却返回是3

# 小技巧
# j = 1
# k = 1
# l = 1
j = k = l = 1
print(j, k, l)
# 1 1 1
