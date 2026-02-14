# Args Parsing
# ex. python3 my_script.py -o result.txt -l DEBUG

import sys
import getopt
import argparse

file_name = "test.txt"
message = "Hello, World"

def my_function(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])

    print(kwargs['KEYONE'])
    print(kwargs['KEYTWO'])

my_function('Hey', True, 19, 'WOW', KEYONE="TEST", KEYTWO="7")
print()

print(sys.argv) # address the individual argument and elements
print()

# Usage: main.py FILENAME \ -p 8080 localhost

opts, args = getopt.getopt(sys.argv[1:], "f:m", ['file_name=', 'message='])

for opt, arg in opts:

    if opt in ('-f', '--file_name'):
        file_name = arg

    if opt in ('-m', '--message'):
        message = arg

with open(file_name, 'w+') as f:
    f.write(message)

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file_name", help="file name", default="test.txt")
parser.add_argument("-m", "--message", help="message", default="Hello, World")
args = parser.parse_args()

print(f"writing file on: {args.file_name}")