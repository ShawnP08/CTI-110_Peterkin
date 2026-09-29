# Shawn Peterkin
# 9/24/2023
# P1HW2.py
# Calculating math based on given values

print()
print("Travel Expenses Budget Tracker!")
print()
print("----- Calculating Travel Expenses -----")
print()

# Getting user input for budget, travel destination, and other information to use for the calculations
budget = int(input("Enter Budget: "))
print()
location = input("Enter Travel Destination: ")
print()
num1 = int(input("How much do you think you will spend on gas?: "))
print()
num2 = int(input("Approximately, How much do you think you will spend on accommodation/hotel?: "))
print()
num3 = int(input("Lastly, How much will you need for food?: "))

# Breaks off and shows the user the information they inputted and the remaining budget after all expenses
print()
print("----- Travel Expenses -----")
print()

print("Location:", location)
print("Initial Budget:", budget)
print()

print("Gas Expenses:", num1)
print("Accommodation/Hotel Expenses:", num2)
print("Food Expenses:", num3)

# Final calculation to show the user how much money they have left after all expenses
Remaining_Budget = budget - (num1 + num2 + num3)
print()
print("Remaining Budget:", Remaining_Budget)

# I think so far out of the assignments I had the most fun on this one
# being able to kinda figure out the correct code for the prompt was fun
# and changing the code to fit how I would want it to look was fun aswell!