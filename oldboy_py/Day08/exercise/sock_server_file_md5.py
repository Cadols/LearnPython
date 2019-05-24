#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import socket
import hashlib

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 6666))
server.listen()

while True:
    conn, addr = server.accept()
    print("new conn:", addr)
    while True:
        print("Waiting for command.")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开。")
            break
        print("执行指令：", data)
        cmd, filename = data.decode().split()  #
        print("filename:", filename)
        if os.path.isfile(filename):
            f = open(filename, 'rb')
            m = hashlib.md5()
            file_size = os.stat(filename).st_size  # get file size
            conn.send(str(file_size).encode('utf-8'))  # send file size to client
            # 连续send 2条会粘包
            client_ack = conn.recv(1024)  # 接收客户端响应
            print("client ack: ", client_ack)
            for line in f:  # read line to get md5 and send line to client
                m.update(line)
                conn.send(line)
            print("file's md5:", m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode('utf-8'))  # send file's md5 to client
server.close()
