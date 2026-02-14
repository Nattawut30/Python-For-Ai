# Encapsulation

class Person:

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        if value == 'Grace':
            self.__name = 'Default Name'
        else:
            self.__name = value

    @staticmethod
    # use it to define static methods
    def my_method():
        print("My name is Grace Ashcroft")

p1 = Person(name='Leon', age=51, gender='Male')
print(p1.Name)

p1.Name = 'Grace'
print(p1.Name)

# Call it here
Person.my_method()
p1.my_method()