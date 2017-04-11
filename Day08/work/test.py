#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

new_dic = {"test": True, "test2": False}

if new_dic["test"]:
    print(new_dic)
if not new_dic["test2"]:
    print(new_dic["test2"])

a = os.path.dirname(os.path.abspath(__file__))
print(a)
b = os.listdir(a)
print(b)
dir_list = ""
for i in b:
    if os.path.isfile(os.path.join(a, i)):
        dir_list += "\033[1;30m%s\033[0m " % i
    elif os.path.isdir(os.path.join(a, i)):
        dir_list += "\033[1;34m%s\033[0m " % i
print(dir_list)

cmd = "lcd     "
re_1 = re.match(r"lcd ", cmd).group()
re_2 = re.split(r" ", cmd)
print(re_1)
print(re_2)
print(bool(re_2[-1]))

dir_name = os.path.dirname(os.path.abspath(__file__))
os_walk = os.walk(dir_name)
print(dir_name)
print(os_walk)
