#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import time

def staff_info(func_type):
    def backup(func):
        def re_name(*args, **kwargs):
            if func_type != 'search_type':  # 判断是否备份
                backup_time = time.strftime('%Y%m%d_%H%M%S')
                shutil.copyfile('staff_info', 'staff_info_%s.bak' % backup_time)
                print("原员工信息已备份为 staff_info_%s.bak" % backup_time)
            print("已有员工：")
            with open('staff_info', 'r', encoding='utf-8') as f:  # 打印已有员工信息
                for line in f:
                    line = line.strip().split(',')
                    print('| ' + ' | '.join(line) + ' |')
            res = func(*args, **kwargs)
            if func_type in ['mod_type', 'del_type'] and os.path.exists('staff_info_new'):   # 重命名文件
                os.remove('staff_info')
                os.rename('staff_info_new', 'staff_info')
            return res
        return re_name
    return backup

@staff_info(func_type='search_type')
def search():
    user_search = input("请输入模糊查询语句:").strip()
    search_list = user_search.split(' ')  # 将条件语法以空格拆分为列表
    found_info = []  # 搜索结果
    with open('staff_info', 'r', encoding='utf-8') as f:
        for line in f:
            user_info = line.strip().split(',')  # 循环出员工信息
            conditional = '%s %s %s' % (user_info[2], search_list[6], search_list[7])  # 将条件字符串写入变量
            if search_list[6] == '=':  # 如果是等号就替换
                conditional = conditional.replace('=', '==')
            # 用语句关键字匹配，用 eval() 将字符串转换为判断条件
            if search_list[5] == 'age' and user_info[0].isdigit() and eval(conditional):
                found_info.append([user_info[1], user_info[2]])
            elif search_list[5] == 'dept' and user_info[4] in search_list[7]:
                found_info.append(user_info)
            # 匹配后，切片出用户信息列表中的年份与语法中的年份对比
            elif search_list[5] == 'enroll_date' and user_info[5][0:4] in search_list[7]:
                found_info.append(user_info)
        if not found_info:
            print("没有找到你要搜索的员工！\n")
        else:
            print("找到以下员工的信息：\n")
            for i in found_info:
                print(' | '.join(i))
            print("\n共计找到 %d 条信息\n" % len(found_info))
    return found_info

@staff_info(func_type='add_type')
def add():
    user_add = input("请输入您要增加的员工信息（注意格式）：").strip()
    add_list = user_add.split(',')  # 以 , 拆分为列表
    phone = []
    with open('staff_info', 'r+', encoding='utf-8') as f:
        user_id = 0  # 员工id变量
        for line in f:
            user_info = line.strip().split(',')  # 循环出员工信息
            phone.append(user_info[3])
            if user_info[0].isdigit() and user_id < int(user_info[0]):  # 判断是否要给员工id变量赋值
                user_id = int(user_info[0])
        if add_list[2] not in phone:
            f.write('\n' + str(user_id + 1) + ',' + ','.join(add_list))
            print("员工 %s 的信息已添加成功！\n" % add_list[0])
        else:
            print("您要添加的员工信息已存在！\n")

@staff_info(func_type='mod_type')
def modify():
    user_mod = input("请输入修改员工信息的语法：").strip()
    mod_list = user_mod.split(' ')
    user_list = []
    mod_flag = False
    with open('staff_info', 'r', encoding='utf-8') as f,\
                open('staff_info_new', 'w', encoding='utf-8') as f2:
        for line in f:
            user_info = line.strip().split(',')
            if user_info[4] in mod_list[10]:
                mod_flag = True
                user_info[4] = mod_list[5].strip('"')
                print("员工 %s 的信息已修改！\n" % user_info[1])
            user_list.append(user_info)
        for list in user_list:
            if not list[0].isdigit():   # 如果list[0]不为数字
                f2.write(','.join(list))
            else:
                f2.write('\n' + ','.join(list))
        if not mod_flag:
            print("没有找到需要修改信息的员工！\n")

@staff_info(func_type='del_type')
def delete():
    user_del = input("请输入您要删除的员工id：").strip()
    if not user_del.isdigit():
        print("请输入正确的员工编号！\n")
        return
    else:
        with open('staff_info', 'r', encoding='utf-8') as f,\
                open('staff_info_new', 'w', encoding='utf-8') as f2:
            for line in f:
                user_info = line.strip().split(',')
                if user_del == user_info[0]:
                    print("已删除员工 %s" % line)
                    continue
                else:  # 切片字符串首个字符，由其是否为数字决定写入格式。
                    if not line[0].isdigit():
                        f2.write(line.strip())
                    else:
                        f2.write('\n' + line.strip())

while True:
    print("""1.模糊查询
2.创建新员工
3.修改员工信息
4.删除员工信息
5.退出
""")
    menu_dict = {'1': search, '2': add, '3': modify, '4': delete}
    user_chosen = input("请输入您想要操作的选项序号:")
    if user_chosen in menu_dict.keys():
        menu_dict[user_chosen]()
    elif user_chosen == '5':
        exit("See you next time!")
    else:
        print("请输入正确的格式！")