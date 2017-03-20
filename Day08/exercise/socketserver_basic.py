#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                # if not self.data:
                #     print("Client is disconnected.")
                #     break
                self.request.send(self.data)
            except ConnectionResetError as e:
                print("ConnectResetError:", e)
                break

if __name__ == "__main__":
    HOST, PORT = "localhost", 6666
    # server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)  # 单线程
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)  # 多线程
    # server = socketserver.ForkingTCPServer((HOST, PORT), MyTCPHandler)  # 多进程，windows不可用
    server.serve_forever()
