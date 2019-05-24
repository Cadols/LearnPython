#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core import accounts
from core import logger


def add_account():
    new_acc_name = input("请输入您要添加的账户名称：").strip()
    new_acc_data = accounts.new_account(new_acc_name)
    logger.logger('operation', new_acc_name, "账户 %s 创建" % new_acc_name)
    # print(new_acc_data)


def mod_account():
    while True:
        mod_acc = input("请输入您要修改额度的账户名：").strip()
        mod_acc_data = accounts.load_account(mod_acc)
        if mod_acc_data:
            print("账户 %s 当前的信用额度为：%s 元。" % (mod_acc, mod_acc_data['credit']))
            break
        else:
            print("账户 %s 不存在！" % mod_acc)
    while True:
        new_credit = input("请输入新的信用额度：").strip()
        if new_credit.isdigit():
            new_credit = int(new_credit)
            break
        else:
            print("请输入数字！")
    mod_acc_data['credit'] = new_credit
    accounts.dump_account(mod_acc_data)
    logger.logger('operation', mod_acc, "账户 %s 的信用额度已调整至 %s 元" % (mod_acc, mod_acc_data['credit']))
    print("账户 %s 的信用额度已修改成功，目前为 %s 元。" % (mod_acc, mod_acc_data['credit']))


def freeze_account():
    mod_acc = input("请输入您要冻结的账户名：").strip()
    mod_acc_data = accounts.load_account(mod_acc)
    if mod_acc_data:
        mod_acc_data['status'] = 2
        accounts.dump_account(mod_acc_data)
        logger.logger('operation', mod_acc, "账户 %s 被管理员冻结" % mod_acc)
        print("账户 %s 已成功冻结！" % mod_acc)
        return
    else:
        print("账户 %s 不存在！" % mod_acc)


def active_account():
    mod_acc = input("请输入您要解除冻结的账户名：").strip()
    mod_acc_data = accounts.load_account(mod_acc)
    if mod_acc_data:
        mod_acc_data['status'] = 1
        accounts.dump_account(mod_acc_data)
        logger.logger('operation', mod_acc, "账户 %s 被管理员解除冻结" % mod_acc)
        print("账户 %s 已成功解除冻结，现为普通用户！" % mod_acc)
        return
    else:
        print("账户 %s 不存在！" % mod_acc)


def admin_operate(user_data):
    menu = """------- Welcome Administrator %s ---------
1.  添加账户
2.  修改账户信用额度
3.  冻结账户
4.  解冻账户
5.  退出
        """ % user_data['user_id']
    menu_dic = {
        '1': add_account,
        '2': mod_account,
        '3': freeze_account,
        '4': active_account,
        '5': exit
    }
    while True:
        print(menu)
        admin_option = input("请选择您要操作的功能：").strip()
        if admin_option in menu_dic:
            menu_dic[admin_option]()
        else:
            print("请输入正确的功能号码：")
