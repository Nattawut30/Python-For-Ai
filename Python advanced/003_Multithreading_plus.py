# ========== Multithreading Plus ==========

# Useful when you works with Video Game or AI/ML
# You absolutely need multiple threads for different things

# first thread maybe for user input
# second thread could be for what to do with mouse or keyboard
# third thread can be for rendering graphic or for sounds
# and so on....

import threading

print_lock = threading.Lock()

def hello(name):
    for x in range(10):
        with print_lock: # use lock for books a queue print
            print(name)

def goodbye(name):
    for y in range(10):
        with print_lock:
            print(name)

# you can write it like this too...
t1 = threading.Thread(target=hello, args=("ONE",))
t2 = threading.Thread(target=goodbye, args=("ZERO",))

# Execute both function at the same time!
t1.start()
t2.start()

# Even though I run the function here
# The program not gonna waiting for the function to finish
print("Hi, there!")

# Waiting thread (preventing finishing program)
# use this to proceed it until it's finished!
t1.join()
t2.join()

# As you can see The program executes both thread and print "hi there"
# After finished, the program is done!
print("--- Done ---")