# Function definition for cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print("Get a blanket.\n")

# First use of cheese_and_crackers (provide numbers directly)
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Second use of cheese_and_crackers (with variables)
print("OR, we can use variables from our script.")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Third use of cheese_and_crackers (with math performed)
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Fourth and final use of cheese_and_crackers (variables + math)
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
