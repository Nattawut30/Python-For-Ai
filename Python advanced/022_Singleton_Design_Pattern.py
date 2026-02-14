# Singleton Design Pattern

# We have a class and this class can only have one single instance
# Imagine you have a king1 who gonna orders him a king2, king3...
# There's only 1 king. the system will tell you to use the king1 not make a new one
# for preserving resources and correct of the data

# กฏเหล็กที่ห้ามมีตัวตนที่สอง

from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def show_details(self):
        """ Implement in Child Class """
        pass

class PersonSingleton(IPerson):

    # Preserving only 1

    __instance = None

    @staticmethod
    def get_instance():
        # If there's no king yet... then make it
        if PersonSingleton.__instance is None:
            # Make it default
            PersonSingleton("Admin", 99)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance is not None:
            # if there's one already... who dare to create new king will get kills
            raise Exception("Singleton!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    # Add method for change variables
    def update_data(self, new_name, new_age):
        self.name = new_name
        self.age = new_age
        print("===== Updated Data =====")

    # no need more staticmethod because we can call it on variables
    def show_details(self):
            print(f"Name: {PersonSingleton.get_instance().name}")
            print(f"Age: {PersonSingleton.get_instance().age}")

p1 = PersonSingleton("Leon", 51)
p1.show_details()

p2 = PersonSingleton.get_instance()
p2.show_details()

p1.update_data("Grace", 24)
print(f"Name of p2: {p2.name}")
print(f"Age of p2: {p2.age}")

print(f"Is it the same person?: {p1 is p2}") # must be TRUE only