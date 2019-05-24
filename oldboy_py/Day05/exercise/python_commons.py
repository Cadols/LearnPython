#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 首先，有一个commons模块，它里面有几个函数，分别用于展示不同的页面，代码如下：


def login():
    print("这是一个登陆页面！")


def logout():
    print("这是一个退出页面！")


def home():
    print("这是网站主页面！")


def run():
    inp = input("请输入您想访问页面的url：  ").strip()
    if inp == "login":
        login()
    elif inp == "logout":
        logout()
    elif inp == "home":
        home()
    else:
        print("404")


if __name__ == '__main__':
    run()
