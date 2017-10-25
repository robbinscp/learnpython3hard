# Python module import
from sys import argv

# Store script name, filename from argv
script, filename = argv

# Open file specified in previous step
txt = open(filename)

# Print the filename using txt.read() function
print(f"Here's your file {filename}")
print(txt.read())
txt.close()

# Request the file from the user
print("Type the filename again")
file_again = input("> ")

# Open the file specified by the user, and print it out
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
