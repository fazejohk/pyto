import socket
import threading
import time
import os.path
from random import randint
#File transfer
#Tee eka ingame currency
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
            for client in clients:
                print str(clients)
                s.sendto(str(addr) + str(clients), client)
        if "help" in str(data):
            for client in clients:
                print "Displaying commands..."
                s.sendto("Commands:\n Online=Shows all the people that are online\nq=Quits", client)
        if "Log" in str(data):
            for client in clients:
                s.sendto("Logging...", client)
                log.write("\n" + time.ctime(time.time()) + "\n" + str(client))
                s.sendto("Logging done", client)

        if addr not in clients:
            clients.append(addr)


        print time.ctime(time.time()) + str(addr) + ": :" + str(data)
        for client in clients:
            s.sendto(data, client)
    except:
        pass
s.close()
