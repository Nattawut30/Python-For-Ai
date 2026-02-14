# Factory Design Pattern

# for working in individual program and classes and modules
# use them in the larger projects
# the class that everything do their own roles well!

# the factory class that actually build person objects!

from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def person_method(self) -> None:
        """ Interface Method """
        pass

# divided the "Creation Logic" out of "Usage Logic"

class Student(IPerson):

    def person_method(self) -> None:
        print("I am a student!")

class Teacher(IPerson):

    def person_method(self) -> None:
        print("I am a teacher!")

class PersonFactory:
    @staticmethod
    def build_person(person_type: str) -> IPerson:
        mapping = {
            "Student": Student,
            "Teacher": Teacher,
        }

        if person_type in mapping:
            return mapping[person_type]()

        raise ValueError(f"Unknown person type: {person_type} (???) ")

if __name__ == '__main__':
    try:
        choice = input("Enter a person type (Student/Teacher): ")
        person = PersonFactory.build_person(choice)
        person.person_method()
    except ValueError as e:
        print(f"Error: {e}")
