#!/usr/bin/env python
# _*_ coding: utf-8 _*_

def calc(n):
    print(n)
    if int(n) > 0:
        return calc(int(n/2))

calc(10)