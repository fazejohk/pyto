import socket
import sys

s = socket.socket()
s.connect(("192.168.10.36",9999))
data = raw_input("File:\n")
f = open (str(data), "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
s.close()
