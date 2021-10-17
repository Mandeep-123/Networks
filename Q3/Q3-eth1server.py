#!/usr/bin/python
#-*- coding: utf-8 -*
import datetime
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
server_address = ('192.16.5.1', 8000)
s.bind(server_address)
s.listen(1)
print(s)
print ('Listening Socket')

def stringconversion(binary_input):
  binary_values = binary_input.split()

  output_string = ""
  for binary_value in binary_values:
      temp = int(binary_value, 2)
      ascii_character = chr(temp)
      output_string += ascii_character
  return (output_string)

while True:

    sc, addr = s.accept()
    
    while True:
        
        recibido = sc.recv(1024)
        if not recibido: break
    
        #b = bytearray(recibido)
        b = recibido.decode()
        test  = stringconversion(b)
    
        print ('-----------------------------------------------------')
        print ('Message received at : ' + datetime.datetime.now().strftime("%H:%M:%S.%f"))
        print (test)
    
    sc.close()
s.close()