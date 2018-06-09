# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/9 21:31'

a = ''
b = []
c = 0
d = False
print(a == None)
print(b == None)
print(c == None)
print(d == None)


# if a:  if None的分支相同

# 当我们做if逻辑判断的时候，python里几乎每个对象都和布尔值True和False有着对应关系
# None永远对应的是False

# 自定义对象
class Test():
    pass


test = Test()
if test:
    print('S')

# S

print('x' * 8)


class AnotherTest():
    def __len__(self):
        return 0


test = Test()
if test:
    print('S')
else:
    print('F')
# S  和教程结果不一样？？？
print(bool(None))
print(bool([]))
print(bool(test))


# False
# False
# True 和教程结果不一样？？？

# 到底是True还是False，和自定义类中的两个方法有关系__bool__  __len__
class Test():
    # def __bool__(self):
    #     return False

    def __len__(self):
        return 0


print('----------------')
print(bool(Test()))
# False  # __bool__的情况
# False  # __len__的情况
