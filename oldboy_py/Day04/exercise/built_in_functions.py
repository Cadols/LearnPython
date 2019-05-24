#!/usr/bin/env python
# -*- coding: utf-8 -*-

print(abs(-10))  # 取绝对值

print(all([-1, 0, 2]), all([-1, 1, 2]))  # 一个可迭代对象中的所有元素均为True，则返回True。为空时返回False

print(any([-1, 0, 2]), any([]))  # 一个可迭代对象中的任一元素为True，则返回True。为空时返回False

print([ascii([1, 3, '要求能打印'])])  # 将一个对象变为可打印的字符串形式

print(bin(1), bin(2), bin(4), bin(8))  # 将一个整数转换为一个二进制字符串

print(bool(),bool(0),bool([]),bool(1),bool('ok'))  # 根据返回布尔值，True or False

a = bytes('abcde', encoding='utf-8')  # 字符串不可修改
b = bytearray('abcde', encoding='utf-8')  # 转为bytes数组后可以修改
print(a.capitalize(), a)
print(b[0])
b[0] = 100
print(b)

print(callable(print), callable([]))  # 后面可以加()的均为True，如函数，类

print(chr(97), chr(500))  # 返回数字所对应的Unicode字符
print(ord('b'), ord('哈'))  # 返回字符所对应的Unicode编码

res = filter(lambda n: n > 5, range(10))  # 按照条件过滤
for i in res:
    print(i)

res2 = map(lambda n:n*2, range(10))  # 与列表生成式[i*2 for i in range(10)]相同
for i in res2:
    print(i)

import functools
res3 = functools.reduce(lambda x, y: x+y, range(10))
print(res3)

a = {6: 2, 8: 0, 1: 4, -5: 6, 99: 11, 4: 22}
print(sorted(a.items()))  # 字典转为列表排序
print(sorted(a.items(), key=lambda x: x[1]))  # 字典转为列表，按value的值排序

a = [1, 2, 3, 4, 5, 6]
b = ['a', 'b', 'c', 'd']
for i in zip(a, b):
    print(i)