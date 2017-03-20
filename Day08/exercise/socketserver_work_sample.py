#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic["action"]
                if hasattr(self, action):
                    func = getattr(self, action)
                    func(cmd_dic)
                self.request.send(self.data)
            except ConnectionResetError as e:
                print("ConnectResetError:", e)
                break

    def put(self, *args):
        """接收客户端文件"""
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        filesize = cmd_dic["size"]
        if os.path.isfile(filename):
            f = open(filename + ".new", 'wb')

        else:
            f = open(filename, 'wb')

        self.request.send(b"200 ok")  # 返回标准码
        received_size = 0
        while received_size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            received_size += len(data)
        else:
            print("file %s have been uploaded." % filename)
            f.close()

if __name__ == "__main__":
    HOST, PORT = "localhost", 6666
    # server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)  # 单线程
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)  # 多线程
    # server = socketserver.ForkingTCPServer((HOST, PORT), MyTCPHandler)  # 多进程，windows不可用
    server.serve_forever()
