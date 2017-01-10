#!/usr/bin/env python
# -*- coding: utf-8 -*-

import python_commons


def run():
    inp = input("请输入您想访问页面的url：  ").strip()
    # modules, func = inp.split("/")
    # obj = __import__(modules)
    # if hasattr(obj, func):
        # func = getattr(obj, func)
    if hasattr(python_commons, inp):
        func = getattr(python_commons, inp)
        func()
    else:
        print("404")

if __name__ == '__main__':
    run()
