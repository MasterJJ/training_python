#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from ftplib import FTP
ftp = FTP('xxx.xxx.x.x.') 
ftp.login(user='usrname', passwd='password')
ftp.cwd('/Enter the directory here/')


def ReceivedFile():
    FileName = 'example.txt'
    LocalFile = open(FileName, 'wb')
    ftp.retrbinary('RETR' + FileName, LocalFile.write, 1024)
    ftp.quit()
    LocalFile.close()


def SendFile():
    FileName = 'example.txt'
    ftp.storbinary('STOR' + FileName, open(FileName, 'rb'))
    ftp.quit()

