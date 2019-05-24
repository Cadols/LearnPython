#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import getpass
from core import logger
from conf import settings


def acc_access(account, password):
    # 验证账户
    account_path = "%s/db/accounts/%s.json" % (settings.BASE_DIR, account)
    # print(account_path)
    if os.path.isfile(account_path):
        with open(account_path, 'r', encoding='utf-8') as f:
            account_data = json.load(f)
            # print(account_data)
            if account_data['password'] == password and account_data['status'] != 2:
                return account_data
            elif account_data['status'] == 2:
                print("您的账户 %s 已被冻结，请尽快联系管理员！" % account)
            else:
                print("您输入的账号或密码错误！")
    else:
        print("账户 %s 不存在！" % account)


def login(user_data):
    attemp_times = 0
    while user_data['login_status'] is not True and attemp_times < 3:
        account = input("请输入您的信用卡号：").strip()
        password = getpass.getpass("请输入您的密码：").strip()
        access = acc_access(account, password)
        if access:
            logger.logger('operation', account, "账户 %s 成功登录" % account)
            user_data['login_status'] = True
            user_data['user_id'] = account
            return access
        attemp_times += 1
    else:
        logger.logger('operation', account, "账户 %s 多次登录失败被强制退出" % account)
        exit("账户 %s 多次尝试登录失败，将强制退出！" % account)
