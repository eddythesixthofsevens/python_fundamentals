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
import random
day = random.choice(["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"])
if day == "saturday" or day == "sunday":
    print("It's the weekend!")
elif day is "monday":
    print("Suffering begins.")
else:
    print("Your suffering shall continue.")

if day is not "monday":
    print("THE SUFFERING IS REDUCED!")

# can use is in place of ==