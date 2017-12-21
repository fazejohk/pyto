import md5
import os
import datetime as dt

counter = 1

pass_in = raw_input("Enter MD5 HASH\n")
pwfile = raw_input("Please define path to PASSW0rD\n")
start = dt.datetime.now()

try:
    pwfile = open(pwfile, "r")
except:
    print "File not found"
    quit()

for password in pwfile:
    filemd5 = md5.new(password.strip()).hexdigest()
    #print "Current password number %d" % (counter)

    counter += 1

    if pass_in == filemd5:
        end = dt.datetime.now()
        print "\nMatch Found. \nPassword is: %s" % password
        print "%d Passwords tried" % (counter)
        print "Time spend: {}".format(end - start)
        break
else:
    end = dt.datetime.now()
    print "Password Not Found."
    print"Time wasted {}".format(end - start)
