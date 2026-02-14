# Use multiple threads at once
# Access the same resource at the same time
# Even change it, it still works it.

import threading
import time

x = 8192

lock = threading.Lock() # we need to define this

def double():
    global x, lock # I wanna access that particular value and change it
    lock.acquire() # tries to acquire the lock if it's free, if it's not? just waiting here.
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1) # we're not going to be able to track what happens. so we need this.
    print("Reached the maximum!\n")
    lock.release()

    # It will lock the resource and executes it in order!

def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the minimum!\n")
    lock.release()

t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

# Endless loop at the same time
t1.start()
t2.start()