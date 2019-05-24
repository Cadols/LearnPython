#!/usr/bin/env python
# -*- coding: utf-8 -*-

li = []
# li[1]

# 单个异常处理
try:
    li[1]
except IndexError as e:
    print("Index error: ", e)

dic = {}
# dic['name']

# 多个异常处理
try:
    dic['name']
    li[1]
except KeyError as e:
    print("Do not have the key: ", e)
except IndexError as e:
    print("Index error: ", e)

try:
    dic['name']
    li[1]
except (KeyError, IndexError) as e:  # 这样写会分不清错误类型。除非出错类型的处理方式相同，不然不要这样写。
    print("There is an Error: ", e)

# 万能异常
s1 = 'hello'
try:
    int(s1)
# 先定义需要特殊处理或提醒的异常，最后定义 Exception 来确保程序正常运行。
except KeyError as e:
    print('键错误', e)
except IndexError as e:
    print('索引错误', e)
except Exception as e:
    print('未知错误', e)

# 异常的结构
num = 1
try:
    # 主代码块
    print(num)
except Exception as e:
    # 异常时，执行该块
    print('未知错误', e)
else:
    # 主代码块执行完，执行该块
    print("It's work.")
finally:
    # 无论异常与否，最终执行该块
    print("No matter it's error or not, I'll run it.")
