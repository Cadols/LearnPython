#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def timer(func):        # timer(test1)  func = test1
    def deco(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print("Func is running %s second.." % (stop_time - start_time))
        return res  # 返回被装饰函数的值
    return deco

@timer  # test1 = timer(test1)
def test1():
    time.sleep(3)
    print("in the test1")

@timer  # test2 = timer(test2)
def test2(name, age):
    time.sleep(3)
    print("in the test2", name, age)

test1()
test2("Alice", 18)