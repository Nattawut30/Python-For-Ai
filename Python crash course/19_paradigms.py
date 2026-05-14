"""
Best practices and guidelines
Python supports multiple programming styles. 
"""

# Functional Programming - Using functions to transform data:

# Functions operate on data
def clean_text(text):
    return text.strip().lower()

def remove_punctuation(text):
    return text.replace(".", "").replace(",", "")

# Chain functions together
result = remove_punctuation(clean_text("  Hello, World.  "))

# ===============================

# Object-oriented programming - Using classes to bundle data and behavior

# Class bundles data and methods
class TextProcessor:
    def __init__(self, text):
        self.text = text
    
    def clean(self):
        self.text = self.text.strip().lower()
        return self
    
    def remove_punctuation(self):
        self.text = self.text.replace(".", "").replace(",", "")
        return self

# Chain methods on object
processor = TextProcessor(text="  Hello, World.  ")
result = processor.clean().remove_punctuation().text