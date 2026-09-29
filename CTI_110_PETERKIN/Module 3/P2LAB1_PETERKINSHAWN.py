# Shawn Peterkin
# P2LAB1
# 9/29/2026
# the program will calculate the diameter, circumference, and area of a circle.

# to be able to use math.pi
import math

print()
print("----- Circle Calculator -----")

print()
# float for the radius to allow for decimal values
radius = float(input("What is the radius of the circle: "))
print()

# variables to calculate the diameter, circumference, and area of a circle using the radius provided by the user
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius**2

#output
print()
print(f"The diameter of the circle is: {diameter:.1f}\n")
print()

print(f"The circumference of the circle is: {circumference:.2f}\n")
print()

print(f"The area of the circle is: {area:.3f}\n")
print()