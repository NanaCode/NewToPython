# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/1/27 21:44'

import json

json_str = '[{"name":"qiyue", "age":18, "flag":false}, {"name":"qiyue", "age":18}]'
student = json.loads(json_str)
print(type(json_str))
print(type(student))
print(student)
# print(student['name'])
# print(student['age'])
