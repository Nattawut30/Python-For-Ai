"""
Chapter 01: Basic Math and Calculus Review
"""

""" 1. Order of Operations """
# 1.1: 
# PEMDAS = parentheses, exponents, multiplication, division, addition, subtraction
print(2 + 3 * 4)  # Output: 14
print((2 + 3) * 4)  # Output: 20
print(10 / 2 * 5)  # Output: 25.0
print(10 / (2 * 5))  # Output: 1.0

# Exponents
print(2**3)  # Output: 8
print(5**2)  # Output: 25
print(9**0.5)  # Output: 3.0
print(16 ** (1 / 4))  # Output: 2.0

# Making use of parentheses for clarity
my_value = 2 * ((3 + 2) ** 2 / 5) - 4
print(my_value)

# ========================================

""" 2. Variables """
# 1.2:

x = int(input("Please input a number\n: "))
product = 3 * x
print(product)

# Greek variable names
beta = 1.75
theta = 30.0
print(beta * theta)

# Expressing subscripted variables
x_1 = 3
x_2 = 10
x_3 = 44
print(x_1 + x_2 + x_3)

# ========================================

""" 3. Functions """
# 1.3: 

# y = 2x + 1
x = int(input("Please input x values\n: "))
y = 2 * x + 1
print(y)

# f(x) = 2x + 1
def f(x):
    return 2 * x + 1


x_values = [0, 1, 2, 3]

for x in x_values:
    y = f(x)
    print(y)

# Using SymPy to plot the linear function
# Don't forget to installed the package
from sympy import *

x = symbols("x")
f = x ** 2 + 1
plot(f)

# three Dimensional plotting
# f(x, y) = 2x + 3y
from sympy import *
from sympy.plotting import plot3d

x, y = symbols("x y")
f = 2 * x + 3 * y
plot3d(f)

# ========================================

""" 4. Summation """
# 1.4:

# Expressed as a sigma Σ and adds elements together.
# ∑i = 1 to 5, 2i = 2(1) + 2(2) + 2(3) + 2(4) + 2(5) = 30

summation = sum(2*i for i in range(1, 6))
print(summation)

# Reminder: Python starting at index 0
# Summations of elements
# ∑i = 1 to n, 10xi
x = [1, 4, 6, 2]
n = len(x)

summation = sum(10*x[i] for i in range(0,n))
print(summation)

# iterate i from 1 through n, multiply each i, and sum them. 
# But then we use the subs() function to specify n as 5, 
# which will then iterate and 
# sum all ielements from 1 through n:
from sympy import *

i,n = symbols('i n')

# iterate each element i from 1 to n,
# then multiply and sum
summation = Sum(2 * i, (i, 1, n))

# specify n as 5
# iterating the numbers 1 through 5
up_to_5 = summation.subs(n, 5)
print(up_to_5.doit()) # 30

# ========================================

""" 5. Exponents """

# 2^3 = 2 * 2 * 2 = 8

# x^2 / x^5
# = x * x / x * x * x * x * x (x * x cut x * x)
# = 1 / x * x * x
# = move up = x^-3

# x^0 = 1

# 1.5:
from sympy import *

x = symbols("x")
expr = x ** 2 / x ** 5
print(expr) # x**(-3)

# Fractional exponents
# roots and square root

# 4^1/2 = sqrt(4) = 2
# 8^1/3 = root3(8) = 8 = 2 * 2 * 2. The answer is 2
# cbrt(8) = 8^1/3 * 8^1/3 * 8^1/3 = 8^1/3 + 8^1/3 + 8^1/3 = 8^1 = 8

# Power Rule
# (8^3)^2 = 8^3 * 8^3 = 8^3+3 = 8^6
# 8^2/3 = (8^1/3)^2 = (2^3/3)^2 = 2^2 = 4
# 8^pi = 8^3.14 / 100 = 

# ========================================

""" 6. Logarithms """

# 2^x = 8, we know the answer is x = 3
# a^x = b, loga^b = x

# 1.6:
from math import log
# 2 raised to that power gives me 8?

x = log(8, 2)
print(x) # 3.0

# ========================================

