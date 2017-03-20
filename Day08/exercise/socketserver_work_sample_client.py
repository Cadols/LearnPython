#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import socket
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 6666))


class FtpClient(object):

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def help(self):
        msg = """
        ls
        pwd
        cd ..
        get filename
        put filename
        """

    def connect(self, ip, port):
        self.client.connect((ip, port))

    def interactive(self):
        # self.authenticate()
        while True:
            cmd = input(">>: ").strip()
            if len(cmd) == 0: continue
            cmd_str = cmd.split(" ")[0]
            if hasattr(self, "cmd_%s" % cmd_str):  # 如果有就用反射调用方法
                func = getattr(self, "cmd_%s" % cmd_str)
                func(cmd)
            else:  # 如果没有则调用help方法
                self.help()

    def cmd_put(self, *args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg_dic = {
                    "action": "put",
                    "filename": filename,
                    "size": filesize
                }
                self.client.send(json.dumps(msg_dic).encode('utf-8'))
                # 等服务器确认，以防止粘包
                server_respone = self.client.recv(1024)  # 可以返回多种状态，客户端根据状态处理后续（403,500,400）
                f = open(filename, 'rb')
                for line in f:
                    self.client.send(line)
                else:
                    print("file had been send")
                    f.close()
            else:
                print(filename, "is not exist.")

    def cmd_get(self):
        pass