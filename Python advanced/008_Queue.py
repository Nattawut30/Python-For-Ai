# One of the data structure
# sometimes when we run a lot of threads
# we need a way to run the data on processed and ordered.

import queue

q = queue.Queue()

# 1, 2, 3, 4, 5
# pop up = 1
# remaining: 2, 3, 4, 5

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for n in numbers:
    q.put(n)

print(q.get())
print(q.qsize()) #index

#LIFO = Last in, First Out
q1 = queue.LifoQueue()
items = [1, 2, 3, 4, 5, 6, 7]
for i in items:
    q1.put(i)

print(q1.get()) # It's just revered! | 7

# Allows you to give every element a certain priority by,
# passing a tuple ((x, y))
# the lower the number, the higher the priority
q2 = queue.PriorityQueue()
q2.put((1, True))
q2.put((13, 99))
q2.put((5, 7.5))
q2.put((2, "Hey!"))

while not q2.empty():
    print(q2.get())
    #print(q2.get() [1])