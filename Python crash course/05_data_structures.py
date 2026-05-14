"""
Store multiple values together

Think of it as containers:
Lists [] = a shopping list (ordered items)
Dictionaries = a phone book (name > number)
Tuples = a coordinates (fixed values)
Sets = a bag of unique items

"""

# ----- LISTS -----

# EX.1
age = 25
has_licence = False
my_list = ["Alice", 25, age, True, has_licence]
print(my_list)

# EX.2
pi = 3.14
mixed = ["Hello", 25, True, pi]
print(mixed)

name = mixed[0]
print(name)

value = mixed[-2]
print(value)

# EX.3
fruits = ["apple", "banana", "orange"]
print(fruits[0])
print(fruits[0:2])
print(fruits[1:])

fruits.append("Avocado")
fruits.remove("Avocado")
print(fruits)

# EX. 4

numbers = [3, 1, 4, 1, 5, 9]

print(len(numbers)) # 6 length
print(numbers.count(1)) # 2 count occurencies
print(numbers.index(4)) # 2 find position

numbers.sort() # sort in place
print(numbers) # [1, 1, 3, 4, 5, 9]

numbers.reverse() # Reverse order
print(numbers) # [9, 5, 4, 3, 1, 1]

duplicate_list = numbers.copy() # Create a copy

# ----- DICTIONARIES -----

# Empty dictionary
my_dict = {}

# Dictionaries with data
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person)

# Different ways to create
scores = dict(math=95, eng=87, science=92)
print(scores)

# EX. 1
person["name"]
person["age"]
person["city"]

person["license"] = True
print(person)
# del person["license"] = for deleting

# EX. 2

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ...])

# Check if key exists
if "name" in person:
    print("Name found!")
else:
    print("Name not found!")

# Update multiple values
person.update({"name": "Leon", "age": 31, "job": "DSO"})
print(person)

# ----- Tuples ------
# Like a lists but they can't be change once created
# They are unchangeable sequence!

# EX. 1

# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")
print(point)

# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = (42)  # This is just 42 in parentheses
print(single)

# Without parentheses (implicit)
coordinates = 10, 20

# EX. 2
print(point[0])      # 3
print(colors[-1])    # "blue"

# Unpack values
x, y = point  # x = 3, y = 5
print(x, y)

# Swap variables elegantly
x, y = y, x  # Swaps values!
print(x, y)

# ----- Sets -----
# Sets are collections that only store unique values. They automatically remove duplicates

# Think of sets like:
# A bag of unique marbles
# Guest list (each person once)
# Unique tags or categories

# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}
print(unique_scores)

names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))
print(unique_names)  # ['Alice', 'Bob', 'Charlie']

# Logical Checking
allowed_users = {"alice", "bob", "charlie"}

if "alice" in allowed_users:  # Very fast!
    print("Access Granted")
else:
    print("Access Denied!")