#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from conf.settings import *
from core.tools import hash
from core.logger import *


class Account(object):
    """账号处理"""
    def register(self, username, password):
        """注册用户"""
        user_db_path = os.path.join(DB_PATH, username + ".json")
        user_home_path = os.path.join(HOME_PATH, username)
        # print(user_db_path)
        open(user_db_path, 'w').close()
        user_info = {
            "username": username,
            "password": hash(password),
            "storage": STORAGE_SIZE
        }
        # print(user_info)
        try:
            os.makedirs(user_home_path)
        except FileExistsError as e:
            print("用户 %s 建立完毕，其文件夹已存在。" % username)
        finally:
            json.dump(user_info, open(user_db_path, 'w', encoding='utf-8'))
            logger("ftp_server", "REGISTER", "info", "新用户 %s 创建成功" % username)

    def login(self, username, password):
        user_db_path = os.path.join(DB_PATH, username + ".json")
        user_dic = json.load(open(user_db_path, 'r', encoding='utf-8'))
        # print("user dict:", user_dic)
        # 根据账号密码的验证情况，返回不同值
        if user_dic["password"] == hash(password):
            logger("ftp_server", "LOGIN", "info", "用户 %s 正常登录" % username)
            return user_dic
        else:
            logger("ftp_server", "LOGIN", "warning", "用户 %s 登录失败，用户密码错误" % username)
            return False
