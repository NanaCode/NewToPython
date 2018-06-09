# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/9 10:01'

# 已经存在的列表创建新的列表 列表推导式
# 数学集合推导式有些相似

# 普通解决思路：
# 1. for循环；
# 2. map

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i * i for i in a]
print(b)
# [1, 4, 9, 16, 25, 36, 49, 64]
c = [i ** 2 for i in a]  # 同样代表平方
print(c)
# [1, 4, 9, 16, 25, 36, 49, 64]
d = [i ** 3 for i in a]
print(d)
# [1, 8, 27, 64, 125, 216, 343, 512]

# 列表推导式 pythonic的写法
# map 其他编程语言里的写法

# 某种情况推荐用列表推导式
b = [i ** 2 for i in a if i >= 5]
print(b)
# [25, 36, 49, 64]
# 有条件的筛选然后进行操作
# 如果是map，需要结合filter

# set
set_demo = {1, 2, 3, 4, 5, 6, 7, 8}
set_de = [i ** 2 for i in a if i >= 5]
print(set_de)
# [25, 36, 49, 64]  注意，结果是中括号
set_de2 = {i ** 2 for i in a if i >= 5}
print(set_de2)
# {64, 25, 36, 49}
# set也可以被推导
# dict 同
# tuple元组 同
