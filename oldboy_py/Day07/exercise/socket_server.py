#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import socket

server = socket.socket()
server.bind(('localhost', 6969))  # 绑定监听端口

server.listen(5)  # 监听，同时最高挂起 5 个连接。

while True:  # 重新连接新电话
    print("I'm going to wait the call: ")
    # conn 是客户端连接后，在服务器端为其生成的一个连接实例
    conn, addr = server.accept()  # 等通信过来
    print(conn, addr)
    print("The call is coming.")
    while True:  # 重复接受信息
        data = conn.recv(1024)  # 接收1024字节
        print("recv:", data.decode())
        if not data:
            print("Client has lost...")
            break
        # conn.send(data.upper())
        # res = os.popen(data).read()  # 发来系统命令直接执行
        # conn.send(res)
        conn.sendall(res)  # sendall 如果文件大小大于缓存区大小，循环 send 发送全部数据

server.close()
