import socket
import threading

host = "192.168.10.36"
port = 4444

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)
print("Waiting for connection")
conn, addr = s.accept()
quitting = False
print("Connected by ", addr)

while not quitting:
    try:
        data, addr = s.recvfrom(1024)
        comment = raw_input("->\n")
        for client in clients:
            s.sendto(comment, addr)
    if addr not in clients:
        clients.append(addr)
            
