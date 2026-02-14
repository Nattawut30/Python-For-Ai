# Before learn this series, get a fundamental first!
# Check out Folders "Python training" on my repo.

# ========== Classes and Objects Plus ==========

class Person:

    amount = 0

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        Person.amount += 1

    def __del__(self): # delete values
        Person.amount -= 1

    # We can write it like this too
    def __str__(self): # get string
        return "Name: {}, Age: {}, job: {}".format(self.name, self.age, self.job)

    def get_older(self, years):
        self.age += years

person1 = Person(name="Leon", age=51, job="Agents") #identify object right away
print(person1.name)
print(person1.age)
print(person1.job)
print()

person2 = Person(name="Chirs", age=60, job="Captain")
print(person2)
print()

del person2 # clear the memory and get out 1 person

print(Person.amount)