""" 7. Euler's Number or e """
# e = 2.71828

# Compound Interest
# A = P * (1 + r / n)^nt
# A = balance
# P = starting investment
# r = interest rate
# t = time span (number of years)
# n = periods (number of months in each year)

# 1.6:

from math import exp

p = 100 # start investing
r = 0.20 # interest rate
t = 2.0 # for 2 years
n = 12 # 12 months

a = p * (1 + (r / n))**(n * t)
print(a) # total balance after 2 years = 148.691...

# What if compound interest daily? change n to 365!
# What if compound interest hour? change n to 8,760!
# What if compound interest minute? change n to 525,600!

# Notics? we are gaining smaller and smaller
# That's why we need to use e = 2.71828

# 1.7:
# A = p * e^r * t
# we use e to get the closest to our value when compounding
from math import exp

p = 100 # principal, starting amount
r = 0.20 # interest rate, by year of 20% or .20
t = 2.0 # time, number of years

a = p * exp(r*t)
print(a) # 149.182469...

# basically, e is the resulting value of the expression (1 + 1 / n)^n

# ========================================

""" 8. Natural Logarithms """
# log() function is e.
# loge^10 = ln(10)

# 1.8:
from math import log

# e raised to what power gives us 10?
x = log(10)

print(x) # 2.30258...

# ========================================

""" 9. Limits """
# lim x -> ∞, 1 / x = 0
# as x approaches infinity, the function 1/x approaches 0 (but never reaches 0)

# 1.9: 
# calculate limits, infinity = oo in sympy
from sympy import *

x = symbols("x")
f = 1 / x
result = limit(f, x, oo)

print(result) # 0

# 1.10:
# Just like Euler's number e this way too...
# lim x -> ∞, (1 + 1 / n)^n = e = 2.178281...
from sympy import *

n = symbols("n")
f = (1 + (1 / n)) ** n
result = limit(f, n, oo)

print(result) # E
print(result.evalf()) # 2.71828182845905

# ========================================

""" 10. Derivatives """

# f(x) = x^2 how "steep" is the curve at x = 2?
# Think of a tangent line as a straight line that “just touches” the curve at a given point

# Take x = 2 and a nearby value x = 2.1,
# which when passed to the function f x = x2
# will yield f(2) = 4 and f(2.1) = 4.41

# m = y2 - y1 / x2 - x1
# m = 4.41 - 4.0 / 2.1 - 2.0
# m = 4.1

# 1.11:
# Calculate derivative
def derivative_x(f, x, step_size):
    m = (f(x + step_size) - f(x)) / ((x + step_size) - x)
    return m

def my_function(x):
    return x**2

slope_at_2 = derivative_x(my_function, 2, .00001)
print(slope_at_2) # 4.000010000000827

# 1.12:
# d / dx indicates a derivative with respect to x
# d / dx * f(x) = d / dx * x^2 = 2x
# d / dx * f(2) = 2(2) = 4
from sympy import *

# Declare 'x' to SymPy
x = symbols('x')

# use Python syntax to declare function
f = x**2

# Calc. the derivative of the function
dx_f = diff(f)
print(dx_f) # 2*x

# 1.13:
# try diff() to calc. the derivative function
def f(x):
    return x**2
def dx_f(x):
    return 2*x

slope_at_2 = dx_f(2)
print(slope_at_2) # 4

# ========================================

""" 11. Partial Derivatives """

# Multiple input variables
# x and y variable each get their own derivatives

# 1.14:
# 2x^3 > bring 3 * 2 and ^-1.
# = (2x * 3)^3-1 = 6x^2
# Slap the power number down and -1, then * with the number infront of variables
# 3y^3 => (3y * 3)^3-1 => 9y^2
from sympy import *
from sympy.plotting import plot3d

# Declare x and y 
x,y = symbols('x y')

# Declare function
f = 2*x**3 + 3*y**3

# Calc. the partial derivatives
dx_f = diff(f, x)
dy_y = diff(f, y)

print(dx_f) # 6*x**2
print(dy_y) # 9*y**2

# plot the fx.
plot3d(f)

# If x,y = 1,2
# the slope x is 6(1)^2 = 6, the slope y is 9(2)^2 = 36 

