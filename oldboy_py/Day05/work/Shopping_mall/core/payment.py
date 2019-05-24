#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from core import logger

BASE_DIR = "%s/Atm" % os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
from core import main

def pay(user_data, cart):
    main.payment()
    total = 0
    for key in cart:
        # print(key)
        total += cart[key]['price'] * cart[key]['amount']
    logger.logger(user_data).info("购物消费 %d 元！" % total)
