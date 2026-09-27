# Shawn Peterkin
# 9/24/2023
# P1HW1.py
# Calculating exponents

print()
print("Welcome to the 2-Trick Pony Calculator!")
print()
print("----- Calculating Exponents -----")
print()

base = int(input("Enter the base number: "))
exponent = int(input("Enter an exponent: "))
result = base ** exponent
print(base, "raised to the power of", exponent, "is", result, "!!")
print()
# calculating addition and subtraction

print("----- Addition and Subtraction -----")
print()

num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))

sum_result = num1 + num2
final_result = sum_result - num3

print(num1, "+", num2, "-", num3, "=", final_result)