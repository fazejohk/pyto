def twister():
    try:
        string = input(str("STRING HERE:\n"))
        print(string[::-1])
    except KeyboardInterrupt:
        exit()
while True:
    twister()
