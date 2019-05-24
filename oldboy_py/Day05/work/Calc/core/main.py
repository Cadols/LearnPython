#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from core import compute

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
        print("算式内没有括号了！\n")
        # result = mul_div(arithmetic)
        # result = add_sub(arithmetic)
        result = compute.compute(arithmetic)
        return result
    front, found, back = re.split(r'\(([^()]+)\)', arithmetic, 1)
    print("\n找到括号内算式：", found)
    # print(front,'\n', found, '\n', back)
    # found = mul_div(found)
    # found = add_sub(found)
    found = compute.compute(found)
    arithmetic = "%s%s%s" % (front, found, back)  # 将括号内算式的结果拼接回去
    print("拼接后的算式：", arithmetic)
    return strip_bracket(arithmetic)

def run():
    calc = input("请输入想要进行计算的算式：").strip()
    calc = re.sub(r'\s', '', calc)  # 除去空格
    print("即将对算式 %s 进行计算！" % calc)
    result = strip_bracket(calc)
    print("最终计算结果为：", result)