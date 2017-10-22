import time
start_time = time.time()
data = True
while data != False:
    try:
        print("--- %s seconds ---" % (time.time() - start_time))
    except KeyboardInterrupt:
        data = False
