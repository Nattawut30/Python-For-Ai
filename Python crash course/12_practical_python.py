"""
Build real programs with proper structure

You've learned the building blocks. Now let's put them together into organized, maintainable programs.
In this section, you'll learn how real Python projects are structured and how to work with files, organize your code, and build programs
that actually do useful things.

Throughout this section, you'll build a sales analysis project step by step:

1. Set up a project - Create organized folder structure
2. Understand paths - Learn how Python finds your files
3. Work with data - Read CSV files and save as JSON
4. Organize code - Split code into reusable functions

By the end, you'll have a complete data analysis program and understand how real Python projects work.

"""

"""
1. Create the data files 

python-for-ai/
├── hello.py              # Your existing practice file
└── sales-analysis/       # New project folder
    ├── data/             # CSV files and data
    └── output/           # Generated files

"""

"""
2. When your script runs from sales-analysis folder
"data/sales.csv"           # Look in the data subfolder
"output/report.json"       # Save to the output subfolder

# Your project structure
# python-for-ai/
#   └── sales-analysis/
#       ├── analyzer.py      <- Your script is here
#       ├── data/sales.csv   <- Your data is here
#       └── output/          <- Results go here

"""

"""
3. The simple rule

import os

# See where Python is right now
print(os.getcwd())

"""

# Check out the files analyzer.py to understand more