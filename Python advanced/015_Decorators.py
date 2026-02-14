# Decorators
# Add a certain functionally to a function or,
# they wrap the function with an additional functionality.
# function in function [he[hey]llo]

def my_decorator(function):
    # whatever we pass here, will pass there too!

    def wrapper(*args, **kwargs):
        print("I am decorating your function!")
        return_value = function(*args, **kwargs)
        return return_value

    return wrapper

@my_decorator # I'm decorating 'hello world' with the fn
def hello(person):
    print(f"Wassup, {person}!")
    return f"Hey, {person}!"

print(hello("Fluke")) # passing the ref. that's it!

# Practical Example #1 - Logging

def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open("logfile.txt", "a+") as f:
            f_name = function.__name__
            print(f"{f_name} returned value: {value}")
            f.write(f"{f_name} returned value {value}\n")
        return value

    return wrapper

@logged # decorating it
def add(x, y):
    return x + y

print(add(x=10, y=20))
# combine decorator

# Practical Example #2 - Timing

import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        f_name = function.__name__ # calls it
        print(f"{f_name} took, {after - before} seconds to execute!")
        return value

    return wrapper

# how fast can they execute!

@timed # decorating it
def time_tested(x):
    result = 1
    for index in range(1, x):
        result += index
    return result

print(time_tested(99999))

