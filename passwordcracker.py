import md5

counter = 1

pass_in = raw_input("Enter MD5 HASH\n")
pwfile = raw_input("Please define path to PASSW0rD\n")

try:
    pwfile = open(pwfile, "r")
except:
    print "File not found"
    quit()

for password in pwfile:
    filemd5 = md5.new(password.strip()).hexdigest()
    print "Current password number %d" % (counter)

    counter += 1

    if pass_in == filemd5:
        print "\nMatch Found. \nPassword is: %s" % password
        print "%d Passwords tried" % (counter)
        break
else:
    print "Password Not Found."
