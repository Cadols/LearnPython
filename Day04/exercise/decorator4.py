#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 页面验证
import time
user, passwd = 'alice', '1234'
def auth(auth_type):
    print("auth func:", auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print("wrapper func args:", *args, **kwargs)
            if auth_type == 'local':
                username = input("Username:").strip()
                password = input("Password:").strip()
                if user == username and passwd == password:
                    print("Welcome back! %s" % username)
                    res = func(*args, **kwargs)
                    print("---------Complete authentication---------")
                    return res
                else:
                    exit("Invalid username or password.")
            elif auth_type == 'ldap':
                print("Are you kidding me?")
        return wrapper
    return outer_wrapper

def index():
    print("Welcome to index page.")

@auth(auth_type="local")
def home():
    print("Welcome to home page.")

@auth(auth_type='ldap')
def forum():
    print("Welcome to forum page.")

index()
home()
forum()