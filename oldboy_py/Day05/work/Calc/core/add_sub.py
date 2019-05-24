#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def add_sub(func):
    # print("进行加减：", func)
    while True:
        if '++' in func or '+-' in func or '--' in func or '-+' in func:  # 替换运算符号
            func = func.replace('++', '+')
            func = func.replace('+-', '-')
            func = func.replace('--', '+')
            func = func.replace('-+', '-')
        else:
            break
    if not re.search(r'\-?\d+\.?\d*[+-]\d+\.?\d*', func):  # 匹配带小数点数字的加减法
        print("加减计算结果为：", func)
        return func
    contain = re.search(r'\-?\d+\.?\d*[+-]\d+\.?\d*', func).group()
    # print("算式：", contain)
    if len(contain.split('+')) > 1:
        res_contain = contain.split('+')
        value = float(res_contain[0]) + float(res_contain[-1])
    else:
        res_contain = contain.split('-')
        value = float(res_contain[0]) - float(res_contain[-1])
    front, back = re.split(r'\-?\d+\.?\d*[+-]\d+\.?\d*', func, 1)
    # print(front, '\n', back)
    new_func = "%s%s%s" % (front, value, back)
    # print("合并后的新算式：", new_func)
    return add_sub(new_func)