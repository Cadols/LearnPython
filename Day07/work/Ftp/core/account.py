#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle
import hashlib
from conf.settings import *
from core.ftp_client import *


class User(object):
    """用户类"""
    def __init__(self, user_name, user_passwd):
        self.name = user_name
        self.password = user_passwd
        self.home_path = os.path.join(USER_HOME_PATH, self.name)
        if not os.path.exists(self.home_path):
            os.makedirs(self.home_path)  # 创建用户家目录

    def run(self):
        FtpClient(HOST, PORT, self.home_path).run()


class Account(object):
    """账户工具"""
    def __init__(self):
        if os.path.exists(ACCOUNT_DB_PATH) and os.stat(ACCOUNT_DB_PATH).st_size != 0:  # 文件存在且不为空时
            self.user_db = pickle.load(open(ACCOUNT_DB_PATH, 'rb'))
        elif not os.path.exists(ACCOUNT_DB_PATH):  # 如果没有用户数据文件，创建空文件
            os.mkdir(DB_PATH)
            open(ACCOUNT_DB_PATH, 'w').close()
            self.user_db = {}
        else:
            self.user_db = {}

    def register(self):
        """注册新用户"""
        print("\n" + "这是个注册界面".center(30, "-"))
        # print(self.user_db)
        new_name = input("\033[34m请输入您的注册用户名：\033[0m").strip()
        if new_name in self.user_db:
            print("\033[1;31m用户 %s 已经注册。\033[0m" % new_name)
            self.register()
        while True:
            new_passwd1 = input("\033[34m请输入您的密码：\033[0m").strip()
            new_passwd2 = input("\033[34m请再次输入您的密码：\033[0m").strip()
            if new_passwd1 == new_passwd2:
                hash_pw = self.hash_it(new_passwd1)
                new_user_obj = User(new_name, hash_pw)
                self.user_db[new_name] = new_user_obj
                pickle.dump(self.user_db, open(ACCOUNT_DB_PATH, 'wb'))
                # add logger here
                print("\033[33m账户 %s 创建成功。\033[0m" % new_name)
                break
            else:
                print("\033[1;31m您两次输入的密码不一致，请重新输入。\033[0m")

    def login(self):
        """登录账户，调用ftp client"""
        print("\n" + "这是个登录界面".center(30, "-"))
        user_name = input("\033[34m请输入您的用户名：\033[0m").strip()
        if user_name in self.user_db:
            user_passwd = input("\033[34m请输入您的密码：\033[0m").strip()
            hash_user_pw = self.hash_it(user_passwd)
            if hash_user_pw == self.user_db[user_name].password:
                self.user_db[user_name].run()
            else:
                print("\033[1;31m用户名或密码错误。\033[0m")
        else:
            print("\033[1;31m用户 %s 不存在。\033[0m" % user_name)

    def hash_it(self, data):
        hash = hashlib.md5()
        hash.update(data.encode('utf-8'))
        return hash.hexdigest()
