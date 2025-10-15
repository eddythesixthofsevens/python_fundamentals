# # CONDITIONALS IN PYTHON
# # comparison operators: ==, !=, <, >, <=, >=
# # logical operators: and, or, not
# # control flow: if, elif, else

# # BOOLEAN LOGIC = True or False

# print("\n --- Conditionals in Python ---\n")
# print(3 == 2)
# print("Hello" == "Hi there")
# print(7 != 4)
# print(4 > 5)

# # if
# num1 = float(input("Enter a number:"))
# num2 = float(input("Enter another number:"))

# if num1 == num2:
#     print(f"{num} is equal to {num2}.")
# else:
#     print(f"{num} is not equal to {num2}.")

# num1 = 12
# num2 = 13
# print(num2 <= 12)
# if num2 <= 12:
#     print("Your number is less than or equal to 12")
# else: 
#     print("Your number is greater than 12")

# if, elif, else

# temperature = 60
# if temperature > 80:
#     print("It's hot!")
# elif temperature >= 60:
#     print("It's nice.")
# else:
#     print("It's cold!")

# x = 2
# y = 20
# if x == y:
#     print("x is equal to y.")
# elif x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is six and seven of y")

# age = 16
# has_permission = True

# if age >= 17 and has_permission:
#     print("You can drive.")
# # If even one is false, the whole thing will return as false.
# else:
#     print("Driving is not permitted as of now.")
# using 'or' and 'not'
# import random
# day = random.choice(["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"])
# if day == "saturday" or day == "sunday":
#     print("It's the weekend!")
# elif day is "monday":
#     print("Suffering begins.")
# else:
#     print("Your suffering shall continue.")

# if day is not "monday":
#     print("THE SUFFERING IS REDUCED!")

# can use is in place of ==

# Challenge 1: Even or Odd
# Ask the user for a number, and tell them if it’s even or odd.
# Example output:
# Enter a number: 7
# 7 is odd.
# Hint: use modulus operator

# number = int(input("Enter a number: "))
# even_or_odd = number % 2
# if even_or_odd == 1:
#     print("Your number is odd.")
# else:
#     print("Your number is even.")

# Challenge 2: Password Check
# Create a variable with a stored password
# Ask the user to enter a password. 
# If it matches the stored password, print "Access granted." Otherwise, "Access denied."
# Example output:
# Enter password: dolphin
# Access granted. Access denied.
# Enter password: swordfish
# Access granted.

# password = "pyramids!"
# insert_pass = input("Enter a password: ")
# if password == insert_pass:
#     print("Access granted.")
# else:
#     print("Access denied.")

# Challenge 3: Grading System
# Ask the user for a numeric grade (0-100) and print a letter grade.
# Example output:
# Enter your grade: 94
# You earned an A.

grade = int(input("Enter a grade (1-100): "))
if grade >= 90:
    print("A")
elif grade >= 80 and grade < 90:
    print("B")
elif grade >= 70 and grade < 80:
    print("C")
else:
    print("F")