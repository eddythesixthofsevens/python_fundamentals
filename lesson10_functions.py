# # functions are blocks of code that can be reused
# # to run a function, you call it by writing its name followed by parentheses and any arguments it needs

# print("Functions (Procedures)")

# print("\nExample 1")

# def say_hi():
#     print("Hi.")

# def say_bye():
#     print("Bye.")

# say_hi()
# say_bye()

# print("\nExample 2")

# def express_this(e): # e is called a parameter, which is a placeholder for an ARGUMENT
#     return e
# expression1 = express_this(1 + 2)   # the mathematical expression is the argument,the actual value that will be used by a function's parameter
# print(expression1)
# expression2 = express_this(45 * 6)
# print(expression2)

# print("\n Example 3")

# def greeter(n): # n is the parameter
#     return f"Hi, {n}. "
# first = greeter("Jojo")
# second = greeter("Bizbo")
# third = greeter ("Hoppy")

# print(first, second, third)

# print("\n Example 4")

# def remainder(a, b):
#     return a % b
# result = remainder(6, 2)
# print("Remainder:", result)

# print("\n Example 5")

# def is_far(distance):
#     # INSERT BASE CASE
#     if distance < 1 or distance > 100:
#         return "Error"
#     elif distance >= 100:
#         return "That's far."
#     elif distance < 100 and distance > 20:
#         return "That's not too far."
#     elif distance <= 20:
#         return "That's nearby."
# print(is_far(20))

# print("\n Example 6")
# # I want to create a function that takes in a number and doubles it, then adds it to a list.
# # The function should also take in a number of times that we should double the number

# def double_sequencer(number, times):
#     value = number
#     sequence = []
#     sequence.append(value)
#     for i in range(times):
#         value = value * 2
#         sequence.append(value)
    
#     return sequence
# result = double_sequencer(1,5)
# print(result)

# Challenge 1
# PROCEDURE add(a, b)
# DISPLAY (a + b)
# PROCEDURE subtract(a, b)
# DISPLAY (a - b)
# PROCEDURE multiply(a, b)
# DISPLAY (a * b)
# PROCEDURE divide(a, b)
# DISPLAY (a / b)

# def add (a, b):
#     print(a + b)
# def subtract (a, b):
#     print(a - b)
# def multiply (a, b):
#     print(a * b)
# def divide (a, b):
#     print(a / b)

# add (10, 2)
# subtract (10, 2)
# multiply (10, 2)
# divide (10, 2)

# Challenge 2
# PROCEDURE average(a, b, c)
# RETURN ((a + b + c) / 3)

# def average (a, b, c):
#     return (a + b + c) / 3
# print(average(1, 1, 1))

# Challenge 3
# PROCEDURE is_even(a)
# IF a MOD 2 = 0
# {
# RETURN ("Even")
# }
# ELSE
#{
#   RETURN ("Odd")
#}

# def is_even (a):
#     if a % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(is_even(3))

# Challenge 4
# Make a function called analyze_word that uses a loop with an IF/THEN statement and works only with strings.
# The function accepts one argument, a single word (string).
# Initialize two variables:
# vowelCount set to 0
# consonantCount set to 0
# Use a loop to iterate through each character in the word.
# Inside the loop, use an IF/ELSE statement:
# If the character is a vowel (a, e, i, o, u), increment vowelCount.
# Otherwise, increment consonantCount.

# After the loop ends, return a string that states how many vowels and how many consonants are in the word.
# # Call the function with a sample one-word string and print the returned result outside the function

def analyze_word(a):
    vowelCount = 0
    consonantCount = 0
    vowels = ["a", "e", "i", "o", "u"]
    for char in range(len(a)):
        if a[char] in vowels:
            vowelCount = vowelCount + 1
        else:
            consonantCount = consonantCount + 1
    return f"Consonant Count: {consonantCount}\
    Vowel Count: {vowelCount}"
print(analyze_word("orca"))