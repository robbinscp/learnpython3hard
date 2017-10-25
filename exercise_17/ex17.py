# Import required python modules
from sys import argv
from os.path import exists

# Set variables from arguments passed to script
script, from_file, to_file = argv

# Perform copy work
print(f"Copying from {from_file} to {to_file}")
in_file = open(from_file).read()
out_file = open(to_file, 'w')
out_file.write(in_file)

# Let user know file copy has completed, close the output file
print("File copy completed.")
out_file.close()
