# Python library imports
from sys import argv

# Store script, input_file information from argv
script, input_file = argv

# Define fuctions
# print_all function
def print_all(f):
    print(f.read())

# rewind function
def rewind(f):
    f.seek(0)

# print_a_line function
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open input_file, store in current_file
current_file = open(input_file)


print("First let's print the whole file:\n")

# Call print_all to print input_file (stored in current_file)
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Rewind back to the start of current_file
rewind(current_file)

print("Let's print three lines:")

# Set current_line
current_line = 0

# Print current_line from the current_file
# Refactored using += operator
current_line += 1
print(current_line)
print_a_line(current_line, current_file)

current_line += 1
print(current_line)
print_a_line(current_line, current_file)

current_line += 1
print(current_line)
print_a_line(current_line, current_file)

