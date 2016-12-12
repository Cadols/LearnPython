#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# strip
username = input('plz input:')
if username.strip() == 'will':
    print('Welcome')
"""

"""
# split, join
name = 'Alice, Betty, Clare'
print(name)
name2 = name.split(',')
print(name2)
name3 = '|'.join(name2)
print(name3)
"""

"""
# capitalize
name = 'will wang'
# print('' in name) # 判断有没有空格
print(name.capitalize()) # 将字符串首字母改为大写
"""

"""
# format
msg = 'Hello {name}, we have met {time} years ago.'
msg2 = msg.format(name = 'Will', time = 3)
msg3 = 'Hello {0}, we have met {1} years ago.'
print(msg2)
print(msg3.format('Alice', 4))
"""

"""
# 切片, center
names = 'Alice Aya'
print(names[2:5])
print(names.center(30, '-'))
print(names.find('A'))
"""

"""
# int, isdigit
age = input('Plz input your age:')
if age.isdigit():
    print('Your age is:', age)
else:
    print('invalid data type')
"""


name = 'alice betty clare'
name2 = name.upper()
name3 = name2.lower()
print(name2)
print(name3)

