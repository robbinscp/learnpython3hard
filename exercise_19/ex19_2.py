# Function definition for sandwiches and chips
def sandwiches_and_chips(num_sandwiches, num_chips):
    print(f"We have {num_sandwiches} sandwiches") 
    print(f"We have {num_chips} bags of chips")
    meals = num_sandwiches % num_chips
    # This logic still needs some work :-/
    if (meals == 0):
       print(f"This means we have {num_sandwiches} meals available.")
    if (num_sandwiches % num_chips) != 0:
       print("We don't have enough for everyone! :-(\n")
    else: 
       print("Yay, there are enough sandwiches and chips for everyone!\n")

# First run - common case
sandwiches_and_chips(10 , 10) 

# Second run - math
sandwiches_and_chips(11 + 3 , 6)

# Third run - convert to int?
sandwiches_and_chips(int(10) , int(10)) 

# Fourth run - int plus math
sandwiches_and_chips(int(10)+10,  int(10)+10)

# Fifth run - floats?
sandwiches_and_chips(float(100), float(1000))
