#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

print(random.random())  # 随机打印小数
print(random.randint(1, 5))  # 随机打印范围内整数
print(random.randrange(1, 5))  # 随机打印范围内整数（不包含末尾数）
print(random.sample(range(100), 5))  # 随机从100个数字中选5个

# 生成随机验证码
import string
str_source = string.ascii_letters + string.digits
print(''.join(random.sample(str_source, 6)))

import random
checkcode = ''
for i in range(4):
    current = random.randrange(0,4)
    if current != i:
        temp = chr(random.randint(65,90))  # 取大写字母 A-Z 之一
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print(checkcode)