#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys

HOST, PORT = 'localhost', 6666
data = " ".join(sys.argv[1:])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    received = str(sock.recv(1024), 'utf-8')
finally:
    sock.close()

print("Sent:     {}".format(data))
print("Received: {}".format(received))
