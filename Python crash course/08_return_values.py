""" Get result back from your functions

So far, our functions have printed output.
But often you want functions to calculate something and give you the result to use elsewhere.

"""

# This function returns a value
def add_return(a, b):
    return a + b

# Now you can use the result
result = add_return(5, 3)
print(f"The result is {result}")  # The result is 8

# ----- The return Statement -----
def calculate_area(width, height):
    area = width * height
    return area

# Store the returned value
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft")  # Room size: 120 sq ft

# ----- Returning Multiple Values -----
def get_min_max(numbers):
    return min(numbers), max(numbers)

# Get both values
minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}") # Min: 1, Max: 9

# Or as a tuple
result = get_min_max([5, 2, 8, 1, 9])
print(result) # (1, 9)

# ----- Return vs Print -----
# return can store the values and use it later
# print only displays

def get_greeting_print(name):
    print(f"Hello, {name}!")  # Just displays

def get_greeting_return(name):
    return f"Hello, {name}!"  # Gives back value

# Can't use print version's output
message = get_greeting_print("Alice")  # Prints but returns None
print(message)  # None

# Can use return version's output
message = get_greeting_return("Alice")  # Returns the string
print(message.upper())  # HELLO, ALICE!

# Functions without explicit return statements return None