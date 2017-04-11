#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.ftp_client import *


class Menu(object):
    """启动菜单"""
    def run(self):
        client = FtpClient()
        menu = """欢迎来到 高级一点的 FTP
1. 注册新账户
2. 登录FTP
3. 退出
        """
        menu_dic = {
            "1": client.register,
            "2": client.login,
            "3": self.quit
        }
        while True:
            print(menu)
            try:
                choice_option = input("\033[34m请输入您想要进行的操作序号：\033[0m").strip()
                menu_dic[choice_option]()
            except KeyError as e:
                print("\033[1;31m请输入正确的序号。\033[0m")

    def quit(self):
        exit("\033[1;31m感谢您的使用，再见。\033[0m")
