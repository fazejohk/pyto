import socket
import threading
from queue import Queue
import time

print_lock=threading.Lock()
target=str(input("Host:\n"))
to1=int(input("From port:\n"))
to2=int(input("To port:\n"))


def portscan(port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con=s.connect((target,port))
        with print_lock:
            print("Port",port,"is open!")
        con.close()
    except:
        pass
def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()
for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon=True
    t.start()

for worker in range(to1,to2):
    q.put(worker)

q.join()
