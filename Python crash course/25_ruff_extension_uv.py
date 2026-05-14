"""
ruff = Automatically format and lint your Python code

Ruff is a modern Python tool that's incredibly fast and combines multiple tools in one:

- Linting - Finding issues and potential errors
- Formatting - Fixing code style automatically
- Import sorting - Organizing imports cleanly
- It's beginner-friendly with clear error messages and works seamlessly with VS Code.

Installed?
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Ruff" and install it
4. Open your setting in VS Code
5. Search for "format on save" click tick correct.
6. Search for "default formatter" and select "Ruff"
"""

# what a messy code looks like

from json import tool


def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


shopping_cart = [
    {
        "name": "apple",
        "price": 0.5,
        "quantity": 6,
    },
    {
        "name": "banana",
        "price": 0.3,
        "quantity": 8,
    },
]
print(calculate_total(shopping_cart))

# now command + save = changed!

"""
Ruff automatically:
- Separated imports
- Added proper spacing
- Fixed indentation
- Made quotes consistent
- Formatted the list for readability
"""

# =========================================

# Understanding linting errors
# Ruff will underline code issues in your editor:

# Unused imports (Ruff warns you)
"""
import os
import sys
"""
# Only using one
print("Hello")

# CMD + Shift + P -> "Ruff: fixed all auto-fixable problems" to fix all issues at once.

"""
Add this on pyproject.toml

[tool.ruff]
# setting for "Python 3.12" based on your project
target-version = "py312"

[tool.ruff.lint]
# pick the rules such as, E (Error), F (Pyflakes), I (isort)
select = ["E", "F", "I"]
"""

#  =========================================
#  =========================================
#  =========================================

"""
Modern Python: UV Python package manager are the game changers!

It's faster, harder, better, wilders!

Install:
Mac = curl -LsSf https://astral.sh/uv/install.sh | sh
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
"""

# Quick Commands
"""
1. Create new project
uv init my-project

2. Add packages
uv add requests pandas

3. Install from existing project
uv sync

4. Run Python
uv run python script.py

5. Remove packages
uv remove package-name

6. Update packages
uv add --upgrade package-name

7. Check what version of python you had
uv python list --only-installed

8. Update packages
uv add --upgrade package-name

9. Install from requirements.txt
uv pip install -r requirements.txt

10. Python version installations
uv python install 3.12
uv python install 3.11
"""

# Understand pyproject.toml

"""
This is your project's configuration file:

[project]
name = "ai-assistant"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "requests>=2.32.0",
    "pandas>=2.2.0",
    "numpy>=1.26.0",
    "matplotlib>=3.8.0",
]

[tool.uv]
dev-dependencies = [
    "pytest>=8.0.0",
    "black>=24.0.0",
]
"""
