#!/usr/bin/env python
# -*- coding: utf-8 -*-

name = "Will Wang"
name2 = name  # name2指向name所指向的"Will Wang"
print(name, name2)

name = "Jack"  # 内存中开辟新地址保存为“Jack”
print(name, name2)
print("What is the value of name2 now?\n" + name2)