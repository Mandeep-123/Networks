#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
import datetime
import socket
import struct
import binascii

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
server_address = ('10.0.0.1', 8000)
s.bind(server_address)
s.listen(1)
print(s)
print ('Listening Socket')
def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m
    
while True:

    sc, addr = s.accept()
    
    while True:
        
        recibido = sc.recv(1024)
        if not recibido: break
    
        #b = bytearray(recibido)
        b = recibido.decode()
        test  = toBinary(b)
    
        print ('-----------------------------------------------------')
        print ('Message received at : ' + datetime.datetime.now().strftime("%H:%M:%S.%f"))
        print (test)
    
    sc.close()

s.close()