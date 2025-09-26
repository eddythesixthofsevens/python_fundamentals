# KEY CONCEPTS: math operators: +, -, *, /, //, %, **

add = 35 + 32
print("Sum:", add)

subtract = 100 - 33
print("Difference:", subtract)

multiply = 33.5 * 2
print("Product:", multiply)

float_divide = 7 / 2
print("Float Division: ", float_divide)

# floor division (integer division) always rounds down to the closest integer (//).
integer_divide = 7 // 2
print("Integer Division", integer_divide)

# modulus: asking only for the remainder of a division (%)
modulus = 7 % 2
print("Modulus:", modulus)

exponent = 7 ** 3
print("Exponent:", exponent)

# Example of boolean with math operators
print(2 + 2 == 10 - 6) 

# python follows the order of operations (PEMDAS)
result1 = (2 + 3) * 4
print("Result 1:", result1)

result2 = 2 ** 3 * 4
print("Result 2:", result2)

result3 = 20 / 5 * 2
print("Result 3:", result3)

result4 = 10 - 2 + 3
print("Result 4:", result4)

result5 = 5 + 2 ** 3 * (4 - 1)
print("Result 5:", result5)

# general math note: multiplication, division, addition, and subtraction work left to right in PEMDAS

# CHALLENGES

#  Challenge 1: Rectangle Area
# Calculate the area of a rectangle with a width of 8 and a height of 5.

print("A =", 8 * 5)

# Challenge 2: Circle Area
# Use the formula (pi)r^2 to calculate the area of a circle with radius of 7.
# (Use 3.14 for pi.)

print("A =", 3.14 * 7 ** 2)

# Challenge 3: Shopping Total
# A book costs $12.99 and a notebook costs $3.50.
# Calculate the total cost for 3 books and 4 notebooks.

book = 12.99
notebook = 3.50

print("Cost =", book * 3 + notebook * 4)

# Challenge 4: Even or Odd
# Create a variable that holds any integer.
# Use the modulus operator to check if the number is even or odd.
# Explain your reasoning.

value = 14
print(value % 2 == 0)
# Set a value to the variable, the next line checks if that number is divisible by two, and therefore checks if it is even.