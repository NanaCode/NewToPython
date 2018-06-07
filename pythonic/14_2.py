# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/7 22:55'

# 字典映射代替switch case语句

day = 2


def get_sunday():
    return 'Sunday'


def get_monday():
    return 'Monday'


def get_tuesday():
    return 'Tuesday'


def get_default():
    return 'Unknown'


switcher = {
    0: get_sunday(),
    1: get_monday(),
    2: get_tuesday(),
}

day_name = switcher.get(day, get_default())
print(day_name)