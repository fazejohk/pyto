from tkinter import *
from tkinter import ttk
import os

def get_update(event):
    os.system("shutdown -s -t 120")

def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())

    sumi = num1 + num2

    sumEntry.delete(0, "end")

    sumEntry.insert(0, sumi)
root = Tk()
"""
Components:
Button, Label, Canvas, Menu, Text, Scale, OptionMenu, Frame, CheckButton,
LabelFrame, MenuButton, PanedWindow, Entry, ListBox, Message, RadioButton,
ScrollBar, Bitmap, SpinBox, Image
"""
"""
Label(root, text="First Name").grid(row=0, sticky=W, padx=4)
Entry(root).grid(row=0, column=1, sticky=E, pady=4)

Label(root, text="Last Name").grid(row=1, sticky=W, padx=4)
Entry(root).grid(row=1, column=1, sticky=E, pady=4)

Button(root, text="Submit").grid(row=3)
"""
"""
Label(root, text="Description").grid(row=0, column=0, sticky=W)
Entry(root, width=50).grid(row=0, column=1)
Button(root, text="Submit").grid(row=0, column=8)

Label(root, text="Quality").grid(row=1, column=0, sticky=W)
Radiobutton(root, text="New", value=1).grid(row=2, column=0, sticky=W)
Radiobutton(root, text="Good", value=2).grid(row=3, column=0, sticky=W)
Radiobutton(root, text="Poor", value=3).grid(row=4, column=0, sticky=W)
Radiobutton(root, text="Damaged", value=4).grid(row=5, column=0, sticky=W)

Label(root, text="Benefits").grid(row=1, column=1, sticky=W)
Checkbutton(root, text="Free Shipping").grid(row=2, column=1, sticky=W)
Checkbutton(root, text="Bonus Gift").grid(row=3, column=1, sticky=W)
"""
#function joka pyörii kun nappia painaa
num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

updateButton = Button(root, text="MAGIC")
updateButton.bind("<Button-1>", get_update)
updateButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

root.mainloop()
