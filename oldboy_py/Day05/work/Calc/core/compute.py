#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core import add_sub
from core import mul_div

def compute(arithmetic):
    arithmetic = mul_div.mul_div(arithmetic)
    arithmetic = add_sub.add_sub(arithmetic)
    return arithmetic