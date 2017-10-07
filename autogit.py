#! /usr/bin/python3
from tkinter import *
from tkinter import ttk
import os

euid = os.geteuid()
if euid != 0:
    print("Script is not running as root please run it as root...")


def Update(event):
    os.system("sudo apt update; sudo apt upgrade -y")

def Autogit(event):
    commit=str(input("Commit:\n"))
    os.system("git add .; git commit -m " + commit + "; git push pyto master")

root=Tk()

aub=Button(root, text="Autogit")
aub.bind("<Button-1>", Autogit)
aub.config(width=20, height=20)
aub.pack(side=LEFT)

upb=Button(root, text="Update")
upb.bind("<Button-1>", Update)
upb.config(width=20, height=20)
upb.pack(side=RIGHT)

root.mainloop()
