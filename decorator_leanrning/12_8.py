# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/6 21:12'

# 很多框架和类库使用了很多装饰器
# 装饰器并不是python独有的，更多的是一种设计模式
# C#-特性 JAVA-注解
# 装饰器使用场景 解决什么问题 优势

# 打印函数执行的时间
import time


def f1():
    # print(time.time())  # 1528291118.223766 unix时间戳
    print('This is a function!')


# f1()

def f2():
    print("This is another function!")


# unix时间戳 Unix timestamp
# Unix时间 Unix Time
# POSIX时间（POSIX time)，是一种时间表示方式
# 定义为从格林威治时间1970年01月01日00时00分00秒起至现在的总秒数

# 开闭原则：对修改是封闭的， 对扩展是开发的

# 尽量通过扩展函数或者扩展类来解决需求变更的问题

# 专门编写一个函数来打印时间
def print_current_time(func):
    print(time.time())
    func()


print_current_time(f1)
print_current_time(f2)
# 1528291839.8241549
# This is a function!
# 1528291839.8241549
# This is another function!
# 但是这种方法不够好，不够优雅
# 并没有体现函数本身的特性

