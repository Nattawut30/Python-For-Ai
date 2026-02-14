# an object that has function to be triggered,
# and when trigger it,
# we can make certain things happen

import threading
import time
import random

event = threading.Event()

def restaurant_fn():
    print("Welcome to our restaurant!\n")
    event.wait() # make them hold...
    print("What would you like to order?")

t1 = threading.Thread(target=restaurant_fn)
t1.start()

while True:
    x = input("\n Are you ready to orders? (Y/N): ").lower()
    if x == "y":
        event.set() # get the waitress works
        t1.join()
        break
    elif x == "n":
        print("The waitress will be back again...")
        wait_time = random.randint(1, 10) #random from 1-10 s.
        time.sleep(wait_time)

