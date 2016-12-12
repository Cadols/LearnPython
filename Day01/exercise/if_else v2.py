#!/usr/bin/env python
# -*- coding: utf-8 -*-

#优化v1
user = "will"
passwd = "wang1234"
username = input("username:")
password = input("password:")

if user == username and passwd == password: # 用and同时判断username和password
    print("Welcome back, %s" %username)
else:
    print("Invalid username or password...")