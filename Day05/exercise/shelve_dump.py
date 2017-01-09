#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shelve

d = shelve.open('shelve_test')  # 打开一个文件

def stu_date(name, age):
    print("Register stu", name, age)
name = ["alex", "rain", "test"]
info = {"name": "alex", "age":22}

d['func'] = stu_date
d['test'] = name
d['info'] = info