# 1.15:
# Apply Limits to Calc. Derivative
# lim s -> 0, (x + s)^2 - x^2 / (x + s) - x
# lim s -> 0, (2 + s)^2 - 2^2 / (2 + s) - 2 = 4
from sympy import *

# 'x' and step size 's'
x, s = symbols('x s')

# declare fx.
f = x**2

# slope between 2 points with gap "s"
# substitute into rise-over-run formula
slope_f = (f.subs(x, x + s) - f) / ((x+s) - x)

# substitute 2 for x
slope_2 = slope_f.subs(x, 2)

# calculate slope at x = 2
# infinitely approach steop size _s_ to 0
result = limit(slope_2, s, 0)

print(result) # 4

# 1.16:
# Not assign a specific value to x
from sympy import *

# "x" and step size "s"
x, s = symbols('x s')

# declare function
f = x**2

# slope between two points with gap "s"
# substitute into rise-over-run formula
slope_f = (f.subs(x, x + s) - f) / ((x+s) - x)
# calculate derivative function

# infinitely approach step size +s+ to 0
result = limit(slope_f, s, 0)
print(result) # 2x

# ========================================

""" 12. The Chain Rule """

# Important for neural network layers!

# Power Rule = Slap power number in front and minus ^-1
# Constant Rule = empty diff without varialbes = always 0

# 1.17: 
# y = x^2 + 1
# z = y^3 - 2
# we can use the 'y' in 'z'
# z = (x^2 + 1)^3 - 2

from sympy import *

z = (x**2 + 1) ** 3 - 2
dz_dx = diff(z, x)
print(dz_dx)

# dz / dx ((x^2 + 1)^3 - 2) Move -2 to +2 and slap 3
# dz = dx * 2*3 (x^2 + 1)^3-1
# dz = 6x (x^2 + 1)^2 we slap 3 to multiply with 2, remaining 2

# Derivative Seperately on the Chain Rule
from sympy import *

x, y = symbols('x y')

# derivative for first function
# need to underscore y to prevent variable clash

_y = x**2 + 1
dy_dx = diff(_y)

# derivative for second function
z = y**3 - 2
dz_dy = diff(z)

# Calc. derivative with and without
# chain rule, substitue y function
dz_dx_chain = (dy_dx * dz_dy).subs(y, _y)
dz_dx_no_chain = diff(z.subs(y, _y))

# Prove chain rule by showing both are equal
print(dz_dx_chain)
print(dz_dx_no_chain)

# ========================================

""" 13. Integrals """

# Find the area under the curve for a given range.
# Hacks: looking for a geometry and calc. it

# 1.18:
# f(x) = x^2 + 1, Graph: U, find the area under the curve on x
# a = min
# b = max
# n = number of rectangles to pack
# f = fx. we are integrating
def approximate_integral(a, b, n, f):
    delta_x = (b - a) / n
    total_sum = 0
    
    for i in range(1, n + 1):
        midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
        total_sum += f(midpoint)
    return total_sum * delta_x

def my_function(x):
    return x**2 + 1

area = approximate_integral(a=0, b=1, n=5, f=my_function)
print(area) # 1.33

# 1.19:
# Looks like we got smaller 1.33... so maybe the answer is 4/3
# prove it!
from sympy import *

x = symbols('x')
f = x**2 + 1

# Calc. the integral of the function with respect to x
# for the area between x = 0 and 1
area = integrate(f, (x, 0, 1))
print(area) # if 4/3 then correct!

# 1.20:
# Apply Limits with Integrals
from sympy import *

x, i, n = symbols('x i n')
f = x**2 + 1
lower, upper = 0, 1

# Calc. width and each rectangle heigh at index 'i'
delta_x = ((upper - lower) / n)
x_i = (lower + delta_x * i)
fx_i = f.subs(x, x_i)

# Iterate all 'n' rectangles and sum their areas
n_rectangles = Sum(delta_x * fx_i, (i, 1, n)).doit()

# Calc. the area by approaching the number
# of rectangles 'n' to infinity
area = limit(n_rectangles, n, oo)

print(area) # 4/3