#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author: Will

import os
import getpass
import time
import json

# 黑名单
if not os.path.exists('blacklist.txt'):
    with open('blacklist.txt', 'a+') as f:
        f.read()

# 账户登录
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
true_username = 'will'
true_password = '1234'
for i in range(3):
    with open('blacklist.txt', 'r') as f:
        blacklist = f.read().split()
    # print(blacklist)
    username = input("请输入您的用户名：")
    if username in blacklist:
        print("您的账户： %s 已经被锁定。请联系管理员解锁，或者更换登录账户。" % username)
        continue
    else:
        password = getpass.getpass("请输入您的密码：")
    if true_username == username and true_password == password:
        print("""
********************************************
**                                        **
**      这里是“没什么东西可买商城”      **
**                                        **
**           欢迎您的光临，%s           **
**                                        **
**                                        **
********************************************
        """ % username)
        break
    elif i == 2:
        with open('blacklist.txt', 'a+') as f:
            f.write('%s\n' % username)
        exit("您已尝试登录3次，您的账户 %s 已被锁定。" % username)
    else:
        print("用户名或密码错误，请重试。")

# 资金余额和已购清单文件读取
if os.path.exists('purchased_list.txt'):
    with open('purchased_list.txt', 'r') as f:
        purchased_list = json.load(f)
    with open('salary.txt', 'r') as f:
        salary = json.load(f)
    # salary = purchased_list.get('Salary')
    # print(purchased_list)
else:
    purchased_list = {}
    salary_flag = False
    while not salary_flag:
        salary = input("请输入您要充值的金额（'q'：退出）：")
        if salary.isdigit():
            salary = int(salary)
            salary_flag = True
        elif salary == 'q':
            exit()
        else:
            print("输入格式不正确，请输入数字。")
print("您现在的资金余额为：%d元\n" % salary)

# 商品字典
goods = {
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

# 根据当前目录是否有purchased_info文件来判断是读取文件信息还是赋空值
if os.path.exists('purchased_info.txt'):
    with open('purchased_info.txt', 'r') as f:
        purchased_info = json.load(f)
else:
    purchased_info = []

# 购物车
shopping_flag = False
while not shopping_flag:
    print("“没什么东西可买商城”商品目录：")
    for menu1 in enumerate(goods):
        print(menu1[0], menu1[1])
    catagory = input("\n请选择您想浏览的商品目录编号（'r'：查看购买记录，'c'：查看已购清单，'q'：退出）：")
    if catagory.isdigit():
        catagory = int(catagory)
        if catagory < len(goods):
            key = list(goods)[catagory]
        else:
            print("请输入正确的商品编号。")
        while catagory < len(goods):
            print("\n“没什么东西可买商城” %s商品列表：" % key)
            for menu2 in enumerate(goods[key]):
                print(menu2[0], menu2[1][0], menu2[1][1])
            user_choice = input("\n请输入您想购买的商品编号（'r'：查看购买记录，'c'：查看已购清单，'b'：返回，'q'：退出）:")
            if user_choice.isdigit():       # 如果用户选择输入的是数字
                user_choice = int(user_choice)
                if user_choice < len(goods[key]):
                    purchased_amount = input("请输入你要购买的数量：")
                    if purchased_amount.isdigit():
                        purchased_amount = int(purchased_amount)
                        purchased_item = goods[key][user_choice]        # 将选择的商品赋值给purchased_item
                        if purchased_item[1] * purchased_amount <= salary:      # 商品总价小于等于资金余额
                            salary -= purchased_item[1] * purchased_amount
                            purchased_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())   # 将购买时间记录下来赋值给purchased_time
                            purchased_record = [purchased_item[0], purchased_item[1], purchased_amount, purchased_time]     # 将商品名，商品价格，购买数量，购买时间以列表计入purchased_record
                            purchased_info.append(purchased_record)     # 将本条购买记录添加进purchased_info
                            # print(purchased_info)
                            with open('purchased_info.txt', 'w') as f:  # 将当前的购买记录写入文件purchased_info.txt
                                json.dump(purchased_info, f)
                            with open('salary.txt', 'w') as f:          # 将当前资金余额写入资金文件salary.txt
                                json.dump(salary, f)
                            # 根据已购清单中是否有商品信息判断
                            if purchased_item[0] in purchased_list:         # 如果已购清单中已有商品信息，最新已购数量 = 此次购买数 + 已购买数
                                purchased_amount_new = purchased_amount + purchased_list.get(purchased_item[0])
                            else:
                                purchased_amount_new = purchased_amount     # 如果已购清单中没有商品信息，最新已购数量 = 此次购买数
                            purchased_list[purchased_item[0]] = purchased_amount_new    # 修改已购清单字典purchased_list中对应商品的最新已购数量
                            with open('purchased_list.txt', 'w') as f:      # 将已购清单字典purchased_list写入已购清单文件purchased_list
                                json.dump(purchased_list, f)
                            # print(purchased_list)
                            print("\n您购买了 “%s” ，数量：%d，共计 %d元" % (purchased_item[0], purchased_amount,
                                                              purchased_item[1] * purchased_amount))
                            print("您现在的资金余额为：%d元\n" % salary)
                        else:
                            recharge = input("\n您的资金余额不足，请输入您要充值的金额（输入'n'退出）：")
                            if recharge.isdigit():
                                recharge = int(recharge)
                                salary += recharge          # 充值
                                print("您现在的资金余额为：%d元\n" % salary)
                            elif recharge == 'n':
                                exit("感谢您的光临，祝你本次购物愉快，再见。")
                            else:
                                print("请正确输入您想要充值的金额。\n")
                    else:
                        print("正确购买的数量应该为数字。\n")
                else:
                    print("请您输入正确的商品编号。\n")
            elif user_choice == 'b':
                break
            elif user_choice == 'r':
                for items in purchased_info:  # 循环购买记录列表
                    print("您在 %s 购买了 “%s” ，单价：%d元，数量：%d ，共计：%d元" % (
                        items[3], items[0], items[1], items[2], items[1] * items[2]))
                print("您现在的资金余额为：%d元\n" % salary)
            elif user_choice == 'c':
                for items in purchased_list:  # 循环已购清单字典
                    print("您目前已购买了 “%s” ，数量：%d" % (items, purchased_list[items]))
                print("您现在的资金余额为：%d元\n" % salary)
            elif user_choice == 'q':
                for items in purchased_list:  # 循环已购清单字典
                    print("您目前已购买了 “%s” ，数量：%d" % (items, purchased_list[items]))
                exit("您现在的资金余额为：%d元\n" % salary)
            else:
                print("您输入了非法字符，请输入数字。\n")
    elif catagory == 'r':
        for items in purchased_info:    # 循环购买记录列表
            print("您在 %s 购买了 “%s” ，单价：%d元，数量：%d ，共计：%d元" % (
                items[3], items[0], items[1], items[2], items[1] * items[2]))
        print("您现在的资金余额为：%d元\n" % salary)
    elif catagory == 'c':
        for items in purchased_list:    # 循环已购清单字典
            print("您目前已购买了 “%s” ，数量：%d" % (items, purchased_list[items]))
        print("您现在的资金余额为：%d元\n" % salary)
    elif catagory == 'q':
        for items in purchased_list:    # 循环已购清单字典
            print("您目前已购买了 “%s” ，数量：%d" % (items, purchased_list[items]))
        exit("您现在的资金余额为：%d元\n" % salary)
    else:
        print("您输入了非法字符，请您输入数字。\n")