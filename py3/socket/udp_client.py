#!/usr/bin/env pytho3
# -*- coding: utf -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Lisa', b'MasterJ']:
    s.sendto(data, ('126.0.0.1', 9999))
    print(s.recv(1024).decode('utf-8'))

s.close()