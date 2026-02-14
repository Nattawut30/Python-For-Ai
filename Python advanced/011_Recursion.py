# The function calling itself
# It could have created a stack overflow

# Factorial
# 9! = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
# 9! = 9 * 8!

# Recursive
n = 7
factorial = 1
while n > 0:
    factorial = factorial * n
    n -= 1

print(factorial)

# Non-Recursive
def factorial(n):
    if n < 1:
        return 1 # If n less than 1 I return 1
    else:
        number = n * factorial(n-1)
        return number

print(factorial(5))

# Fibonacci sequence: a functions that give me a value of a fibonacci number at some position
# the sequence that starts with 0 and 1 and the element is always the sum of the previous two elements
# 0, 1, 1, 2, 3, 5, ...

def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a + b

    return a

print(fibonacci(10)) # 0, 1, 1 = 2, Index 3 is 2

def fibonacci_two(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_two(n - 1) + fibonacci_two(n - 2))

print(fibonacci_two(10))

# In the first recursion I call 2 functions then both these two function
# Call two functions so now we have four then we got eight then 16, 32, ...
# an exponential runtime complex!