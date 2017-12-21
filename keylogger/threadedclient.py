# -*- coding: utf-8 -*-
import time
import socket
import threading
from passlib.hash import sha256_crypt

#tee homma joka päivittää joka 5 minuutti ja näyttää kaikki jotka on onlines
tLock = threading.Lock()
shutdown = False

def Admin():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host, port))
    s.setblocking(0)

    global rT
    rT = threading.Thread(target=receiving, args=("RecvThread", s))
    rT.start()

    alias = "Admin"
    message = raw_input(alias + "-> ")
    while message != 'q':
        if message != '':
            s.sendto(alias + ": " + message, server)
        tLock.acquire()
        message = raw_input(alias + "-> ")
        tLock.release()
        time.sleep(0.2)
    if message == 'q':
        s.sendto("FAGGOT" + alias + ": " + "Left ", server)
        #tLock.acquire()
        #tLock.release()
def Osku():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host, port))
    s.setblocking(0)

    global rT
    rT = threading.Thread(target=receiving, args=("RecvThread", s))
    rT.start()

    alias = "Dr. MenBOB"
    message = raw_input(alias + "-> ")
    while message != 'q':
        if message != '':
            s.sendto(alias + ": " + message, server)
        tLock.acquire()
        message = raw_input(alias + "-> ")
        tLock.release()
        time.sleep(0.2)
    if message == 'q':
        s.sendto("FAGGOT" + alias + ": " + "Left ", server)
        #tLock.acquire()
        #tLock.release()
def Vilske():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host, port))
    s.setblocking(0)

    global rT
    rT = threading.Thread(target=receiving, args=("RecvThread", s))
    rT.start()

    alias = "Vilske"
    message = raw_input(alias + "-> ")
    while message != 'q':
        if message != '':
            s.sendto(alias + ": " + message, server)
        tLock.acquire()
        message = raw_input(alias + "-> ")
        tLock.release()
        time.sleep(0.2)
    if message == 'q':
        s.sendto("FAGGOT" + alias + ": " + "Left ", server)
        #tLock.acquire()
        #tLock.release()
def Tuukka():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host, port))
    s.setblocking(0)

    global rT
    rT = threading.Thread(target=receiving, args=("RecvThread", s))
    rT.start()

    alias = "Tuukka.Koistinen"
    message = raw_input(alias + "-> ")
    while message != 'q':
        if message != '':
            s.sendto(alias + ": " + message, server)
        tLock.acquire()
        message = raw_input(alias + "-> ")
        tLock.release()
        time.sleep(0.2)
    if message == 'q':
        s.sendto("FAGGOT" + alias + ": " + "Left ", server)
        #tLock.acquire()
        #tLock.release()

def receiving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print str(data)
        except:
            pass
        finally:
            tLock.release()
host = '192.168.10.36'
port = 12345
server = ('192.168.10.36', 12345)

list = open("l.txt").readlines()
hash = list[0].rstrip()
hash1 = list[1].rstrip()
hash2 = list[2].rstrip()
hash3 = list[3].rstrip()
print "Muista että sinun pitää päivittää viestit painamalla ENTER että näet onko tullut uusia viestejä\n"
login = str(raw_input("LOGIN:\n"))

if (sha256_crypt.verify(login, hash) == True):
    print "Tervetuloa Vilske\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host, port))
    s.setblocking(0)
    s.sendto("Vilske" + " IS BACKK!!", server)
    s.close()
    Vilske()
elif(sha256_crypt.verify(login, hash1) == True):
    print "Tervetuloa Tuukka.Koistinen\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host, port))
    s.setblocking(0)
    s.sendto("Tuukka.Koistinen" + " IS BACKK!!", server)
    s.close()
    Tuukka()
elif(sha256_crypt.verify(login, hash2) == True):
    print "Tervetuloa DR. MenBOOOOOM\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host, port))
    s.setblocking(0)
    s.sendto("DR. MenBOOOOM" + " IS BACKK!!", server)
    s.close()
    Osku()
elif(sha256_crypt.verify(login, hash3) == True):
    print "Tervetuloa ADMIN\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host, port))
    s.setblocking(0)
    s.sendto("Admin" + " IS BACKK!!", server)
    s.close()
    Admin()
else:
    print "Salasana väärin :)"
    time.sleep(1)
    exit(0)

shutdown = True
rT.join()
s.close()
