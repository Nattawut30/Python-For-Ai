"""
Git & GitHub
= Version control basics

What is Git?:

= Git is like a save system for your code. 
It tracks every change you make, lets you go back to previous versions, 
and helps you collaborate with others.

= GitHub is where you store your Git projects online
think of it as Google Drive for code.

Why you need Git:

As an AI engineer, you'll use Git to:
1. Save your progress: Never lose code again
2. Try experiments: Test ideas without breaking working code
3. Share projects: Show your work to employers or collaborators
4. Use AI tools: Many AI projects are shared on GitHub

How Git works:

Think of Git as taking snapshots of your code:
1. You write code - Make changes to your files
2. You save a snapshot - Called a “commit” in Git
3. Git remembers everything - Every snapshot, who made it, when, and why
"""

# Monday: Your code works
def calculate_price(amount):
    return amount * 1.20  # 20% markup

# Tuesday: Boss wants 25% markup
def calculate_price(amount):
    return amount * 1.25  # Changed from 20% to 25%

# Wednesday: "Actually, can we go back to 20%?"
# With Git: Easy! Just go back to Monday's version
# Without Git: Hope you still have that file somewhere...

"""
Key concepts (Essentials)

1. Repository (repo): A project tracked by Git
Your python-for-ai folder can be a repository

2. Staging: Choosing which changes to save
Like selecting items to put in a box before shipping

3. Commit: A saved snapshot of your code
Like saving in a video game - you can always go back

4. Push: Upload your commits to GitHub
Backs up your code online

5. Pull: Download changes from GitHub
Get updates when working with others

6. Clone: Copy a project from GitHub
How you get AI projects to try
"""

# STEP 0: Example Work flow
# First time only - initialize Git in your project
""" git init """

# Save your changes locally
""" git add .
git commit -m "Add price calculation function" """

# Upload to GitHub (after connecting to GitHub - see next pages)
""" git push """

# That's it! Your code is saved and backed up

# STEP 1: Check if you have Git:
"""
git --version
"""

# STEP 2: Download
""" https://git-scm.com/downloads/mac """

# STEP 3: Sign Up, Verify, and Set up profile
""" https://github.com/ """

# STEP 4: Configure Git locally
"""
Open terminal in VS Code (Terminal > New Terminal)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
"""

# STEP 5: Anthetication Method
"""
Install GitHub CLI:
Windows: Download from cli.github.com
macOS: brew install gh
Linux: See installation guide

Authenticate:
Terminal > gh auth login

Follow the prompts:
1. Choose GitHub.com
2. Choose SSH (recommended) or HTTPS
3. Authenticate with browser

That's it! Git will automatically use your gh credentials.
"""

# ==========================================================

# Clone and Create = Working with repositories
""" 
Clone: Download existing projects from GitHub to your local computer
Create: Start new projects and upload them

If you don't like using 'cd' navigate...
Mac: Right-click a folder in Finder > Services > New Terminal at Folder (or hold Option and right-click > “Open in Terminal”)
Windows: Right-click a folder in File Explorer > “Open in Terminal” (or Shift + right-click > “Open PowerShell window here”)

This opens the terminal already in that folder!
"""

# Clone some Project on your local
"""
1. Open Terminal (Mac) or Command Prompt (Windows)
2. Navigate to where you want the project

cd ~/Documents  # Mac
cd C:\Users\YourName\Documents  # Windows

3. Clone using HTTPS URL (Recommended)
git clone https://github.com/openai/openai-quickstart-python.git

4. Go into the project
cd openai-quickstart-python

5. Open in VS code (fast way)
code .

5.1 If 'code .' doesn't work, you need to enable it first:

Mac:
Open VS Code
Press Cmd + Shift + P
Type “Shell Command: Install 'code' command in PATH”
Press Enter
Restart your terminal

Windows:
During VS Code installation, check “Add to PATH”
If you missed it, reinstall VS Code and check that option
Or manually: Right-click project folder > “Open with Code”
"""


# The .gitignore filre (Important!)
"""
.gitignore = tells Git what NOT to track

.venv/
.env
__pycache__/
*.pyc
.DS_Store
"""