#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def mul_div(func):
    # print("进行乘除：", func)
    if not re.search(r'\d+\.?\d*[*/]+[+-]?\d+\.?\d*', func):  # 匹配带小数点数字的乘除法
        print("乘除计算结果为：", func)
        return func
    contain = re.search(r'\d+\.?\d*[*/]+[+-]?\d+\.?\d*', func).group()
    # print("算式：", contain)
    if len(contain.split('*')) > 1:
        res_contain = contain.split('*')
        # print("算式：", res_contain)
        value = float(res_contain[0]) * float(res_contain[-1])
        # print("结果：", value)
    if len(contain.split('/')) > 1:
        res_contain = contain.split('/')
        # print("算式：", res_contain)
        value = float(res_contain[0]) / float(res_contain[-1])
        # print("结果：", value)
    front, back = re.split(r'\d+\.?\d*[*/]+[+-]?\d+\.?\d*', func, 1)
    new_func = "%s%s%s" % (front, value, back)
    # print("合并后的新算式：", new_func)
    return mul_div(new_func)