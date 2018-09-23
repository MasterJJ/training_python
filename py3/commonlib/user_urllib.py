#!/usr/bin/env ptthon3
# -*- coding: utf-8 -*-

from urllib import request, parse

# get:

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

# advanced get:

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Too tierd')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))

# post:

print('Login to WebService..')
email = input('Email:  ')
passwd = input('Password: ')
login_data =parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'google'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'too long information ... type is too tired sorry man ')
])

req = request.Request('https://example.com:8888')
proxy_auth_handler = urllib.request.ProxyBasicAuthhandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with openr.open('http://www.example.com/login.html') as f:
    pass






