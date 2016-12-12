#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1.循环
li = []
for i in range(1, 11):
    li.append(i * 2)
print(li)

# 2.列表生成式
li2 = [i * 2 for i in range(1, 11)]
print(li2)

# 3.for循环后面还可以加上if判断
li3 = [i * i for i in range(1, 11) if i % 2 == 0]   # 生成1-10的平方切且可以被2整除的列表
print(li3)