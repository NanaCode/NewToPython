# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/9 14:25'


# 组的概念 列表 元组 集合

# 可迭代对象 迭代器
# 凡是可以被for in循环遍历的数据结构都是可迭代对象， 如列表 元组 集合
# 可迭代对象 英文叫iterable ??? iterator

# 迭代器：
# 1. 迭代器是个对象 class ???

class A:
    pass


# 默认情况下，class不能被for in循环来遍历
# 想让class能被for in循环遍历，只要把class变成一个迭代器，
# 就可以被for in循环遍历了

# 什么情况下，需要遍历自定义的class
# class Book:
#     pass
#
#
# class BookCollection:
#     pass
# Book可能不需要被遍历，但是Bookcollection表示这样一组书的时候，
# 这个类需要被遍历


# 如果自己定义的类没有被实现为迭代器，是不能直接被for in循环来遍历的

# 2. 由于迭代器是可以被for in循环来遍历的，所以迭代器一定是一个可迭代对象
# 但是，可迭代对象并不一定是迭代器

# 如何把普通对象变成一个迭代器，让它可以被for in循环来遍历？
# 实现两个内置函数：__iter__  __next__
# 只要一个类，实现了这两个方法，这个类就是一个迭代器，同时可以被for in循环直接遍历

class Book:
    pass


# 普通对象变成迭代器
class BookCollection:
    def __init__(self):
        self.data = ['《往事》', '《智能》', '《回味哈》']
        self.cur = 0  # 记录当前返回数据的序号， 每调用一次next, cur加1

    def __iter__(self):
        return self  # 返回自己这个迭代器

    def __next__(self):
        if self.cur >= len(self.data):
            raise StopIteration()
        r = self.data[self.cur]
        self.cur += 1
        return r


books = BookCollection()
for book in books:
    print(book)
    # 《往事》
    # 《智能》
    # 《回味哈》
    # for in循环内部的实质在于会不断调用迭代器内部的__next__方法，不断返回数据，
    # 最后没有数据返回了，抛出异常，表示迭代已经结束了，数据已经全部返回了

# 迭代器还可以调用next方法一个一个的取出来
books_next = BookCollection()
print(next(books_next))
print(next(books_next))
print(next(books_next))
# 《往事》
# 《智能》
# 《回味哈》

# 列表和元组不能使用next

print('*' * 10)
# 迭代器的特性：
books_feature = BookCollection()
for book in books_feature:
    print(book)
for book in books_feature:
    print(book)
    # 遍历一次之后，再遍历，结果会一样吗？
    # 《往事》
    # 《智能》
    # 《回味哈》
    # 只会执行第一次，第二次不会执行打印出任何结果
    # 迭代器重要特性：一次性
    # 这和列表 元组 是有区别的
    # 列表元组无论打印多少次，都会打印相同结果

    # 多次遍历迭代器，需要多次实例化迭代器
    # 或者对象拷贝

# python对象拷贝或者复制非常简单
import copy

books_copy = copy.copy(books)
# 浅复制 浅拷贝

# 深拷贝 深复制
import copy

books_deep_copy = copy.deepcopy(books)


# 生成器
# print 0-10000

# n = [i for i in range(0, 10001)]
# print(n)
# print(type(n))  # <class 'list'>
# for i in n:
#     print(i)


# 非常消耗计算机资源 比如内存
# 列表的存储是需要消耗计算机内存的

# 迭代器是针对一个对象来说的
# 生成器是针对一个函数的

def gen(max):
    t = 0
    while t <= max:
        print(t)
        t += 1


# gen(10000)


# 这种方式没有直接存储相关的数据
# 解决性能问题，但是不能满足要求

def gen_num(max):
    n = 0
    while n <= max:
        n += 1
        return n


print(gen_num(10000))


# 1  只会返回1

def gen_demo(max):
    n = 0
    while n <= max:
        n += 1
        yield n


print(gen_demo(10000))
# <generator object gen_demo at 0x0000021C6B430F10> 生成器

# 生成器的使用：
g = gen_demo(200)
next_g = next(g)
print(next_g)
# 1
print(next_g)
# 1
for i in g:
    print(i)
# 为什么结果是201？

# 生成器的内部是它保存了一个算法

n = (i for i in range(0, 10001))
print(n)
# <generator object <genexpr> at 0x0000021A9ABE0FC0>
# 列表推导式的中括号变成圆括号 结果就从列表编程生成器了
