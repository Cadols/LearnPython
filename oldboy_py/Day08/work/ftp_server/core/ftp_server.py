#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import json
import hashlib
import socketserver
from conf.settings import *
from core.tools import *
from core.accounts import *
from core.logger import *


class MyTCPHandler(socketserver.BaseRequestHandler):
    """FTP 服务器"""
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                # print("connected client:", self.client_address)
                if not self.data:
                    logger("ftp_server", "Connection", "warning", "客户端断开连接")
                    break
                cmd_dic = json.loads(self.data.decode())
                # print("recv data:", cmd_dic)
                if hasattr(self, cmd_dic["action"]):
                    func = getattr(self, cmd_dic["action"])
                    func(cmd_dic)
                else:
                    print("\033[1;31mDoes not have this function.\033[0m")
            except ConnectionResetError as e:
                logger("ftp_server", "ConnectionResetError", "warning", e)
                break

    def register(self, *args):
        # print("register args:", args)
        cmd_dic = args[0]
        user_file_path = os.path.join(DB_PATH, cmd_dic["username"] + ".json")
        # 根据用户文件的有无来返回状态
        if os.path.isfile(user_file_path):
            cmd_dic["account_status"] = True
            self.request.send(json.dumps(cmd_dic).encode('utf-8'))
            logger("ftp_server", "REGISTER", "warning", "创建新用户 %s 失败，该用户已存在" % cmd_dic["username"])
        else:
            cmd_dic["account_status"] = False
            self.request.send(json.dumps(cmd_dic).encode('utf-8'))
            cmd_dic = json.loads(self.request.recv(1024).decode())
            # print("new cmd_dic:", cmd_dic)
            Account().register(cmd_dic["username"], cmd_dic["password"])

    def login(self, *args):
        # print("login args:", args)
        cmd_dic = args[0]
        user_file_path = os.path.join(DB_PATH, cmd_dic["username"] + ".json")
        user_home_path = os.path.join(HOME_PATH, cmd_dic["username"])
        if os.path.isfile(user_file_path):
            cmd_dic["exist"] = True
            # 向客户端发送用户存在状态
            self.request.send(json.dumps(cmd_dic).encode('utf-8'))
            cmd_dic = json.loads(self.request.recv(1024).decode())
            # 验证用户名密码
            user_dic = Account().login(cmd_dic["username"], cmd_dic["password"])
            if user_dic:
                self.username = cmd_dic["username"]
                self.home_path = user_home_path
                self.server_path = user_home_path
                self.home_size = user_dic.get("storage")
                cmd_dic["login"] = True
                cmd_dic["home_path"] = user_home_path
            # 向客户端发送用户登录状态
            self.request.send(json.dumps(cmd_dic).encode('utf-8'))
        else:
            cmd_dic["exist"] = None
            self.request.send(json.dumps(cmd_dic).encode('utf-8'))
            logger("ftp_server", "LOGIN", "warning", "用户 %s 登录失败，该用户不存在" % cmd_dic["username"])

    def put(self, *args):
        # print("put args:", args)
        put_dic = args[0]
        filenname = put_dic["filename"]
        file_size = put_dic["file_size"]
        file_path = os.path.join(self.server_path, filenname)
        dir_size = get_dir_size(self.home_path)
        if dir_size + file_size <= self.home_size:
            if os.path.isfile(file_path):
                msg_dic = {"file_status": True}
            else:
                msg_dic = {"file_status": False}
            self.request.send(json.dumps(msg_dic).encode('utf-8'))  # 发送文件是否存在信息
            f = open(file_path, 'wb')
            m = hashlib.md5()
            # 准备接收文件
            received_size = 0
            while received_size < file_size:
                # 根据文件剩余大小，定义此次接收的大小
                if file_size - received_size > 1024:
                    size = 1024
                else:
                    size = file_size - received_size
                data = self.request.recv(size)
                received_size += len(data)
                m.update(data)
                f.write(data)
            # print(m.hexdigest())
            f.close()
            md5_dic = json.loads(self.request.recv(1024).decode())
            if md5_dic["file_md5"] == m.hexdigest():  # MD5值相符
                msg_dic = {"md5_correct": True}
                logger(self.username, "PUT", "info", "MD5值验证正确，文件 %s 成功上传至 %s" % (filenname, self.server_path))
            else:  # MD5值不符
                os.remove(file_path)
                msg_dic = {"md5_correct": False}
                logger(self.username, "PUT", "warning", "MD5值验证错误，文件 %s 上传失败" % filenname)
            self.request.send(json.dumps(msg_dic).encode('utf-8'))
        else:
            msg_dic = {"storage": "\033[1;31m用户 %s 磁盘配额不足\033[0m" % self.username}
            self.request.send(json.dumps(msg_dic).encode('utf-8'))
            logger(self.username, "PUT", "warning", "文件 %s 上传失败，用户 %s 磁盘配额不足" % (filenname, self.username))

    def get(self, *args):
        # print("get args:", args)
        get_dic = args[0]
        filename = get_dic["filename"]
        file_path = os.path.join(self.server_path, filename)
        # 根据文件有无返回不同信息
        if os.path.isfile(file_path):
            file_size = os.stat(file_path).st_size
            msg_dic = {
                "file_status": True,
                "file_size": file_size
            }
            self.request.send(json.dumps(msg_dic).encode('utf-8'))
            client_status = self.request.recv(1024).decode()
            if client_status:
                f = open(file_path, 'rb')
                m = hashlib.md5()
                for line in f:
                    self.request.send(line)
                    m.update(line)
                f.close()
                md5_dic = json.loads(self.request.recv(1024).decode())
                if md5_dic["file_md5"] == m.hexdigest():
                    msg_dic = {"md5_correct": True}
                    logger(self.username, "GET", "info", "MD5值验证正确，用户 %s 下载文件 %s 成功" % (self.username, filename))
                else:
                    msg_dic = {"msg": "\n\033[1;31m文件 %s MD5值与服务器不符\033[0m" % filename}
                    logger(self.username, "GET", "warning", "MD5值验证错误，用户 %s 下载的文件 %s 有错误" % (self.username, filename))
                self.request.send(json.dumps(msg_dic).encode('utf-8'))
        else:  # 没有文件
            msg_dic = {"msg": "\033[1;31m没有找到文件 %s\033[0m" % filename}
            self.request.send(json.dumps(msg_dic).encode('utf-8'))
            logger(self.username, "GET", "info", "用户 %s 下载文件 %s 失败，该文件不存在" % (self.username, filename))

    def mkdir(self, *args):
        # print("mkdir args:", args)
        mkdir_cmd = args[0]["mkdir"]
        new_dir_path = os.path.join(self.server_path, mkdir_cmd[-1])
        if not os.path.isdir(new_dir_path) and len(mkdir_cmd) > 1:
            os.mkdir(new_dir_path)
            logger(self.username, "MKDIR", "info", "文件夹 %s 建立成功" % mkdir_cmd[-1])
            msg_dic = {"new dir": True}
        elif len(mkdir_cmd) == 1:
            msg_dic = {"msg": "\033[1;31m请输入您要建立的文件夹名称\033[0m"}
        else:
            msg_dic = {"msg": "\033[1;31m文件夹 %s 已存在\033[0m" % mkdir_cmd[-1]}
            logger(self.username, "MKDIR", "warning", "文件夹 %s 建立失败，文件夹已经存在" % mkdir_cmd[-1])
        self.request.send(json.dumps(msg_dic).encode('utf-8'))

    def cd(self, *args):
        # print("cd args:", args)
        cd_cmd = args[0]["cd cmd"]
        new_server_path = os.path.join(self.server_path, cd_cmd[-1])
        if cd_cmd[-1] == "~":
            print("now is ~")
            self.server_path = self.home_path
            msg_dic = {"server path": self.server_path}
        elif cd_cmd[-1] == "..":
            if not os.path.dirname(self.server_path).startswith(self.home_path):
                msg_dic = {"msg": "\033[1;31mserver: 没有离开家目录权限\033[0m"}
            else:
                self.server_path = os.path.dirname(self.server_path)
                msg_dic = {"server path": self.server_path}
        elif os.path.isdir(new_server_path):
            if not new_server_path.startswith(self.home_path):
                msg_dic = {"msg": "\033[1;31mserver: 没有离开家目录权限\033[0m"}
            else:
                self.server_path = new_server_path
                msg_dic = {"server path": self.server_path}
        elif os.path.isfile(new_server_path):
            msg_dic = {"msg": "\033[1;31mserver: %s: 不是一个文件夹\033[0m" % cd_cmd[-1]}
        else:
            msg_dic = {"msg": "\033[1;31mserver: %s: 没有这个文件或文件夹\033[0m" % cd_cmd[-1]}
        self.request.send(json.dumps(msg_dic).encode('utf-8'))

    def ls(self, *args):
        server_dir_list = color(self.server_path)
        print(server_dir_list)
        self.request.send(server_dir_list.encode('utf-8'))

    def pwd(self, *args):
        # print(self.server_path)
        self.request.send(self.server_path.encode('utf-8'))


