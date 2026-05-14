"""
Handle errors gracefully

Errors happen. Files might not exist, APIs might be down, 
users might enter invalid data.
Error handling lets your program deal with these problems gracefully instead of crashing.

"""

# Missing Colon
# Forget to define value
x = 2
if x > 5: # syntaxerror
    print("Big Number")
else:
    print("Tiny Number")

# Why handle errors?
# This will crash if the file doesn't exist
with open('data.txt', 'r') as f:
    content = f.read()
print("Done!")  # Never reaches here if file missing

# Build the program that keeps running even if file doesn't exist

try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Could not find data.txt")
    content = "default data"
print("Done!")  # Always reaches here

"""
Try and Except
- helps catch errors before they crash

"""

try:
    result = 10 / 0 # ZeroDivision
except:
    print("Something went wrong, but hi there!")

# ===========================================

# Multiple error types
# - handle different erros differently

try:
    # Read a number from a file
    with open('number.txt', 'r') as f:
        text = f.read()
    number = int(text)
    result = 100 / number
    print(f"Result: {result}")
except FileNotFoundError:
    print("Could not find number.txt")
except ValueError:
    print("File doesn't contain a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# ===========================================

# The else clause
# - Code in "else" runs only if error happended:
try:
    with open('data.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
else:
    # This only runs if the file was opened successfully
    print(f"File has {len(data)} characters")

# ===========================================

# The finally clause
# - Code in 'finally' always runs, error or not:

try:
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    # This always runs to clean up
    if 'file' in locals() and not file.closed:
        file.close()
    print("Cleanup complete")