#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2019-12-19 16:36:14
@LastEditor: John
@LastEditTime: 2020-07-15 19:23:10
@Discription: 
@Environment: python 3.7.7
'''
import socket
import os
import time

def sendfile(conn,filename):
    #str1=conn.recv(1024)
    #filename=str1.decode('utf-8')
    #print('recv file name request is %s' %filename)
    if os.path.exists(filename):
        print("%s begin to send" % filename)
        size=1024
        with open(filename,'rb') as f:
            while True:
                data=f.read(size)
                conn.send(data)
                if len(data)<size:
                    break
        print('%s sended!' % filename)
    else:
        print('sorry file not exist!')


def sendmsg(s,msg):
    s.send(msg.encode('utf-8'))
    print('send file msg!')

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8008))
#filename='1.jpg'
#s.send(filename.encode('utf-8'))
#str1=s.recv(1024)
#str2=str1.decode('utf-8')
i=0

dirs=os.listdir("./send/")
for dirc in dirs:
    
    time.sleep(0.01)
    
    filename='./send/'+dirc 
    
    file_size=os.path.getsize(filename)
    print('size of filename is %d' %file_size)
    msg = filename + '##' + str(file_size)
    
    sendmsg(s,msg)
    sendfile(s,filename)
    
  

