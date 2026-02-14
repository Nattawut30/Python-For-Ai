# Magic Methods and Dunder
# double underscore for class = def __xyz__ (self, x, y):
# Identified and called it

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Object is being deconstructed!")

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): # Vector is different to the others
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y)

    def __repr__(self): # represent the factors
        return f"X: {self.x}, Y: {self.y}"

    def __len__(self): # check the length of the object
        return 10 # If you identified this, it's always 10

    def __call__(self): # call the objects
        print("Hello!, Vector was called!")

p = Person(name="Fluke", age=26)

v1 = Vector(x=10, y=20)
v2 = Vector(x=50, y=60)
v3 = v1 + v2
print(v3.x)
print(v3.y)
print(v3)

print(len(v3))
v3()