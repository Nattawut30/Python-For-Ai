""" Make your programs smart with decisions

Making programs think
If this, then that


ATM: IF password correct, THEN allow access
APSS: IF user clicks button, THEN perform action
WEATHER APP: IF temperature < 0, THEN show snow icon
GAMES: IF health = 0, THEN game over
"""

# EX. 1 
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# EX. 2
has_ticker = True
age = 16

if has_ticker:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Needs supervision!")
else:
    print("Please buy a tickey first!")

""" 
LOOPS: let you repeat code without writing it multiple times.
instead of copying and pasting you tell python repeat the code for you.
"""

for index in range(5): # Index = i
    print("Hello!")

for i in range(10): # start to count from 0
    print(i)

for i in range(1, 6):
    print(i)

for i in range(0, 10, 2):
    print(i)