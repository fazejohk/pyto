def twister():
    try:
        string = input(str("STRING HERE:\n"))
        if string[::-1] == string:
            print("Very nice")
        else:
            print("Fock off")
    except KeyboardInterrupt:
        exit()
while True:
    twister()
