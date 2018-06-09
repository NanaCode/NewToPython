# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/9 18:49'

# None Python表示空的特殊类型
# None不等于空字符串 空列表 0 False  类型和取值上都是不相等的
a = ''
b = []
c = 0
d = False
print(a == None)
print(b == None)
print(c == None)
print(d == None)
# False
# False
# False
# False
# 取值不等同

# print(isinstance(a, None))
# print(isinstance(b, None))
# print(isinstance(c, None))
# print(isinstance(d, None))
# Traceback (most recent call last):
#   File "C:/Users/Administrator/PycharmProjects/NewToPython/pythonic/14_6.py", line 21, in <module>
#     print(isinstance(a, None))
# TypeError: isinstance() arg 2 must be a type or tuple of types

print('*' * 8)
print(a is None)
print(b is None)
print(c is None)
print(d is None)
# False
# False
# False
# False
# 类型也不相同

# python里的空本身也是一个对象 也是一个类型
print(type(None))


# <class 'NoneType'>
# 体现python一切皆对象


# if not a 和 if a is None实际区别很大， 这两个表达式不是在任何时候结果都是相同的

def fun():
    return None


a = fun()
if not a:
    print('S')
else:
    print('F')

if a is None:
    print('S')
else:
    print('F')
    # S
    # S

b = []
if not b:
    print('S')
else:
    print('F')

if b is None:
    print('S')
else:
    print('F')
    # S
    # F
    # 此时if not a 和 if a is None进入不同条件分支

# 推荐判空操作:
# if a:
# if not a:

# a = None  a = '' a = [] a = False

# 本质意义理解None False
# None不存在的概念 False表示真假
# 有时if None和if False都会得到相同的结果，但是结果相同，不代表他们在本质和概念上是相同的
# 表示空的不同的数据类型，在if会得到同样结果，但是本质上类型是不同的
