#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core import login
from core import transaction
from core import accounts
from core import admin
from core import logger
from conf import settings

user_data = {
    'user_id': None,
    'login_status': None,
    'account_data': None
}


def acc_type(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if user_data['account_data']['status'] == 1:
            user_operate(user_data)
        if user_data['account_data']['status'] == 0:
            admin.admin_operate(user_data)
        return res
    return wrapper


def account_info(user_data):
    info = """------- 账户 %s 信息详情 -------
信用卡号：%s
信用额度：%s 元
剩余额度：%s 元
    """ % (user_data['user_id'], user_data['user_id'], user_data['account_data']['credit'],
           user_data['account_data']['balance'])
    print(info)

def repayment(user_data):
    # 用于还款
    account_info(user_data)  # 显示当前账户的信息
    account_data = user_data['account_data']  # 获取当前账户的信息
    print("您还需归还的金额为 %s 元。" % float((account_data['credit']) - float(account_data['balance'])))
    while True:
        if account_data['credit'] == account_data['balance']:
            print("您的欠款已结清，无需还款！")
            break
        repay_amount = input("请输入您想要归还的金额，'b'键返回：")
        if repay_amount.isdigit() or type(eval(repay_amount)) == float:  # 如果输入的是整数或浮点数
            account_data, interest = transaction.transaction(account_data, 'repayment', repay_amount)
            if account_data:
                logger.logger('transaction', user_data['user_id'], "账户 %s 还款 %s 元"
                                                                        % (account_data['account'], repay_amount))
                print("归还操作完成，您当前的剩余额度为：%s 元。" % account_data['balance'])
                return
        else:
            print("%s 不是一个有效的数字，请您确认是否输入正确。" % repay_amount)


def withdraw(user_data):
    # 用于提现
    account_info(user_data)
    account_data = user_data['account_data']
    while True:
        withdraw_amount = input("请输入您要提取的现金额度，'b'键返回：").strip()
        if withdraw_amount.isdigit() or type(eval(withdraw_amount)) == float:
            account_data, interest = transaction.transaction(account_data, 'withdraw', withdraw_amount)
            if account_data:
                logger.logger('transaction', user_data['user_id'], "账户 %s 提取现金 %s 元，手续费 %s 元"
                                                                % (account_data['account'], withdraw_amount, interest))
                print("提现操作完成，您当前的剩余额度为：%s 元。本次提现收取手续费 %s 元。" % (account_data['balance'], interest))
                return
        else:
            print("%s 不是一个有效的数字，请您确认是否输入正确。" % withdraw_amount)


def transfer(user_data):
    # 转账
    account_info(user_data)
    account_data = user_data['account_data']
    while True:
        # 录入转账目标账户
        transfer_account = input("请输入您要转账的账户卡号：").strip()
        if transfer_account == account_data['account']:
            print(account_data['account'])
            print("请不要输入自己的账户！")
            return
        trans_acc_data = accounts.load_account(transfer_account)
        if trans_acc_data:
            break
        else:
            print("您要转账的账户 %s 不存在，请重新输入！" % transfer_account)
    print(trans_acc_data)
    while True:
        transfer_amount = input("请输入您要转账的金额：").strip()
        if transfer_amount.isdigit() or type(eval(transfer_amount)) == float:
            account_data, interest = transaction.transaction(account_data, 'transfer', transfer_amount)
            transaction.transaction(trans_acc_data, 'repayment', transfer_amount)
            if account_data:
                logger.logger('transaction', account_data['account'], "成功向账户 %s 转账 %s 元，手续费 %s 元"
                                                                % (account_data['account'], transfer_amount, interest))
                logger.logger('transaction', transfer_account, "账户 %s 向您转账 %s 元"
                                                                % (transfer_account, transfer_amount))
                print("转账操作完成，成功向 %s 转账 %s 元。您当前的剩余额度为：%s 元，本次转账收取手续费 %s 元。" %
                      (transfer_account, transfer_amount, account_data['balance'], interest))
        else:
            print("%s 不是一个有效的数字，请您确认是否输入正确。")


def pay_check(user_data):
    log_file = "%s//log/%s/%s" % (settings.BASE_DIR, user_data['user_id'], 'transactions.log')
    with open(log_file, 'r', encoding='utf-8') as f:
        for i in f:
            print(i.strip())


def payment(costs_amount):
    pay_acc_data = login.login(user_data)
    # print(pay_acc_data)
    pay_status = transaction.transaction(pay_acc_data, 'payment', costs_amount)
    # print(pay_status)
    if pay_acc_data and pay_status:
        logger.logger('transaction', pay_acc_data['account'], "账户 %s 购物消费 %s 元"
                      % (pay_acc_data['account'], costs_amount))
    return pay_acc_data, pay_status


def user_operate(user_data):
    menu = """------- Welcome %s ---------
1.  账户信息
2.  归还欠款
3.  提取现金
4.  向他人转账
5.  查看流水账单
6.  退出
    """ % user_data['user_id']
    menu_dic = {
        '1': account_info,
        '2': repayment,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': exit
    }
    while True:
        print(menu)
        user_option = input("请选择您要操作的功能：").strip()
        if user_option in menu_dic:
            menu_dic[user_option](user_data)
        else:
            print("请输入正确的操作号码：")


@acc_type
def run():
    while True:
        acc_data = login.login(user_data)
        if user_data['login_status']:
            user_data['account_data'] = acc_data
            # user_operate(user_data)
            return acc_data
