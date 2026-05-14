""" 
Python packages add new functionality to your programs. 
There are two types:
Built-in: Come with Python (no installation needed)
External: Need to install first with pip

"""

# Since 2025 up untill now
# We use uv python packages manager to install libraries
# We will cover it later

# Pattern 1: Import the whole module
import math
math.sqrt(16)

# Pattern 2: Import specific items from a module
from math import sqrt, pi
sqrt(16)

import random

# Entire module
number = random.randint(1, 10)
print(number)

# Module functions
choice = random.choice(["apple", "banana", "orange"])
print(choice)

# Date and time
import datetime
today = datetime.date.today()
print(today)  # 2024-01-15

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)

import pandas as pd
import numpy as np
