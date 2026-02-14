# If we don't use semaphore, the program gonna run everything all at once.
# Semaphore use it when tells them that the resource are limited!
# 5 players try to steal their seated but allowed only 3 seated for 1 rounds

# Your server available only 100 all at once but 1,000 people join together at the same time
# you set it Semaphore(100) the first 100 get in first. the left 900 have to wait.

# The files might crash or corrupted if we let it run everything at the same time at once

import threading
import time
import random

# build a semaphore to play it only 1 players
# The left 4 people have to wait
stadium_seats = threading.BoundedSemaphore(1)


def play_game(name):
    print(f" Player: {name} is waited...")

    # reserved your seat (If full, then please wait a moment)
    with stadium_seats:
        print(f" {name}: Your turned!")
        duration = random.randint(a=2, b=5)
        time.sleep(duration)  # Demonstrate play time
        print(f" {name}: Finished in {duration} seconds. Leaving seat...")

    # Automatic count +1 after the block 'with'
    # it show there's available seats left!


# There's 5 player but 3 seated!
friends = ["Ames", "Billy", "Cathy", "Danny", "Eve"]
threads = []

for name in friends:
    t = threading.Thread(target=play_game, args=(name,))
    threads.append(t)
    t.start()

# Asked program to waited everyone finished
for t in threads:
    t.join()

print("----- All players have finished! -----")