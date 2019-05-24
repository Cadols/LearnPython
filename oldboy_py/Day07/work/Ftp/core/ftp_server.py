#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import socket
import json
from conf.settings import *


class FtpServer(object):
    """Ftp 服务器端"""
    def __init__(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(5)

    def run(self):
        """启动接口"""
        self.interactive()

    def interactive(self):
        """Ftp server命令处理"""
        while True:
            print("Ftp服务已启动，正在等待通信: ")
            self.conn, self.addr = self.server.accept()  # 等通信过来
            print(self.conn, self.addr)
            while True:
                try:
                    data = self.conn.recv(1024)
                    # print(data)
                    # data = data.decode()
                    if not data:
                        print("客户端连接已断开")
                        break
                    elif data.decode() in ['ls', 'pwd']:
                        self.reflection(data.decode(), data.decode())
                    elif re.match(r'(cd |pwd |put |get |home |mkdir)', data.decode()):
                        res = re.split(r' ', data.decode())
                        self.reflection(res[0], res[1])
                except ConnectionResetError as e:
                    print("客户端连接已断开2")
                    break
                except ConnectionAbortedError as e:
                    print("ConnectionAbortedError", e)

    def reflection(self, *args):
        """通过反射调用方法"""
        # print("server reflect = ", args)
        if hasattr(self, args[0]):
            func = getattr(self, args[0])
            func(args[1])

    def put(self, *args):
        """接收 put 命令并接收客户端文件"""
        # print("put_args = ", args)
        put_file_path = os.path.join(self.pwd_path, args[0])
        # print(put_file_path)
        if os.path.isfile(put_file_path):
            server_f = open(put_file_path + "_new", 'wb')
        else:
            server_f = open(put_file_path, 'wb')
        client_dic = json.loads(self.conn.recv(1024).decode())
        received_file_size = 0
        self.conn.send("ok".encode('utf-8'))
        while received_file_size < client_dic["file size"]:
            put_file = self.conn.recv(1024)
            received_file_size += len(put_file)
            server_f.write(put_file)
        server_f.close()
        msg = "\033[33m文件 %s 服务器接受完毕。\033[0m" % args[0]
        self.conn.send(msg.encode('utf-8'))

    def get(self, *args):
        """接收 get 命令并向客户端发送文件"""
        # print("get_args = ", args)
        file_path = os.path.join(self.pwd_path, args[0])
        # print(file_path)
        msg_dic = {}
        if os.path.isfile(file_path):  #
            msg_dic["file size"] = os.stat(file_path).st_size
            msg_dic["file name"] = args[0]
            msg_dic["file status"] = 1
            # print(msg_dic)
            self.conn.send(json.dumps(msg_dic).encode('utf-8'))
            client_ready_status = self.conn.recv(1024)
            # print("Are you OK?", client_ready_status.decode())
            if client_ready_status.decode() == "ok":
                with open(file_path, 'rb') as server_f:
                    for line in server_f:
                        self.conn.send(line)
                    print("文件 %s 发送完毕。" % args[0])
        else:
            msg_dic["file status"] = "\033[1;31m服务器上没有找到文件 %s\033[0m" % args[0]
            self.conn.send(json.dumps(msg_dic).encode('utf-8'))

    def delete(self, *args):
        pass

    def cd(self, *args):
        """更改当前远程目录"""  # 需修改，远程服务器只能用cd ..
        # print("cd_args = ", args)
        try:
            if args[0] == '~':
                self.pwd_path = self.home_path  # 回到当前用户家目录
                msg = "当前远程目录 %s" % self.pwd_path
                self.conn.send(msg.encode('utf-8'))
            elif args[0] == '..':
                if os.path.dirname(self.pwd_path) == USER_HOME_PATH:
                    self.conn.send("\033[1;31m没有权限离开家目录。\033[0m".encode('utf-8'))
                else:
                    self.pwd_path = os.path.dirname(self.pwd_path)
                    msg = "当前远程目录 %s" % self.pwd_path
                    self.conn.send(msg.encode('utf-8'))
            # 检测是否是文件夹
            elif os.path.isdir(os.path.join(self.pwd_path, args[0]))\
                    and os.path.join(self.pwd_path, args[0]).startswith(USER_HOME_PATH):
                self.pwd_path = os.path.join(self.pwd_path, args[0])
                # print(self.pwd_path)
                msg = "当前远程目录 %s" % self.pwd_path
                self.conn.send(msg.encode('utf-8'))
            elif os.path.isfile(os.path.join(self.pwd_path, args[0])):
                msg = "\033[1;31m%s 不是一个文件夹。\033[0m" % args[0]
                self.conn.send(msg.encode('utf-8'))
            else:
                msg = "\033[1;31m找不到目录：%s\033[0m" % args[0]
                self.conn.send(msg.encode('utf-8'))
        except FileNotFoundError as e:
            msg = "\033[1;31m系统没有找到路径 %s\033[0m" % args[0]
            self.conn.send(msg.encode('utf-8'))

    def ls(self, *args):
        """查看当前远程目录下所有文件和文件夹"""
        # print("ls_args = ", args)
        dir_list = os.listdir(self.pwd_path)
        if dir_list:
            # print(dir_list)
            msg = "当前远程目录 %s 下有：\n%s" % (self.pwd_path, ", ".join(dir_list))
            self.conn.send(msg.encode('utf-8'))
        else:
            msg = "\033[1;31m当前远程文件夹 %s 下没有文件或文件夹。\033[0m" % self.pwd_path
            self.conn.send(msg.encode('utf-8'))

    def pwd(self, *args):
        """查看当前远程目录"""
        # print("pwd_args = ", args)
        msg = "当前远程目录 %s" % self.pwd_path
        self.conn.send(msg.encode('utf-8'))

    def mkdir(self, *args):
        # print("mkdir_args = ", args)
        new_dir = os.path.join(self.pwd_path, args[0])
        if os.path.exists(new_dir):
            msg = "\033[1;31m文件夹 %s 已存在。\033[0m" % args[0]
        else:
            os.makedirs(new_dir)
            msg = "\033[33m文件夹 %s 已建立完毕。\033[0m" % args[0]
        self.conn.send(msg.encode('utf-8'))

    def home(self, *args):
        # print("home_args = ", args)
        if re.match(r'[A-Za-z]:[/\\]', args[0]):
            self.home_path = args[0]
            self.pwd_path = args[0]
            # print(self.home_path)
            # print(self.pwd_path)
