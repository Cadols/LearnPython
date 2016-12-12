#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def timer(func):
    def deco():
        start_time = time.time()
        func()
        end_time = time.time()
        print("I am running in %s" % (end_time - start_time))
    return deco

@timer
def test1():
    time.sleep(3)
    print("I am test1")

test1()