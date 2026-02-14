# Generators

import sys

def my_generator(n):
    for x in range(n):
        yield x ** 3
        # essentially just a way of returning a value
        # but not in the way that you then get out of the function
        # you just get the next value

values = my_generator(100000000)

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(sys.getsizeof(values))
print()

def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print()

for x in range(100):
    print(x)

