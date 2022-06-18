import os
import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tests connection and sees whether or not it passes or fails
try:
    mySocket.connect(('data.pr4e.org',80))
    print("Connected.")
except:
    print("Did not connect.")
    quit()

# Found that this only works with "http" and not "https"
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mySocket.send(cmd)

while True:
    data = mySocket.recv(1024)
    if len(data) < 1:
        break
    print(data.decode())
mySocket.close()