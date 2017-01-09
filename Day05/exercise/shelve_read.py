#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shelve

def stu_date(name, age):
    print("?? stu", name, age)

f = shelve.open("shelve_test")

print(f['func']("test", 30))
print(f['test'])
print(f['info'])