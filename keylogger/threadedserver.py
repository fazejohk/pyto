import socket
import threading
import time
import os.path
from random import randint

host = "192.168.10.36"
port = 12345
log = open("log.txt", "a+")


clients = []


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

quitting = False
print "Server Started."

while not quitting:
    try:
        data, addr = s.recvfrom(1024)
        if "Quit" in str(data):
            quitting = True
        if "Online" in str(data):
            log.write("\n" + clients)

        if addr not in clients:
            clients.append(addr)


        print time.ctime(time.time()) + str(addr) + ": :" + str(data)
        for client in clients:
            s.sendto(data, client)
    except:
        pass
s.close()
