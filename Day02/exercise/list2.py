#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
练习方法copy, deepcopy, reverse, sort, pop, extend, index, count, 步长[::2], del
找出有多少个9，把它改成9999
同时找出有多少个34，把它删除
"""

"""
# copy, deepcopy
import copy
names = ['Will', 'Jack', 'Rose', [1, 2, 3, 4]]
names2 = names.copy()
names3 = copy.copy(names)
names4 = copy.deepcopy(names)

names[0] = 'WILL'
names2[3][1] = 'Yes'
names[3][2] = 'No'

print(names)
print(names2)
print(names3)
print(names4)
"""

"""
# reverse, sort
names = ['Alex', 'Betty', 'Clare', 'Dior', 'Ella', 'Fiona']
names.reverse()
print(names)

names.sort()
print(names)
"""

"""
# pop, extend
names = ['Alex', 'Betty', 'Clare', 'Dior', 'Ella', 'Fiona', 1]
names.pop()
print(names)

nums = [1, 2, 3, 4, 5]
names.extend(nums)
print(names)
"""

"""
# index, count, 步长, del
names = ['Will', 3, 5, 3, 6, 3, 5, 3, 8, 'Jack', 'Rose']
print(names.index(5)) # 只返回找到的第一个下标
print(names.count(3))
print(names[::2])
del names[5:8]
print(names)
"""

nums = [1, 9, 2, 34, 9, 3, 9, 34, 4, 9, 5, 34, 9, 6, 9, 34, 7, 9, 8, 34, 9, 0]
for i in range(nums.count(9)):
    nums[nums.index(9)] = 9999
print(nums)

for i2 in range(nums.count(34)):
    nums.remove(34)
print(nums)