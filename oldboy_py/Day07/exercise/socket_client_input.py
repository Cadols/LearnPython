#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

client = socket.socket()  # 声明socket类型，同是生成socket连接对象
client.connect(('localhost', 6969))

while True:
    msg = input(">> ").strip()  # bytes 只支持ASCII，其他的需要encode
    if len(msg) == 0:continue
    client.send(msg.encode('utf-8'))  # 发送。 2.x可发送 bytes 和 string ，3.x只能发送 bytes
    data = client.recv(1024)  # 接收1024字节
    print("recv:", data.decode())

client.close()
