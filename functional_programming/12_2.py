# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/13 23:00'

# 三元表达式 在lambda用的比较多
# 表达式版本的if else语句
# if else条件控制语句 表达式这样简洁的概念来实现条件控制语句

# 根据x y的大小，最终决定返回的结果 x大于y取x, x小于y取y

# 其他语言，三元表达式的编写：
# x > y ? x:y  ?是如果 意义：问号前面是判断语句，如果x大于y，返回x, 否则返回y

# python 三元表达式
# 条件为真时返回的结果 if 条件判断 else 条件为假时的返回结果
# x if x > y else y   只是表达式，不是完整的代码

# 变量接收三元表达式的执行结果
# r = x if x > y else y

x = 1
y = 3
r = x if x > y else y
print(r)
# 3

# 三元表达式的本质在于表达式，所以适合用在lambda表达式上












