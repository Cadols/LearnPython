#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRANS_TYPE = {
    'repayment': {'action': 'plus', 'interest': 0},
    'withdraw': {'action': 'minus', 'interest': 0.05},
    'transfer': {'action': 'minus', 'interest': 0.05},
    'payment': {'action': 'minus', 'interest': 0},
}

LOG_TYPES = {
    'transaction': 'transactions.log',
    'operation': 'operation.log'
}