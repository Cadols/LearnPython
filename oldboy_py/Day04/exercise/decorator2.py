#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# 1.未定义bar函数，会报错
def foo():
    print("in the foo")
    bar()
foo()

# 2.调用时，函数已定义。
def bar():
    print("in the bar")
def foo():
    print('in the foo')
    bar()
foo()

# 3.
def foo():
    print("in the foo")
    bar()
def bar():
    print("in the bar")
foo()

# 4.
def foo():
    print("in the foo")
    bar()
foo()
def bar():
    print("in the bar")

# 高阶函数补充
import time
def bar():
    time.sleep(3)
    print("in the bar")

def test1(func):
    start_time = time.time()
    func()  # 就是bar()，但是改变了函数的调用方式
    stop_time = time.time()
    print("the func is running in %s second." % (stop_time - start_time))

test1(bar)      # 相当于func = bar

import time
def bar():
    time.sleep(3)
    print("in the bar")
def test2(func):
    print(func)
    return func

# print(test2(bar))
bar = test2(bar)     # 将bar的内存地址重新给回到bar
"""

# 嵌套函数
def foo():
    print("in the foo")
    def bar():
        print("in the bar")
    bar()
foo()