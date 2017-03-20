#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import hashlib

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 6666))

while True:
    cmd = input(">>: ").strip()
    if len(cmd) == 0:
        continue
    if cmd.startswith("get"):
        client.send(cmd.encode('utf-8'))
        server_response = client.recv(1024)  # 接收命令结果的长度
        print("server response:", server_response)
        client.send("ready to receive file.".encode('utf-8'))
        file_total_size = int(server_response.decode())
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename + ".new", 'wb')
        m = hashlib.md5()
        while received_size < file_total_size:
            if file_total_size - received_size > 1024:  # 接收多次
                size = 1024
            else:  # 最后一次接收
                size = file_total_size - received_size
                print("The last size:", size)
            data = client.recv(size)
            received_size += len(data)
            m.update(data)
            f.write(data)
        else:
            new_file_md5 = m.hexdigest()
            print("new file md5:", new_file_md5)
            print("Receive completed:", received_size, file_total_size)
        f.close()
        server_file_md5 = client.recv(1024)
        print("server file md5:", server_file_md5)
client.close()
