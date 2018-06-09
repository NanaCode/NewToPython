# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/9 10:24'

# 字典 列表推导式
students = {
    'Anna': 15,
    'Peter': 16,
    'Henry': 17
}

# b = [key for key, value in students]
# Traceback (most recent call last):
#   File "C:/Users/Administrator/PycharmProjects/NewToPython/pythonic/14_4.py", line 12, in <module>
#     b = [key for key, value in students]
#   File "C:/Users/Administrator/PycharmProjects/NewToPython/pythonic/14_4.py", line 12, in <listcomp>
#     b = [key for key, value in students]
# ValueError: too many values to unpack (expected 2)

b = [key for key, value in students.items()]
print(b)
# ['Anna', 'Peter', 'Henry']

# key value颠倒
c = {value: key for key, value in students.items()}  # 注意，这里要用花括号
print(c)
# {15: 'Anna', 16: 'Peter', 17: 'Henry'}

d = (key for key, value in students.items())
print(d)
# <generator object <genexpr> at 0x000002C1A9600D58>
# 不是元组 而是可遍历对象generator
for x in b:
    print(x)
    # Anna
    # Peter
    # Henry

    # 为什么元组会出现这样一种情况？得到一个generator对象。
    # 因为元组是不可变的，所以元组在很多行为上和列表这样典型的
    # 可变序列是有区别的

    # 推荐这里使用列表而不是元组，因为有时操作generator对象可能会出错误。
