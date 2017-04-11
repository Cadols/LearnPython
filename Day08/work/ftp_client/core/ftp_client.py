#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import json
import socket
import hashlib
from core.tools import *
from conf.settings import *


class FtpClient(object):
    """FTP 客户端"""
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((server_ip, server_port))

    def interactive(self):
        """Ftp client 命令交互"""
        while True:
            # ftp_cmd = input("FTP %s> " % self.server_path).strip()
            ftp_cmd = input("ftp> ").strip()
            if ftp_cmd:
                # print(ftp_cmd)
                cmd_str = ftp_cmd.split(" ")[0]
                if hasattr(self, cmd_str):
                    func = getattr(self, cmd_str)
                    func(ftp_cmd)
                else:
                    self.help()

    def help(self, *args):
        """帮助信息"""
        help_msg = """Ftp可用命令格式如下：
ls
lls
cd
lcd
pwd
put filename
get filename
mkdir dirname
        """
        print(help_msg)

    def register(self):
        """与服务器交互注册信息"""
        new_username = input("\033[34m请输入要注册的新用户名：\033[0m").strip()
        msg_dic = {
            "action": "register",
            "username": new_username
        }
        self.client.send(json.dumps(msg_dic).encode('utf-8'))  # 发送信息判断用户是否已存在
        server_response = json.loads(self.client.recv(1024).decode())
        # print("response dict", server_response)
        if not server_response["account_status"]:
            new_password1 = input("\033[34m请输入新账号的密码：\033[0m").strip()
            new_password2 = input("\033[34m请再次输入新账号的密码：\033[0m").strip()
            if new_password1 == new_password2:
                msg_dic["password"] = new_password1
                self.client.send(json.dumps(msg_dic).encode('utf-8'))
                print("\033[33m用户 %s 已成功建立。\033[0m\n" % new_username)
            else:
                print("\033[1;31m两次密码输入不一致。\033[0m\n")
        else:
            print("\033[1;31m用户 %s 已经存在。\033[0m\n" % new_username)

    def login(self):
        """与服务器交互登录信息"""
        username = input("请输入您的用户名：").strip()
        msg_dic = {
            "action": "login",
            "username": username
        }
        self.client.send(json.dumps(msg_dic).encode('utf-8'))
        server_response = json.loads(self.client.recv(1024).decode())
        # print("response dict:", server_response)
        # 判断用户是否已经注册
        if server_response.get("exist"):
            password = input("请输入您的密码：").strip()
            msg_dic["password"] = password
            self.client.send(json.dumps(msg_dic).encode('utf-8'))
            server_response = json.loads(self.client.recv(1024).decode())
            # 根据用户验证结果，进行处理
            if server_response.get("login"):
                self.home_path = server_response["home_path"]
                self.server_path = self.home_path
                self.local_path = os.path.dirname(BASE_DIR)
                print("\033[33m用户 %s 登录成功\033[0m" % username)
                self.interactive()
            else:
                print("\033[1;31m用户名或密码错误\033[0m\n")
        else:
            print("\033[1;31m用户 %s 不存在\033[0m\n" % username)

    def put(self, *args):
        """与服务器交互 put 命令"""
        # print("put args:", args)
        put_cmd = re.split(" ", args[0])
        put_file = os.path.join(self.local_path, put_cmd[-1])
        if os.path.isfile(put_file):
            put_file_size = os.stat(put_file).st_size
            # print(put_file_size)
            msg_dic = {
                "action": "put",
                "filename": put_cmd[-1],
                "file_size": put_file_size
            }
            self.client.send(json.dumps(msg_dic).encode('utf-8'))
            server_response = json.loads(self.client.recv(1024).decode())
            # print(server_response)
            if not server_response.get("storage"):  # 用户磁盘容量足够时
                if server_response.get("file_status"):
                    print("\033[1;31m文件 %s 已经存在，即将进行覆盖处理\033[0m" % put_cmd[-1])  # 当已经有文件时提示
                f = open(put_file, 'rb')
                m = hashlib.md5()
                for line in f:
                    self.client.send(line)
                    m.update(line)
                    send_size = f.tell()  # 获取当前发送文件位置的大小
                    progress_bar(send_size, put_file_size)
                f.close()
                # print(m.hexdigest())
                msg_dic= {"file_md5": m.hexdigest()}
                # 将文件MD5值发给服务器，并根据服务器响应进行操作
                self.client.send(json.dumps(msg_dic).encode('utf-8'))
                md5_response = json.loads(self.client.recv(1024).decode())
                # print(md5_response)
                if md5_response["md5_correct"]:
                    print("\n\033[33m文件 %s 上传完毕\033[0m" % put_cmd[-1])
                else:
                    print("\n\033[1;31m文件 %s MD5值与服务器不符\033[0m" % put_cmd[-1])
            else:
                print(server_response["storage"])
        else:
            print("\033[1;31m请输入文件名称\033[0m")

    def get(self, *args):
        """与服务器交互 get 命令"""
        # print("get args:", args)
        get_cmd = re.split(" ", args[0])
        if len(get_cmd):
            msg_dic = {
                "action": "get",
                "filename": get_cmd[-1]
            }
            file_path = os.path.join(self.local_path, get_cmd[-1])
            self.client.send(json.dumps(msg_dic).encode('utf-8'))  # 向服务器发送 get 请求
            server_response = json.loads(self.client.recv(1024).decode())
            # 根据返回判断
            if server_response.get("file_status"):
                file_size = server_response["file_size"]
                f = open(file_path, 'wb')
                m = hashlib.md5()
                received_size = 0
                self.client.send("ready".encode('utf-8'))
                while received_size < file_size:
                    if file_size - received_size > 1024:
                        size = 1024
                    else:
                        size = file_size - received_size
                    data = self.client.recv(size)
                    received_size += len(data)
                    m.update(data)
                    f.write(data)
                    progress_bar(received_size, file_size)
                f.close()
                # 向服务器发送已接收的文件MD5值
                file_md5 = {"file_md5": m.hexdigest()}
                self.client.send(json.dumps(file_md5).encode('utf-8'))
                server_response = json.loads(self.client.recv(1024).decode())
                if server_response.get("md5_correct"):
                    print("\n\033[33m文件 %s 下载完毕\033[0m" % get_cmd[-1])
                else:
                    os.remove(file_path)
                    print(server_response["msg"])
            else:
                print(server_response["msg"])
        else:
            print("\033[1;31m请输入文件名称\033[0m")

    def mkdir(self, *args):
        """与服务器交互 mkdir 命令"""
        # print("mkdir args:", args)
        mkdir_cmd = re.split(" ", args[0])
        msg_dic = {
            "action": "mkdir",
            "mkdir": mkdir_cmd
        }
        self.client.send(json.dumps(msg_dic).encode('utf-8'))
        server_response = json.loads(self.client.recv(1024).decode())
        # print(server_response)
        if server_response.get("new dir"):
            print("\033[33m新文件夹 %s 已成功建立\033[0m" % mkdir_cmd[-1])
        else:
            print(server_response["msg"])

    def cd(self, *args):
        """与服务器交互 cd 命令"""
        # print("cd args:", args)
        cd_cmd = re.split(" ", args[0])
        # print(cd_cmd)
        msg_dic = {
            "action": "cd",
            "cd cmd": cd_cmd
        }
        # 向服务器发送信息处理字典
        self.client.send(json.dumps(msg_dic).encode('utf-8'))
        # 接收服务器发来的处理字典
        server_response = json.loads(self.client.recv(1024).decode())
        # print(server_response)
        if server_response.get("server path"):
            self.server_path = server_response["server path"]
        else:
            print(server_response["msg"])
        print("当前远程目录", self.server_path)

    def ls(self, *args):
        """与服务器交互 ls 命令"""
        # print("ls args:", args)
        msg_dic = {"action": "ls"}
        self.client.send(json.dumps(msg_dic).encode('utf-8'))
        server_response = self.client.recv(1024).decode()
        print(server_response)

    def pwd(self, *args):
        """与服务器交互 pwd 命令"""
        # print("pwd args:", args)
        msg_dic = {"action": "pwd"}
        self.client.send(json.dumps(msg_dic).encode('utf-8'))
        self.server_path = self.client.recv(1024).decode()
        print("当前远程目录", self.server_path)

    def lcd(self, *args):
        """客户端处理 lcd 命令"""
        # print("lcd args:", args)
        lcd_cmd = re.split(r" ", args[0])
        if lcd_cmd[-1] == "..":
            self.local_path = os.path.dirname(self.local_path)
        elif os.path.isdir(os.path.join(self.local_path, lcd_cmd[-1])):
            self.local_path = os.path.join(self.local_path, lcd_cmd[-1])
        elif os.path.isfile(os.path.join(self.local_path, lcd_cmd[-1])):
            print("\033[1;31mlocal: %s: 不是一个文件夹\033[0m" % lcd_cmd[-1])
        else:
            print("\033[1;31mlocal: %s: 没有这个文件或文件夹\033[0m" % lcd_cmd[-1])
        print("当前本地目录", self.local_path)

    def lls(self, *args):
        """客户端处理 lls 命令"""
        # print("lls args:", args)
        local_dir_list = color(self.local_path)
        print(local_dir_list)
