# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/9 21:59'


class Test():
    pass

    # def __bool__(self):
    #     return False
    #
    # def __len__(self):
    #     return 0

    # def __len__(self):
    #     return 8

    # def __len__(self):
    #     return '8'

    # def __len__(self):
    #     return 1.0

    # def __len__(self):
    #     return True

    def __len__(self):
        return False


print('----------------')
print(bool(Test()))


# True 没有定义这两个方法，默认是True
# False  # __bool__的情况
# False  # __len__的情况  如果返回8之类的，则为True,
# 返回'8'会报错:TypeError: 'str' object cannot be interpreted as an integer
# 返回1.0浮点型也会报错：TypeError: 'float' object cannot be interpreted as an integer
# 例外，__len__可以返回布尔值，return True--True, return False--False

# bool()调用bool布尔这个对象时，实质是调用内部__len__这个内部函数
# 还有一个方法触发调用内部__len__这个内部函数：len()判断对象长度

class TestDemo():
    # def __len__(self):
    #     return True

    def __len__(self):
        return False


print(len(TestDemo()))


# 1  return True
# 0  return False

# 調用len()的实质是调用__len__()

class TestLen():
    pass


# print(len(TestLen()))
# TypeError: object of type 'TestLen' has no len()

print('---------')


class TestBoolOrLen():
    def __nonzero__(self):
        pass  # python2里决定对象取值的方法 python3里被__bool__方法给替代了

    def __bool__(self):
        return False
        # return 0  # 只能返回bool, TypeError: __bool__ should return bool, returned int

    def __len__(self):
        return True


print(bool(TestBoolOrLen()))
# False 取决于bool方法
# 两个方法都有时，bool()只运行__bool__()方法，不运行__len__()方法
# 没有__bool__()方法, bool()运行__len__()方法

