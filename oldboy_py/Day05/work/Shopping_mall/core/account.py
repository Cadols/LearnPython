#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import getpass
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def acc_access(username, password):
    account_path = "%s/db/accounts/%s.json" % (BASE_DIR, username)
    if os.path.isfile(account_path):
        with open(account_path, 'r') as f:
            user_data = json.load(f)
            # print(user_data)
            if user_data['password'] == password and user_data['status'] != 2:
                return user_data
            elif user_data['status'] == 2:
                print("您的账户 %s 已经被锁定，请联系管理员！" % username)
            else:
                print("账户名或密码错误！")
    else:
        print("账户 %s 不存在！" % username)


def acc_ban(username):
    # 锁定账户
    account_path = "%s/db/accounts/%s.json" % (BASE_DIR, username)
    if os.path.isfile(account_path):
        with open(account_path, 'r') as f:
            user_data = json.load(f)
            user_data['status'] = 2
        with open(account_path, 'w') as f:
            json.dump(user_data, f)
        return username
    else:
        print("账户 %s 不存在！" % username)


def login(user_data):
    attemp_times = 0
    while user_data['login_status'] is not True and attemp_times < 3:
        username = input("请输入您的用户名：").strip()
        password = getpass.getpass("请输入您的密码：").strip()
        access = acc_access(username, password)
        if access:
            user_data['login_status'] = True
            user_data['user_name'] = username
            return user_data
        elif access is None:
            attemp_times += 1
        if attemp_times == 3:
            acc_ban(username)
            exit("账户 %s 多次尝试登录，即将被锁定！" % username)