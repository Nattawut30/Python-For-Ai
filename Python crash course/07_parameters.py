""" Pass data into your functions

Parameters let you pass data into functions.
Instead of hardcoding values, you make functions
flexible to work with different inputs.

"""
# ----- Basic -----

# With parameters (flexible)
def greet(name):
    print(f"Hello, {name}!")

# Now it works for anyone
greet("Alice")
greet("Bob")
greet("Charlie")

# ----- Multiple Parameters -----
# Functions can have multiple parameters

def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

# Order matters!
calculate_total(100, 0.08, 10) # 98
print(calculate_total)

# ----- Keyword Arguments ------
# Call functions using parameter names for clarity

def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")

# Positional arguments (order matters)
create_profile("Alice", 25, "NYC")

# Keyword arguments (order doesn't matter)
create_profile(city="NYC", age=25, name="Alice")
create_profile(name="Bob", city="LA", age=30)
