import ctypes
from time import strftime
again=True
def Main():
    xtime=strftime("%H:%M")
    yourtime=input(str("Time:\n"))
    comment=input(str("Comment:\n"))
    while xtime != yourtime:
        xtime=strftime("%H:%M")

    if xtime == yourtime:
        ctypes.windll.user32.MessageBoxW(0, comment, "ALARM", 1)

if __name__ == "__main__":
    Main()
