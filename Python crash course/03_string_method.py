""" Logical Operator
These combine boolean values and conditions
"""

# AND = Both must be true
age = 25
has_license = True
can_drive = age >= 16 and has_license
print(can_drive)

# OR = At least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)

# NOT = reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)


age = 26
has_license = True
drunk = False
drive_permission = age >= 16 and has_license and not drunk
print(drive_permission)

""" Shortcuts Assignments """

score = 10
score = score + 5
score += 5
print(score)

""" F-string methods """

name = "Fluke"
message = f"Welcome Sir {name}!"
print(message)

text = "Nattawut Boonnoon"

print(text.lower())
print(text.upper())
print(text.title())

""" Cleaning Methods """

messy = "     Nattawut Boonnoon.   "
print(messy.strip()) # remove whitespace

price = "$19.99"
print(price.strip("$")) # 19.99