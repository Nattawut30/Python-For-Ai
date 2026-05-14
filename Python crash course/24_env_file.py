"""
A .env file is a simple text file that stores your environment variables.
Instead of typing export commands, you write them once in a file.
"""

# Load in Python
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Now use your variables
api_key = os.environ.get('API_KEY')
debug = os.environ.get('DEBUG')

print(f"API Key: {api_key}")
print(f"Debug mode: {debug}")

# ===============================================

# Real-Word Example

# app.py
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.environ.get('OPENAI_API_KEY')

if not API_KEY:
    print("Please set OPENAI_API_KEY in .env file")
    exit(1)

# Use the API
headers = {"Authorization": f"Bearer {API_KEY}"}
# Make your API calls...

"""
Never commit .env files! They contain secrets. Add to .gitignore immediately
Never commit .env files! They contain secrets. Add to .gitignore immediately
Never commit .env files! They contain secrets. Add to .gitignore immediately
"""