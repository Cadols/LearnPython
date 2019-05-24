#!/usr/bin/env python
# -*- coding: utf-8 -*-


name = input("Please input your name:")
age = int(input("Please input your age:")) #convert str to int
job = input("Please input your job:")

msg = """
Information of user %s:
Name:   %s
Age :   %d
Job :   %s
"""%(name, name, age, job)
print(msg)
