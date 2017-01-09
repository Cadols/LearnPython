#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from conf import settings


def transaction(account_data, trans_type, amount):
    # 用于完成信用卡的资金处理
    amount = float(amount)
    if trans_type in settings.TRANS_TYPE:
        interest = amount * settings.TRANS_TYPE[trans_type]['interest']
        balance = account_data['balance']
        if settings.TRANS_TYPE[trans_type]['action'] == 'plus':
            new_balance = balance + amount + interest
            if new_balance > account_data['credit']:
                print("剩余额度将超过信用额度，请确认金额。")
                return
        elif settings.TRANS_TYPE[trans_type]['action'] == 'minus':
            new_balance = balance - amount - interest
            if new_balance < 0:
                print("您的剩余额度为 %s 元，无法完成本次交易所需费用 %s 元。" % (balance, (amount + interest)))
                return
        account_data['balance'] = new_balance
        account_path = "%s/db/accounts/%s.json" % (settings.BASE_DIR, account_data['account'])
        with open(account_path, 'w', encoding='utf-8') as f:
            json.dump(account_data, f)
        return (account_data, interest)
