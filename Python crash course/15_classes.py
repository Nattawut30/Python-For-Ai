"""
Create your own data types

What is object-oriented programming?

Object-oriented programming (OOP) is a way to organize code by grouping related data and functions together.
Instead of having separate variables and functions scattered around, you bundle them into objects.
Think of it like organizing a toolbox:

1. Without OOP: Tools scattered everywhere
2. With OOP: Tools organized in labeled compartments

What is a class?

A class is a blueprint for creating objects. It defines:
1. Attributes: What data the object stores
2. Methods: What the object can do

"""

# Without Classes - data and functions separate
name = "OpenAI"
model = "gpt-5-mini"

def generate_response(prompt):
    # Process prompt...
    return response

response = generate_response
print(response)

# With classes - everything bundled together
class OpenAIClient:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def generate_response(self, prompt):
        # Process prompt
        return response
    
response = generate_response
print(response)

"""
Classes help you write more understandable programs as they grow.
Here's the typical progression of a Python developer:

"""

