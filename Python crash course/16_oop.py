"""
Working with classes follows a simple pattern:

1. Define the class - Create a blueprint with the class keyword
2. Add an __init__ method - Set up initial data when objects are created
3. Create instances - Make actual objects from your class
4. Access the data - Use the attributes you defined

"""

class Cat:
    pass

"""
__init__ looks weird with those double underscores! 
This is called a “dunder” method (double underscore).
It's just how Python works - you'll need to type it exactly like this. 
Don't worry, after writing it a few times it becomes second nature. 
Think of it as Python's special way of saying “this is the setup method”.
"""

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# Create dog objects - using positional arguments
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")

# Or with named arguments (clearer)
dog3 = Dog(name="Charlie", breed="Poodel")

print(dog1.name)
print(dog2.name)
print(dog3.name)

""" What is self?

#self refers to the current object. It’s how an object keeps track of its own data:
#When defining methods in a class, you always include self as the first parameter. 
#But when calling the method, you don’t pass it - Python does that automatically!
"""

"""
Configuration
"""

class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

# Create different configurations
# Using positional for required arg, named for optional
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

# Access the configuration
print(dev_config.model)        # gpt-3.5-turbo
print(prod_config.model)       # gpt-4
print(prod_config.max_tokens)  # 1000

"""
Class vs instance

1. Class: The blueprint (like a recipe)
2. Instance/Object: What you create from the class (like a cake from the recipe)
"""

# APIConfig is the class
# config1 and config2 are instances
config1 = APIConfig(api_key="key1", max_tokens=50)
config2 = APIConfig(api_key="key2", max_tokens=200)

# Each instance has its own data
print(config1.max_tokens)  # 50
print(config2.max_tokens)  # 200

# Changing one doesn't affect the other
config1.max_tokens = 75
print(config1.max_tokens)  # 75
print(config2.max_tokens)  # 200 (unchanged)