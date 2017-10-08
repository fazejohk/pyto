import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=str(input("Host:\n"))
to1=int(input("From port:\n"))
to2=int(input("To port:\n"))
server=host

def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(to1,to2):
    if pscan(x):
        print("PORT ",x," IS OPEN!")
    else:
        print("Port ",x,"is closed")
