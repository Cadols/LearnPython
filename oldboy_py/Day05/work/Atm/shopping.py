#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import getpass
import json
import logging
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
from core import main

user_data = {
    'user_name': None,
    'login_status': None,
}

goods_dic = {
    '图书类': [
        ('魔鬼经济学', 135), ('权力的游戏', 285), ('莎士比亚悲剧喜剧全集', 109)
    ],
    '3C类': [
        ('iPhone7 Plus', 5000), ('Macbook Pro', 20000), ('Dell XPS15', 12000)
    ],
    '家电类': [
        ('电视机', 5000), ('电冰箱', 7000), ('空调', 4000)
    ],
    '服装类': [
        ('羽绒服', 1200), ('牛仔裤', 500), ('毛呢大衣', 1800)
    ]
}

cart = {}


def logger(user_data, message):
    # 创建日志
    pur_list = logging.getLogger()
    pur_list.setLevel(logging.INFO)

    # 创建
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    log_path = "%s/%s_purchased.log" % (BASE_DIR, user_data['user_name'])
    fh = logging.FileHandler(log_path, encoding='utf-8')
    fh.setLevel(logging.INFO)

    # 日志格式
    log_format = logging.Formatter('%(asctime)s - %(message)s')

    ch.setFormatter(log_format)
    fh.setFormatter(log_format)

    pur_list.addHandler(ch)
    pur_list.addHandler(fh)
    pur_list.info(message)
    pur_list.removeHandler(ch)
    pur_list.removeHandler(fh)
    return pur_list


def acc_access(username, password):
    account_path = "%s/%s.json" % (BASE_DIR, username)
    if os.path.isfile(account_path):
        with open(account_path, 'r', encoding='utf-8') as f:
            user_data = json.load(f)
            # print(user_data)
            if user_data['password'] == password and user_data['status'] != 2:
                return user_data
            elif user_data['status'] == 2:
                print("您的账户 %s 已经被锁定，请联系管理员！" % username)
            else:
                print("账户名或密码错误！")
    else:
        print("账户 %s 不存在！" % username)


def acc_ban(username):
    # 锁定账户
    account_path = "%s/%s.json" % (BASE_DIR, username)
    if os.path.isfile(account_path):
        with open(account_path, 'r', encoding='utf-8') as f:
            user_data = json.load(f)
            user_data['status'] = 2
        with open(account_path, 'w', encoding='utf-8') as f:
            json.dump(user_data, f)
        return username
    else:
        print("账户 %s 不存在！" % username)


def login(user_data):
    attemp_times = 0
    while user_data['login_status'] is not True and attemp_times < 3:
        username = input("请输入您的用户名：").strip()
        password = getpass.getpass("请输入您的密码：").strip()
        access = acc_access(username, password)
        if access:
            user_data['login_status'] = True
            user_data['user_name'] = username
            return user_data
        elif access is None:
            attemp_times += 1
        if attemp_times == 3:
            acc_ban(username)
            exit("账户 %s 多次尝试登录，即将被锁定！" % username)


def info(cart_info, user_data):
    print("\n" + " %s 的购物车 ".center(50, '-') % user_data['user_name'])
    for key in cart_info:
        print("商品名：%s ，单价：%d 元，数量：%d ，共计：%d 元" %
              (cart_info[key]['goods'], cart_info[key]['price'],
               cart_info[key]['amount'], cart_info[key]['price']*cart_info[key]['amount']))
    print("")


def pay(user_data, cart):
    total = 0
    for key in cart:
        # print(key)
        total += cart[key]['price'] * cart[key]['amount']
    if cart:
        res, pay_status = main.payment(total)
        # print(res, pay_status)
        if res and pay_status:
            logger(user_data, "购物消费 %d 元！" % total)
        else:
            print("")
    else:
        print("您的购物车还是空的呢！")


def mall(user_data, goods_dic, cart):
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
    layer = [goods_dic]
    while not exit_flag:
        print("“没什么东西可买商城” 商品目录 -（'c'：查看购物车，'l'：查看已购清单，'p':付款，'b'：返回，'q'：退出）")
        for menu in enumerate(goods_dic):
            if len(menu[1]) == 2:
                print(menu[0], menu[1][0], menu[1][1])
            else:
                print(menu[0], menu[1])
        choice = input("\n请选择您想浏览的商品目录编号：").strip()
        if choice.isdigit():  # 放入购物车
            choice = int(choice)
            if choice > len(goods_dic) - 1:
                print("请输入正确的商品目录编号！\n")
                continue
            if type(goods_dic) is list:
                goods_name = goods_dic[choice][0]
                goods_amount = input("请输入你要购买的数量：").strip()
                if goods_amount.isdigit():
                    goods_amount = int(goods_amount)
                    if goods_name in cart:
                        new_goods_amount = goods_amount + cart.get(goods_name).get('amount')
                    else:
                        new_goods_amount = goods_amount
                    cart_goods = {'goods': goods_name, 'price': goods_dic[choice][1], 'amount': new_goods_amount}
                    cart[goods_name] = cart_goods
                    print("商品 %s 已放入购物车，数量 %d" % (goods_name, goods_amount))
                    continue
                else:
                    print("请输入正确的数字！")
                    continue
            if choice < len(goods_dic):
                layer.append(goods_dic)
                goods_dic = goods_dic[list(goods_dic)[choice]]
            else:
                print("请输入正确的商品目录编号！")
        elif choice == 'c':
            info(cart, user_data)
        elif choice == 'l':
            log_file = "%s/%s_purchased.log" % (BASE_DIR, user_data['user_name'])
            if os.path.isfile(log_file):
                print("%s 的已购清单" % user_data['user_name'])
                with open(log_file, 'r', encoding='utf-8') as f:
                    for i in f:
                        print(i.strip())
            else:
                print("您尚未购买过商品！")
        elif choice == 'p':
            pay(user_data, cart)
            cart = {}
        elif choice == 'b':
            goods_dic = layer[-1]
            layer.pop()
        elif choice == 'q':
            exit(" %s 欢迎您的再次光临，！" % user_data['user_name'])
        else:
            print("请输入正确的数字编号！")


if __name__ == '__main__':
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
        login(user_data)
        if user_data['login_status']:
            mall(user_data, goods_dic, cart)