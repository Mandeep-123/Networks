# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 8000

# connect to the server on local computer
s.connect(('192.168.5.1', port))
msg ="1110111 1110011"
s.send(msg.encode())
# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection
s.close()