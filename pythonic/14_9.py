# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/10 10:58'

# 装饰器副作用
import time


def decorator(func):
    def wrapper():
        print(time.time())
        func()

    return wrapper


@decorator
def fun1():
    print("This is a function!")


fun1()


# 1528601327.8642523
# This is a function!

def fun2():
    print(fun2.__name__)


fun2()


# fun2

@decorator
def fun3():
    print(fun3.__name__)


fun3()


# 1528601542.706881
# wrapper  # 函数名字变了
# 有时函数名字被改变，将会影响到我们的代码

def fun5():
    '''
    This is fun5
    :return:
    '''
    print(fun5.__name__)


print('*********')
print(help(fun5))
print('*********')
# Help on function fun5 in module __main__:
#
# fun5()
#     This is fun5
#     :return:
#
# None
fun5()


@decorator
def fun6():
    '''
    This is fun5
    :return:
    '''
    print(fun5.__name__)


print('*********')
print(help(fun6))
print('*********')
# Help on function wrapper in module __main__:
#
# wrapper()
#
# None
fun6()

# 解决方法：
from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper():
        print(time.time())
        func()

    return wrapper

@decorator
def fun7():
    '''
    This is a func
    :return:
    '''
    print(fun7.__name__)

print('--------')
print(help(fun7))
# Help on function fun7 in module __main__:
#
# fun7()
#     This is a func
#     :return:
#
# None
# 1528602208.80544
# fun7
fun7()
# 1528602187.042891
# fun7
help(fun7)
# Help on function fun7 in module __main__:
#
# fun7()
#     This is a func
#     :return:

# 为什么wraps函数能保持原有函数不变
# wraps函数可以把func一系列的信息复制到wrapper这个闭包函数上，就可以保持原有函数不变
