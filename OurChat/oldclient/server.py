import socket
import threading

s = socket.socket()
host = "192.168.10.36"
port = 12345
s.bind((host, port))

s.listen(5)
c, addr = s.accept()
print "Got connection from", addr

while True:
    data = c.recv(1024)
    if not data:
        break
    print "From connected user: " + str(data)
    c.send(data)
c.close()
