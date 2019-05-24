#!/usr/bin/env python
# -*- coding: utf-8 -*-

user = "will"
passwd = "wang1234"
username = input("username:")
password = input("password:")

if user == username:
    print("Username is correct...")
    if passwd == password:
        print("Welcome back, %s" %username)
    else:
        print("Password is not invaild...")
else:
    print("Guess it again, %s" %username)