#!/usr/bin/env python
# -*- coding: utf-8 -*-


def calc(n):
    return n**n
print(calc(10))

# 匿名函数
calc = lambda n:n**n if n > 5 else n*n
print(calc(6))

# 与其他函数配合使用
res = map(lambda x:x**2, [1, 5, 7, 4, 8])
for i in res:
    print(i)