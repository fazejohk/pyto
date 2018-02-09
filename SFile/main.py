#! /usr/bin/python
#textin mita laitetaan sisaan muuttuu encryptatuksi tekstiksi
import os
import sys

if os.getuid() != 0:
       print "You need root permissions to do this, laterz!"
       sys.exit(1)
#===========================================
class Main():

    def Writing(self , text,  fileName):
        with open('/home/me/S/' + str(fileName), 'a') as output:
            output.write(str(text))

    def UWriting(self , text,  fileName):
        with open('/media/me/GGX/RandomFiles/' + str(fileName), 'a') as output:
            output.write(str(text))

    def Crypt(self, fileName):
        try:
            os.system("gpg -c /home/me/S/" + str(fileName))
            os.system("rm /home/me/S/" + str(fileName))
        except:
            print "File you are lookin for does not exist..."
            pass

    def UCrypt(self, fileName):
        try:
            os.system("gpg -c /media/me/GGX/RandomFiles/" + str(fileName))
            os.system("rm /media/me/GGX/RandomFiles/" + str(fileName))
        except:
            print "File you are lookin for does not exist..."
            pass

#===========================================
class Decrypt():

    def Show(self, fileName):
        try:
            print("\n")
            os.system("gpg -d /home/me/S/" + str(fileName) + ".gpg")
            print("\n")
        except:
            print "File doesnt exist"
            pass
#============================================
if __name__ == "__main__":
    try:
        what = sys.argv[1]
    except:
        what = ""
        pass
    crypt = Main()
    decrypt = Decrypt()
    filenam = raw_input("Filename:\n")
    if(os.path.isdir("/media/me/GGX/RandomFiles")):
        text = raw_input("U Go ahead...\n")
        crypt.UWriting(text, filenam)
        crypt.UCrypt(filenam)
        sys.exit(0)
    else:
        pass

    if (what != "d"):
        text = raw_input("Go ahead...\n")
        crypt.Writing(text, filenam)
        crypt.Crypt(filenam)
    elif(what == "d"):
        decrypt.Show(filenam)
