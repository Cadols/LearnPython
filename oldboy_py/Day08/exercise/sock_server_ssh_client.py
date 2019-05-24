#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 6666))
while True:
    cmd = input(">>: ").strip()
    if len(cmd) == 0:
        continue
    client.send(cmd.encode('utf-8'))
    cmd_res_size = client.recv(1024)  # 接收命令结果的长度
    print("收到的命令大小：", cmd_res_size)
    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data)  # 收到的数据可能小于1024
        print(received_size)
        received_data += data
        # print(data.decode())
    else:
        print("cmd has received done...", received_size)
        print(received_data.decode())
client.close()