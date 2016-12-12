#!/usr/bin/env python
# _*_ coding: utf-8 _*_

welcome_msg = 'Welcome to shopping mall'.center(50,'-')
print(welcome_msg)

salary_flag = False
while not salary_flag:
    salary = input('Please input your salary:')
    if salary.isdigit():
        salary = int(salary)
        salary_flag = True
    elif salary == 'q' or salary == 'quit':
        exit()
    else:
        print('Invalid date type...')

goods_info = [('iPhone', 5999), ('Macbook Air', 8999), ('Milk', 5), ('Bicycle', 700)]

purchased_goods = []

stop_flag = False
while not stop_flag:
    for goods in enumerate(goods_info): # 枚举字典goods_info，并将结果赋值给goods
        print(goods[0], goods[1][0].center(15, ' '), goods[1][1])
    user_choice = input('Please choice your good:')
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice < len(goods_info):
            choiced_good = goods_info[user_choice] # 将选择的商品赋值给choiced_good
            if choiced_good[1] <= salary: # 判断工资余额是否足够
                salary -= choiced_good[1]
                purchased_goods.append(choiced_good) # 将选择的商品记录到purchased_item
                print("You have choiced %s," % choiced_good[0], "cost: %d" % choiced_good[1])
                print("Your current banlance is %d" % salary)
            else:
                print("Your balance is not enough.")
        else:
            print('Please input correct number!')
    elif user_choice == 'c' or user_choice == 'check':
        for items in purchased_goods:
            print(items[0],items[1],salary)
    elif user_choice == 'q' or user_choice == 'quit':
        for items in purchased_goods:
            print(items,salary)
        stop_flag = True
    else:
        print("Invalid date type...")