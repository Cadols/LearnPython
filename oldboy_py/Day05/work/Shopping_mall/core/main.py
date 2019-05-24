#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from core import account
from conf import goods
from core import cart
from core import payment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

user_data = {
    'user_name': None,
    'login_status': None,
}


def mall(user_data):
    print("""
********************************************
**                                        **
**      这里是“没什么东西可买商城”        **
**                                        **
**            欢迎您的光临，%s          **
**                                        **
**                                        **
********************************************
            """ % user_data['user_name'])
    exit_flag = False
    layer = [goods.dic]
    while not exit_flag:
        print("“没什么东西可买商城” 商品目录 -（'c'：查看购物车，'l'：查看已购清单，'p':付款，'b'：返回，'q'：退出）")
        for menu in enumerate(goods.dic):
            if len(menu[1]) == 2:
                print(menu[0], menu[1][0], menu[1][1])
            else:
                print(menu[0], menu[1])
        choice = input("\n请选择您想浏览的商品目录编号：").strip()
        if choice.isdigit():  # 放入购物车
            choice = int(choice)
            if choice > len(goods.dic) - 1:
                print("请输入正确的商品目录编号！\n")
                continue
            if type(goods.dic) is list:
                goods_name = goods.dic[choice][0]
                goods_amount = input("请输入你要购买的数量：").strip()
                if goods_amount.isdigit():
                    goods_amount = int(goods_amount)
                    if goods_name in goods.cart:
                        new_goods_amount = goods_amount + goods.cart.get(goods_name).get('amount')
                    else:
                        new_goods_amount = goods_amount
                    cart_goods = {'goods': goods_name, 'price': goods.dic[choice][1], 'amount': new_goods_amount}
                    goods.cart[goods_name] = cart_goods
                    print("商品 %s 已放入购物车，数量 %d" % (goods_name, goods_amount))
                    continue
                else:
                    print("请输入正确的数字！")
                    continue
            if choice < len(goods.dic):
                layer.append(goods.dic)
                goods.dic = goods.dic[list(goods.dic)[choice]]
            else:
                print("请输入正确的商品目录编号！")
        elif choice == 'c':
            cart.info(goods.cart, user_data)
        elif choice == 'l':
            print("%s 的已购清单" % user_data['user_name'])
            with open("%s/log/%s_purchased.log" % (BASE_DIR, user_data['user_name']), 'r', encoding='utf-8') as f:
                for i in f:
                    print(i.strip())
        elif choice == 'p':
            payment.pay(user_data, goods.cart)
            goods.cart = {}
        elif choice == 'b':
            goods.dic = layer[-1]
            layer.pop()
        elif choice == 'q':
            exit(" %s 欢迎您的再次光临，！" % user_data['user_name'])
        else:
            print("请输入正确的数字编号！")


def run():
    while True:
        print("""
********************************************
**                                        **
**                                        **
**          欢迎来到账户登录界面          **
**                                        **
**                                        **
**                                        **
********************************************
        """)
        account.login(user_data)
        if user_data['login_status']:
            mall(user_data)
