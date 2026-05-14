"""
Build on existing classes

Inheritance is an advanced Python concept that you probably won't use when starting out.
Most beginner programs work perfectly fine without it.
However, as your projects grow, inheritance can make your code much cleaner by avoiding repetition.

Inheritance lets you create new classes based on existing ones. The new class (child) gets everything from the parent class, plus can add its own stuff.
Think of it like this:

1. All dogs are animals (dogs inherit from animals)
2. Dogs have everything animals have, plus dog-specific things
"""

# Basic

# Parent class - general animal
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."
    
    def sleep(self):
        return f"{self.name} is sleeping"

# Child class - specific animal  
class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"
    
# Create a dog - using positional argument
my_dog = Dog("Buddy")
# Or with named argument
my_dog2 = Dog(name="Max")

# Dog can do animal things (inherited)
print(my_dog.eat()) # Buddy is eating
print(my_dog.sleep()) # Buddy is sleeping

# Dog can also do dog things
print(my_dog.bark()) # Buddy says woof!

# ==============================

# Adding attributes in child classes
# - Child classes can have their own attributes too:

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_pet = True

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # Pass name to parent's __init__
        self.breed = breed # Dog-specific attribute
    
    def describe(self):
        return f"{self.name} is a {self.breed}"
    
# Create dogs with breeds - positional arguments
golden = Dog("Buddy", "Golden Retriver")

# Or with named arguments (clearer)
poodle = Dog(name="Max", breed="Poodle")

print(golden.describe()) # Buddy is a Golden Retriever
print(golden.is_pet) # True (inherited from Animal)

# ==============================

# Overriding methods
# Child classes can change how parent methods work:

class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} makes a sound"
    
class Dog(Animal):
    def make_sound(self): # Override parent method
        return f"{self.name} barks: Woof!"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} meows: Meow!"

# Different animaks, different sounds
generic = Animal(name="Something")
dog = Dog(name="Buddy")
cat = Cat(name="Whiskers")

print(generic.make_sound()) # Something makes a sound
print(dog.make_sound()) # Buddy barks: Woof!
print(cat.make_sound()) # Whiskers meows: Meow!

# ==============================

# Real-World Use case
# Here’s a practical example for AI applications:

class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_loaded = False
    
    def load(self):
        print(f"Loading {self.model_name}...")
        self.is_loaded = True

class TextModel(BaseModel):
    def __init__(self, model_name, max_length=1000):
        super().__init__(model_name)
        self.max_length = max_length
    
    def process_text(self, text):
        if not self.is_loaded:
            self.load()
        # Truncate if needed
        if len(text) > self.max_length:
            text = text[:self.max_length]
        return f"Processed: {text}"

# Use the model - with named arguments
model = TextModel(model_name="gpt-5.5-turbo", max_length=100)

# Call method - notice no 'self' parameter needed
result = model.process_text(text="Hello world!")
print(result)  # Loading gpt-3.5-turbo...
               # Processed: Hello world