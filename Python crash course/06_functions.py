""" Create a reuseable blocks of code
that do the specific tasks. so we don't write the same code several times.

A recipe you can follow multiple times
A machine that take input and produce output
A name shortcut for complex operations

Why?
Don't repeat myself
Stay organized
Fix bug Easier
Test your code
"""

# Basic
def function_name():
    # Code goes here
    # Must be indented
    pass

def greet():
    print("hello, world!")
    print("Welcome to Python for AI training")

# ----- Call the function -----
greet()

# Functions with logic
def check_weather():
    temperature = 25
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")

# Use the function
check_weather()

# ----- Local Variables -----
# Variables created inside a function only exist within that function

def calculate_price():
    price = 100
    tax = price * 0.1
    print(f"Total: {price + tax}")

calculate_price()  # Total: 110

# ----- Global Variables -----
# Variables created outside functions can be accessed anywhere

discount_rate = 0.15  # Global variable

def apply_discount(price):
    discount = price * discount_rate  # Can read global variable
    return price - discount

result = apply_discount(100)
print(result)  # 85.0

# ----- Good Practice -----
# Use parameters and returns!

def add_amounts(current_total, amount):
    return current_total + amount

total = 0
total = add_amounts(total, 10)
total = add_amounts(total, 20)
print(total) # 30