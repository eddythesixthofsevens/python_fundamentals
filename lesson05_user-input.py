# USER INPUT IN PYTHON

# print("\n--- User Input Demonstration ---")

# name = input("Enter your name: ")
# print(name)
# print("Hello,", name)
# # default data type for input() is a string, even if you don't type it as such.

# age = int(input("Enter your age: "))
# print(type(age))

# age_number = int(age)
# print("Next year, you will be: ", age_number + 1)

# # Example with a float input.

# height = float(input("Enter your height in meters: "))
# print("You are ", height, "meters tall.")

# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.

# q = input("What's your favorite color?")
# print("That's cool!", q, "is my favorite too!")

# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.

# num = int(input("Enter one number: "))
# num2 = int(input("Enter another number: "))
# print(num + num2)

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.

# import math

# d = int(input("Input the diameter of a circle: "))
# print(math.pi * (d / 2) ** 2)

# Challenge 4: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.

import random

die = int(input("Input side amount: "))
print(random.randint(1, die))