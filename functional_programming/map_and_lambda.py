# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/16 22:20'

a = 2

list_x = [1, 2, 3, 4, 5, 6]


def square(x):
    return a * x * x


list_y = []
for x in list_x:
    y = square(x)
    list_y.append(y)
print(list_y)

r = map(square, list_x)
print(r)
print(list(r))

with_lambda = map(lambda x: x * x, list_x)
print(with_lambda)
print(list(with_lambda))
# <map object at 0x000001ABC5D7B1D0>
# [1, 4, 9, 16, 25, 36]

# 代码变得更加简洁


# 两个或两个以上参数
list_x = [1, 2, 3, 4, 5, 6]
list_y = map(lambda x, y: x * x + y, list_x)
# print(list(list_y))
# Traceback (most recent call last):
#   File "C:/Users/Administrator/PycharmProjects/NewToPython/functional_programming/map_and_lambda.py", line 36, in <module>
#     print(list(list_y))
# TypeError: <lambda>() missing 1 required positional argument: 'y'

list_o = [1, 2, 3, 4, 5, 6]
list_p = [1, 2, 3, 4, 5, 6]
list_map = map(lambda x, y: x * x + y, list_o, list_p)
print(list_map)
print(list(list_map))
# <map object at 0x000001585AF70128>
# [2, 6, 12, 20, 30, 42]

# map里可以传入多个参数


list_o = [1, 2, 3, 4, 5, 6]
list_p = [1, 2, 3, 4]
list_map = map(lambda x, y: x * x + y, list_o, list_p)
print(list_map)
print(list(list_map))
# <map object at 0x0000026622270240>
# [2, 6, 12, 20]\
# 元素个数不相等，并不会报错
# 取决于交集

# map lambda 并不能提升代码运行效率，只能让代码更加简洁
