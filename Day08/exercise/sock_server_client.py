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
    cmd_res = client.recv(1024)
    print(cmd_res.decode())

client.close()
