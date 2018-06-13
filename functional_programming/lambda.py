# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/10 11:51'


# 闭包不是函数式编程的全部
# 函数式编程是一种思维，而闭包只是其中的一种体现

# 匿名函数

def f():
    pass


# lambda  parameter_list: expression

def add(x, y):
    return x + y


result = lambda x, y: x + y
print(result(1, 2))

# 匿名函数的调用

# 匿名函数的定义非常简洁

# 其他语言叫lambda表达式  关键点在表达式上

# f = lambda x, y: a = x + y
#   File "C:/Users/Administrator/PycharmProjects/NewToPython/functional_programming/lambda.py", line 30
#     f = lambda x, y: a = x + y
#        ^
# SyntaxError: can't assign to lambda
# 不能在lambda里面做赋值操作
# 冒号后面是表达式 a = x + y 这个不是表达式，这是完整的代码语句

# C#里匿名函数是匿名函数 lambda表达式是lambda表达式

# 注意，冒号后面不能是代码块


