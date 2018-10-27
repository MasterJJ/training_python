#!/usr/bin/env python3

import socket

prot = 60000

s = socket.socket()
hots = socket.gethostname()
s.bind((host, port))
s.listen(5)


print('Server listening....')

while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Servr received', repr(data))

    filename = 'mytext.txt'
    f = open(filename, 'rb')
    in_data = f.read(1024)
    while (in_data)
        conn.send(in_data)
        print('Sent', repr(in_data))
        in_data = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connection')
    conn.close()

# client side server
import socket

s = socket.socket()
host = socket.gethostname()
port = 60000

s.connect((host, port))
s.send("Hello server!")

with open('receved_file', 'wb') as f:
    print('file opend')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        f.write(data)


f.close()
print('Successfully get the file')
s.close()
print('connection closed')

    
