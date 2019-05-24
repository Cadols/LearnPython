#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pickle
import re
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings


# while True:
#     line = input(">> ").strip()
#     res = re.search('cd ', line).group()
#     res2 = re.sub('cd ', '', line, count=1)
#     print(res, res2)
#     print("before strip:", line)
#     line.strip('cd ')
#     print("after strip:", line)


path = os.path.join(os.getcwd(), 'home')
print('path = ', path)

user_info = pickle.load(open(settings.ACCOUNT_DB_PATH, 'rb'))
print(user_info)
print(user_info['will'].password)

# 更改ftp目录路径操作
print("当前目录为：", os.getcwd())
while True:
    cmd = input(">> ").strip()
    try:
        if cmd == 'ls':
            # os.listdir()
            print(os.listdir())  # 当前目录下所有文件和文件夹
        if cmd == 'pwd':
            print(os.getcwd())  # 当前目录
        if re.match('cd ', cmd):
            res = re.sub('cd ', '', cmd)
            print(res)
            if res == '~':
                os.chdir(data['will'].home_path)  # 回到当前用户家目录
            # if res == '..':
            #     # os.chdir(os.pardir)  # 返回上一级目录
            #     os.chdir(res)  # 返回上一级目录
            # elif re.match(r'[A-Za-z]:[/\\]', res):
            #     print('abspath: ', re.match(r'[A-Za-z]:[/\\]', res).group())
            elif os.path.exists(os.getcwd() + '/' + res):
                print("/")
                res = os.getcwd() + '/' + res
            # else:
            #     print("\033[1;31m文件夹 %s 不存在。\033[0m" % res)
            os.chdir(res)  # 更改当前目录
            print("当前目录为：", os.getcwd())
    except NotADirectoryError as e:
        print("\033[1;31m%s 不是一个文件夹。\033[0m" % e)
    except FileNotFoundError as e:
        print("\033[1;31m系统没有找到路径 %s\033[0m" % res)
