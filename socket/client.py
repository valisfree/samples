#!/usr/bin env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()

sock.connect(('localhost', 9090))
mess = "hello world!"
sock.send(mess.encode("utf-8"))

data = sock.recv(1024)
sock.close()

print(data.decode("utf-8"))
