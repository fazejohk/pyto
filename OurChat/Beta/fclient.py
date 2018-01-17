import socket

host = "192.168.10.36"
port = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((host, port))
s.setblocking(0)
s.send("Connected")
data = s.recv(1024)
s.close()
print 'Received ', repr(data)    
