# Set variables
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

# Print string x and string y
print(x)
print(y)

# Repeat string print
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Set hilarious to False, evaluate joke
hilarious = True
joke_evaluation = "Isnt that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

# Set variables w, e
w = "This is the left side of..."
e = "a string with a right side."

# Print string combination
print(w+e)
