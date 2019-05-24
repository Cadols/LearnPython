#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 6666))
server.listen()

while True:
    conn, addr = server.accept()
    print("new conn:", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已断开。")
            break
        print("执行指令：", data)
        cmd_res = os.popen(data.decode()).read()  # 接收字符串，执行结果也是字符串
        print("Before send.")
        if len(cmd_res) == 0:
            cmd_res = "cmd_res does not exist."
        conn.send(str(len(cmd_res.encode('utf-8'))).encode('utf-8'))
        # 连续send 2条会粘包
        client_ack = conn.recv(1024)  # 接收客户端响应
        print("client ack: ", client_ack)
        conn.send(cmd_res.encode('utf-8'))
        print("After send.")
server.close()
