# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/6 21:33'
import time


def decorator(func):
    def wrapper():  # 真正的业务逻辑
        print(time.time())
        func()
    return wrapper


def f1():
    print('This is a function!')

f = decorator(f1)
f()
# 1528293370.0752788
# This is a function!

# 这就是装饰器，其实和12_8里的调用方案没有太大区别
# 只是这种写法内聚性更高



