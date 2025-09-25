# CONCEPTS VARIABLES
# variable - holds a value
# stored in physical storage of your device

taco = "hello world"

password = "r3@l3st@t3!"
email = "homesforlife@gmail.com"
print("Email:", email)
print("Password:", password)

temperature = 72.5
print(type(temperature))
price = 3.99

enabled = False
is_complete = True
print(is_complete)

#Variables can be overwritten
enabled = True
print(enabled)

# When writing variables, variable name must be meaningful so others can understand them more easily.

# For math problems:
x = 3.14
y = 7
print(x + y)

# Variables are flexible. You create or update another variable like so:
count = 10
print(count)
count_down = count - 1
print(count_down)
count = count_down
count_down = count - 1
print(count_down)

# Challenge 1: Rename Variables
# Change the variable names x, y, and z below to more descriptive names.

being = "Radia Perlman"
age = 34
Job = "Networking Engineer"

# Challenge 2: Update Variables
# Create a variable called 'count' with a value of 10.
# Increase it by 5 and print the result.
# Use two variables total.

count2 = 10
print(count2)
count_up = count2 + 5
print(count_up)

#Challenge 3: Swap Variables
# Given variables x = 4 and y = "hello".
# Swap the variable values. Use a temporary variable.

x = 4
y = "hello"
temp = y
y = x
x = temp
print(x, y)

#Challenge 4: Boolean Practice
# Create a variable named 'is_raining'. Set it to False.
# On the next line, update it to True.
# Print "Is it raining?" followed by the boolean.

is_raining = False
is_raining = True
print("Is it raining?", is_raining)