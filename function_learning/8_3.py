# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/3/14 14:20'


# 让函数返回多个结果

# 函数的返回：
# 1. return value
# 2. 不return value或者return None，python都默认是return None
# 3. 只有return这样的关键字：函数代码碰到return之后，return后面的语句是不会执行的
# 函数遇到return之后，函数的运行就终止了

def print_word(word):
    print(word)
    return
    print("Nana, let it be!")


print_word('heynana')


# heynana

# 其他语言，说明返回结果的类型
# python没有这样的限制，可以返回任意类型的变量
# python，甚至函数可以返回一个函数

def damage(skill1, skill2):
    damage1 = skill1*2
    damage2 = skill2*3 + 10
    return damage1, damage2

damages = damage(3, 9)
print(damages)
# (6, 37)
print(type(damages))
# <class 'tuple'>
# python默认会把函数返回的多个结果组成一个元组

# 如何使用返回的多个结果呢？
print(damages[0], damages[1])
# 6 37
# 这种依靠序号来访问特定变量结果的方法是不可取的

# 建议的方式：
skill1_damage, skill2_damage = damage(2, 3)
print(skill1_damage, skill2_damage)
# 用不同变量来接收函数的不同返回结果， 这样变量的意义就非常明确
# 4 19

# 序列解包
# 维护的时候更加方便， 使代码变得易于维护
