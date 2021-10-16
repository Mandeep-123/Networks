#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
import socket


HOST = '127.0.0.1'   
PORT = 1650
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    s.close()
    print ('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

s.listen(1)
print(s)
print ('Listening on port: '+str(PORT))
def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m
    
while True:

    msg, addr = s.accept()
    
    while True:
        
        received = msg.recv(1024)
        if not received: break
    
        #b = bytearray(recibido)
        text = received.decode()
        result  = toBinary(text)
    
        print ('-----------------------------------------------------')
        print (result)
    
    msg.close()
s.close()