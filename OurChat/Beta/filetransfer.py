import socket
import sys
import time

name = time.strftime("%y-%m-%d-%H-%M-%S")

s = socket.socket()
s.bind(("192.168.10.36",9999))
s.listen(10) # Acepta hasta 10 conexiones entrantes.
print "Waiting for packets"
while True:
    sc, address = s.accept()

    print address
    f = open(str(name) + ".txt",'wb') #open in binary
    while (True):
    # recibimos y escribimos en el fichero
        l = sc.recv(1024)
        while (l):
                f.write(l)
                l = sc.recv(1024)
    f.close()


    sc.close()

s.close()
