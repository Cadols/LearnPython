#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import json
import socket
from conf.settings import *


class FtpClient(object):
    """Ftp 客户端"""
    def __init__(self, host, port, home_path):
        self.lcd_path = BASE_DIR  # 本地目录地址
        # 启动客户端，并发送连接请求
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.client.send("home ".encode('utf-8') + home_path.encode('utf-8'))  # 传递用户家目录地址

    def run(self):
        """启动接口"""
        self.interactive()

    def interactive(self):
        """Ftp client 命令处理"""
        print("当前本地目录", self.lcd_path)
        while True:
            ftp_cmd = input("ftp> ").strip()
            if ftp_cmd in ['ls', 'lls', 'pwd']:
                self.reflection(ftp_cmd, ftp_cmd, ftp_cmd)
            elif re.match(r'(cd |lcd |get |put |mkdir)', ftp_cmd):
                res = re.split(r' ', ftp_cmd)
                # print(res)
                self.reflection(res[0], res[1], ftp_cmd)
            else:
                if ftp_cmd and ftp_cmd not in ['cd', 'lcd', 'get', 'put']:
                    print("\033[1;31m未知命令：\033[0m", ftp_cmd)

    def reflection(self, *args):
        """通过反射调用方法"""
        # print("reflect_args = ", args)
        if hasattr(self, args[0]):
            func = getattr(self, args[0])
            func(args[1], args[2])

    def put(self, *args):
        """传递 put 命令并接受服务器反馈"""
        # print("put_args = ", args)
        put_cmd = args[-1]
        put_file_path = os.path.join(self.lcd_path, args[0])
        # print(put_file_path)
        if os.path.isfile(put_file_path):
            # print("put file path = ", put_file_path)
            self.client.send(put_cmd.encode('utf-8'))
            with open(put_file_path, 'rb') as client_f:
                msg_dic = {"file size": os.stat(put_file_path).st_size}
                self.client.send(json.dumps(msg_dic).encode('utf-8'))
                server_response = self.client.recv(1024)
                if server_response.decode() == "ok":
                    for line in client_f:
                        self.client.send(line)
                    msg = self.client.recv(1024)
                    print(msg.decode())
        else:
            print("\033[1;31m没有找到文件 %s\033[0m" % args[0])

    def get(self, *args):
        """传递 get 命令并接受服务器反馈"""
        # print("get_args = ", args)
        get_cmd = args[-1]
        self.client.send(get_cmd.encode('utf-8'))  # 发送要 get 的文件信息
        server_response = json.loads(self.client.recv(1024).decode())
        # print(server_response)
        if server_response["file status"] == 1:  # 发来的是否为文件路径
            get_file_path = os.path.join(self.lcd_path, server_response["file name"])
            # print("get file path = %s" % get_file_path)
            if os.path.isfile(get_file_path):  # 该文件是否存在
                client_f = open(get_file_path + "_new", 'wb')
            else:
                client_f = open(get_file_path, 'wb')
            received_file_size = 0
            self.client.send("ok".encode('utf-8'))
            while received_file_size < server_response["file size"]:  # 判断已接收文件的大小
                # print("before size is %d" % received_file_size)
                get_file = self.client.recv(1024)
                received_file_size += len(get_file)
                # print("after size is %d" % received_file_size)
                client_f.write(get_file)
            client_f.close()
            print("\033[33m文件 %s 接收完成。\033[0m" % server_response["file name"])
        else:
            print(server_response["file status"])

    def cd(self, *args):
        """传递 cd 命令并接收服务器反馈"""
        # print("cd_args = ", args)
        cd_cmd = args[-1]
        self.client.send(cd_cmd.encode('utf-8'))
        server_response = self.client.recv(1024)
        print(server_response.decode())

    def lcd(self, *args):
        """更改当前本地目录"""
        # print("lcd_args = ", args)
        try:
            if args[0] == '..':
                self.lcd_path = os.path.dirname(self.lcd_path)
            elif os.path.isdir(args[0]):
                self.lcd_path = args[0]
            # 检测是否是文件夹
            elif os.path.isdir(os.path.join(self.lcd_path, args[0])):
                self.lcd_path = os.path.join(self.lcd_path, args[0])
            # 检测是否是文件
            elif os.path.isfile(os.path.join(self.lcd_path, args[0])):
                print("\033[1;31m%s 不是一个文件夹。\033[0m" % args[0])
            else:
                print("\033[1;31m找不到本地目录：%s\033[0m" % args[0])
            print("当前本地目录", self.lcd_path)
        except FileNotFoundError as e:
            print("\033[1;31m系统没有找到路径 %s\033[0m" % args[0])

    def ls(self, *args):
        """传递 ls 命令并接收服务器反馈"""
        # print("cd_args = ", args)
        cd_cmd = args[0]
        self.client.send(cd_cmd.encode('utf-8'))
        server_response = self.client.recv(1024)
        print(server_response.decode())
        # print("当前本地目录 %s 下有：\n%s" % (server_response.decode(), os.listdir(server_response.decode())))

    def lls(self, *args):
        """查看当前本地目录下所有文件和文件夹"""
        print("当前本地目录 %s 下有：\n%s" % (self.lcd_path, ", ".join(os.listdir(self.lcd_path))))

    def pwd(self, *args):
        # print("pwd_args = ", args)
        cd_cmd = args[-1]
        self.client.send(cd_cmd.encode('utf-8'))
        server_response = self.client.recv(1024)
        print(server_response.decode())

    def mkdir(self, *args):
        print("mkdir_args = ", args)
        mkdir_cmd = args[-1]
        self.client.send(mkdir_cmd.encode('utf-8'))
        server_reponse = self.client.recv(1024)
        print(server_reponse.decode())
