#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conf.settings import *
from core.fabric_host import *


def create_dir(func):
    """检测文件夹存在状态"""
    def deco():
        if not os.path.exists(DB_DIR_PATH):
            os.mkdir(DB_DIR_PATH)
        if not os.path.exists(LOG_DIR_PATH):
            os.mkdir(LOG_DIR_PATH)
        if not os.path.exists(FILE_DIR_PATH):
            os.mkdir(FILE_DIR_PATH)
        if not os.path.exists(DOWNLOAD_PATH):
            os.mkdir(DOWNLOAD_PATH)
        func()
    return deco


def quit():
    exit("感谢您的使用，再见")

@create_dir
def run():
    """启动程序"""
    fabric_host = FabricHost()
    menu = """欢迎来到类 Fabric 主机管理程序
1. 新增远程主机
2. 删除远程主机
3. 激活远程主机
4. 操作远程主机
5. 退出程序
"""
    menu_dic = {
        "1": fabric_host.create_host,
        "2": fabric_host.delete_host,
        "3": fabric_host.active_host,
        "4": fabric_host.remote_host,
        "5": quit
    }

    while True:
        # try:
            print(menu)
            user_choice = input("\033[34m请输入您要操作的选项序号：\033[0m").strip()
            # print(user_choice)
            # print(menu_dic[user_choice])
            menu_dic[user_choice]()
        # except TypeError as e:
        #     print("TypeError: ", e)
        # except Exception as e:
        #     print("\033[1;31m请输入正确的选项序号\033[0m\n", e)
