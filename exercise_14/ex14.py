# Python import statements
from sys import argv

# Store variables from argv, set prompt display
script, user_name, date = argv
prompt = '->  '

# Print initial text
print(f"Hi, {user_name}, I am the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")

# Store input into likes variable
likes = input(prompt)

# Query for user location, store in lives variable
print(f"Where do you live {user_name}")
lives = input(prompt)

# Ask for user computer, store in comptuer variable
print(f"What kind of computer do you have?")
computer = input(prompt)

# Print data gathered
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.  Not sure where that is.
And you have a {computer} computer.  Nice.  
You said today was {date}
""")
