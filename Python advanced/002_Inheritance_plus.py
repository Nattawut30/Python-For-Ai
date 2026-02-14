# ========== Inheritance Plus ==========

# Class parent & Class Child
# Animals (parent) = Dog (Child1), Cat (Child2)

# Parent
class Person:

    amount = 0

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        Person.amount += 1

    def __del__(self):
        Person.amount -= 1


    def __str__(self):
        return "Name: {}, Age: {}, Job: {}".format(self.name, self.age, self.job)

    def get_older(self, years):
        self.age += years

# Child
class Employee(Person):

    def __init__(self, name, age, job, salary):
        # accessing the parent class | use "super" and __init__
        # write it like this to not write everything once again!
        super(Employee, self).__init__(name, age, job)
        self.salary = salary

    def __str__(self):
        text = super(Employee, self).__str__() # inherit from parent class: str style
        text += ", Salary: {}".format(self.salary) # add another column
        return text

    def calculate_yearly_salary(self):
        return f"${self.salary * 12}"

Employee1 = Employee("Leon", 51, "Agents", 15000)
print(Employee1)
print(Employee1.calculate_yearly_salary())
print()

Employee2 = Employee("Chris", 60, "Captain", 18000)
print(Employee2)
print(Employee2.calculate_yearly_salary())
print()

# ========== Operator Overloading ==========

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # other object is also part of the operation
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return "X: {}, Y: {}".format(self.x, self.y)

v1 = Vector(x=2, y=5)
v2 = Vector(x=6, y=3)

print(v1)
print(v2)
print()

v3 = v1 - v2
print(v3)
