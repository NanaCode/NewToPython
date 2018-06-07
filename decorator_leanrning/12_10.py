# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/6 22:16'

#  python装饰器提供的语法糖 @符号 核心价值所在

# 可以接受定义时的复杂，只要调用的时候简单就行

import time


def decorator(func):
    def wrapper():  # 真正的业务逻辑
        print(time.time())
        func()

    return wrapper


@decorator  # 这样就构成了语法糖
def f1():
    print('This is a function!')


f1()  # 不改变原来的调用，装饰器最大的优势-没有改变原来调用的逻辑
# 12_8 12_9方式改变了原来的调用方式
# 1528294837.7080543
# This is a function!

# 只有@符号这个语法糖，才能真正体现装饰器的优势，才能保持代码不被破坏

# ES6对于javascript是个里程碑一样的标准 class关键字定义javascript的类 原先原型链

# C#里有大量语法糖

# 因为定义时的复制可能只会写一次，但是调用是到处都会用到的

# python装饰器其实是体现了AOP的思想 设计模式
