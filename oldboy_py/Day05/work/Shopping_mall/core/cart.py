#!/usr/bin/env python
# -*- coding: utf-8 -*-


def info(cart_info, user_data):
    print("\n" + " %s 的购物车 ".center(50, '-') % user_data['user_name'])
    for key in cart_info:
        print("商品名：%s ，单价：%d 元，数量：%d ，共计：%d 元" %
              (cart_info[key]['goods'], cart_info[key]['price'],
               cart_info[key]['amount'], cart_info[key]['price']*cart_info[key]['amount']))
    print("")
