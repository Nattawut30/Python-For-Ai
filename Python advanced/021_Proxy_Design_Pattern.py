# Proxy Design Pattern

# Quite similar to the decorator design pattern
# Wrapping functionality around object creation
# or additional layer for abstraction or protection for creating instance

from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):
    @abstractmethod

    def person_method(self):
        """ Interface Method """
        pass

class Person(IPerson):

    def __init__(self):
        print("=== Heavy Person Object Created ===")

    def person_method(self):
        print("I am a person! (Executing real logic)")

# Access Control

class ProxyPerson(IPerson):

    def __init__(self, access_code):
        self.person = None # no creation until granted the access!
        self.access_code = access_code

    def person_method(self):
        if self.access_code == "SECRET_123":
            print("[Proxy]: Access Granted!")
            # Created only correct password
            if self.person is None:
                self.person = Person()
            self.person.person_method()
        else:
            print("[Proxy]: Access Denied. No object was created.")
        # You control what happens when you call certain methods
        # calling the functions directly

print("Test 1: Wrong password")
p1 = ProxyPerson("Wrong123")
p1.person_method()

print("\nTest 2: Correct password")
p2 = ProxyPerson("SECRET_123")
p2.person_method()

# Golden rules of Proxy Pattern

# 1. Same Interface (Identity)
# The Proxy and the Real Object must look exactly the same.
# They must implement the same interface so the user doesn't know
# they are talking to a "representative."
# Simple phrase: "Look like the real thing."

# 2. Access Control (The Gatekeeper)
# The Proxy stands in the middle to decide if, when, and how
# the user can access the Real Object.
# This includes checking permissions (Security) or saving results (Caching).
# Simple phrase: "Control the access."

# 3. Lazy Initialization (The Middleman)
# The Proxy should only create the "Heavy" Real Object when it is absolutely necessary.
# This saves memory and speeds up the system.
# Simple phrase: "Create only when needed."