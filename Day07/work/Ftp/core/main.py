#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conf.settings import *
from core.account import *


class Menu(object):
    """启动菜单"""
    def run(self):
        while True:
            try:
                menu = """\033[1;30m欢迎来到\033[1;34m 真的好简单 \033[1;30mFTP\033[0m
1. 注册新账户
2. 登录FTP账户
3. 退出
    """
                # menu_dic = {'1': self.register, '2': self.login_ftp, '3': self.quit_ftp}
                menu_dic = {'1': Account().register, '2': Account().login, '3': self.quit_ftp}
                print(menu)
                choice = input("\033[34m请输入您想要进行的操作序号：\033[0m").strip()
                menu_dic[choice]()
            except KeyError as e:
                print("\033[1;31m请输入正确的序号。\033[0m")

    def quit_ftp(self):
        """退出系统"""
        exit("\033[1;31m感谢您的使用，再见！\033[0m")

if __name__ == "__main__":
    Menu().run()
