#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def add_sub(func):
    print("进行加减：", func)
    while True:
        if '++' in func or '+-' in func or '--' in func or '-+' in func:  # 替换运算符号
            func = func.replace('++', '+')
            func = func.replace('+-', '-')
            func = func.replace('--', '+')
            func = func.replace('-+', '-')
        else:
            break
    if not re.search(r'\-?\d+\.?\d*?[+-]\d+\.?\d*', func):  # 匹配带小数点数字的加减法
        return func
    contain = re.search(r'\-?\d+\.?\d*?[+-]\d+\.?\d*', func).group()
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
    print("新的加减func：", new_func)
    return add_sub(new_func)


def mul_div(func):
    print("进行乘除：", func)
    if not re.search(r'\d+\.?\d*[*/]+[+-]?\d+\.?\d*', func):  # 匹配带小数点数字的乘除法
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
        value = round(value, 12)
        # print("结果：", value)
    front, back = re.split(r'\d+\.?\d*[*/]+[+-]?\d+\.?\d*', func, 1)
    new_func = "%s%s%s" % (front, value, back)
    print("新的乘除func：", new_func)
    return mul_div(new_func)


def compute(arithmetic):
    arithmetic = mul_div(arithmetic)
    arithmetic = add_sub(arithmetic)
    return arithmetic


def strip_bracket(arithmetic):
    while True:
        if '++' in arithmetic or '+-' in arithmetic or '--' in arithmetic or '-+' in arithmetic:
            arithmetic = arithmetic.replace('++', '+')
            arithmetic = arithmetic.replace('+-', '-')
            arithmetic = arithmetic.replace('--', '+')
            arithmetic = arithmetic.replace('-+', '-')
        else:
            break
    if not re.search(r'\(([^()]+)\)', arithmetic):
        print("没有括号了！")
        # result = mul_div(arithmetic)
        # result = add_sub(arithmetic)
        result = compute(arithmetic)
        return result
    front, found, back = re.split(r'\(([^()]+)\)', arithmetic, 1)
    print("括号内算式：", found)
    # print(front,'\n', found, '\n', back)
    # found = mul_div(found)
    # found = add_sub(found)
    found = compute(found)
    arithmetic = "%s%s%s" % (front, found, back)  # 将括号内算式的结果拼接回去
    print("拼接后的算式：", arithmetic)
    return strip_bracket(arithmetic)

if __name__ == "__main__":
    calc = input("please input:")
    calc = re.sub(r'\s', '', calc)  # 除去空格
    print(calc)
    result = strip_bracket(calc)
    print("最终结果：", result)