#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2019-12-19 17:25:16
@LastEditor: John
@LastEditTime: 2020-07-15 19:41:48
@Discription: 
@Environment: python 3.7.7
'''
import socket
import os
import time
import _thread
import base64

recv_path='./recv/'


def recvfile_size(conn,filename,file_suffix,filesize): 
    recvname=recv_path+filename+'my'+file_suffix
    size=1024 
    with open(recvname,'wb') as f:  
        while True: 
            data=conn.recv(size)
            f.write(data) 
            filesize-=size 
            if filesize<=0:
                break
    print('downloaded!!')

def recvmsg(conn): 
    data=conn.recv(1024)
    strmsg=data.decode('utf-8')
    if strmsg=='':
        return None, None
    s1,s2=strmsg.split('##')
    slist=s1.split('/')
    nlist=slist[-1].split('.')
    print('receive message name is %s ,size is %s' %(nlist[0],s2))
    return nlist[0],"."+nlist[-1],int(s2)

from signal import signal, SIGPIPE, SIG_DFL, SIG_IGN
signal(SIGPIPE, SIG_IGN)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8008))
s.listen(1)
print('wait for connecting...')

i=0
flag=0
(conn,addr)=s.accept()

while True:
    filename,file_suffix,filelen=recvmsg(conn)
    print("filename ", filename)
    if filename is None:
        break
    print("len is %d",filelen)
    if filelen>1000:
        recvfile_size(conn,filename,file_suffix,filelen)

  

    
        


