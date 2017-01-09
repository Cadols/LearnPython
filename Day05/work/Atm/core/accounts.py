#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from conf import settings
from db import sample


def load_account(account_id):
    # 读取账户信息
    file_path = "%s/db/accounts/%s.json" % (settings.BASE_DIR, account_id)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            account_data = json.load(f)
            return account_data
    else:
        return


def dump_account(account_data):
    # 写入账户信息
    file_path = "%s/db/accounts/%s.json" % (settings.BASE_DIR, account_data['account'])
    with open(file_path, 'w', encoding='utf-8') as f:
        account_data = json.dump(account_data, f)
        return account_data


def new_account(acc_name):
    # 添加账户
    account_path = "%s/db/accounts/%s.json" % (settings.BASE_DIR, acc_name)
    if os.path.exists(account_path):
        print("账户 %s 已经存在，请不要重复建立！" % acc_name)
    else:
        new_acc_data = sample.sample_dic
        # print(new_acc_data)
        while True:
            # 新账户两次密码验证
            acc_passwd = input("请输入新账户 %s 的密码：" % acc_name).strip()
            acc_passwd2 = input("请再次输入新账户 %s 的密码：" % acc_name).strip()
            if acc_passwd == acc_passwd2:
                break
            else:
                print("两次密码不一致，请重新输入！")
        while True:
            acc_status = input("请确认账户 %s 的权限类型（ 0 = 管理员，1 = 普通用户 ）：" % acc_name).strip()
            if acc_status.isdigit():
                acc_status = int(acc_status)
                if acc_status == 0 or acc_status == 1:
                    break
                else:
                    print("请正确选择账户类型！")
            else:
                print("请正确选择账户类型！")
        new_acc_data['account'], new_acc_data['password'], new_acc_data['status'] = acc_name, acc_passwd, acc_status
        dump_account(new_acc_data)
        print("新账户 %s 已经添加完毕！" % acc_name)
        return new_acc_data
