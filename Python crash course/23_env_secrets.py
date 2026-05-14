"""
Always keep your API keys safe

Never put secrets in your code!
when working with APIs or databases, you'll need:

- API keys
- Passwords
- Connection Strings
Putting these directly in your code is dangerous - anyone can see em!

Solutions?
= Environment variables let you keep secrets separate from your code.

(Most Python projects use .env files - they're simple and work great for local development)
"""

# Environment Variables
"""
Environment variables are settings stored outside your code. 
Think of them as configuration that your program can read.
"""

# BAD: never hardcode sensitive data!
api_key = "sk-1234567890abcdef"  # Everyone can see this!
database = "production_database"  # Can't change without editing code
# Problems:
# - Secrets visible in code
# - Can’t share code safely
# - Different settings for different computers

# ============================================

"""
How environment variables work?
Environment variables live in your system, not your code:
"""

import os

# Read from environment
api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE_NAME', 'default.db')

print(f"Using database: {database}")

# ============================================

# Setting environment variables
# You can set them temporarily in your terminal:
"""
1. Mac/Linux
export API_KEY=sk-1234567890abcdef
python app.py

2. Windows
set API_KEY=sk-1234567890abcdef
python app.py

But they disappear when you close the terminal.
"""

# ============================================

# Reading in Python 

import os

# Method 1: Get with default
api_key = os.environ.get('API_KEY', 'demo-key')

# Method 2: Check if exists
if 'API_KEY' in os.environ:
    api_key = os.environ['API_KEY']
else:
    print("No API key found")

# Method 3: Will crash if not found
api_key = os.environ['API_KEY']  # KeyError if missing!

"""
Common uses:

1. API Keys: OPENAI_API_KEY, GITHUB_TOKEN
2. Database URLs: DATABASE_URL, REDIS_URL
3. App Settings: DEBUG=True, PORT=8000
4. File Paths: LOG_DIR, UPLOAD_FOLDER
"""