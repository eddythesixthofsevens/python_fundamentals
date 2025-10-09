# # Basic string creation and indexes
# greeting = "hello"
# name = "ada"

#  0 1 2 3 4
#  H e l l o

# message = greeting + " " + name + "!!!"

# print("Concatenated message: ", message)
# print()
# print(greeting[1])
# print()
# word = "super - cali - fragil - istic - expi - ali - docious"
# print("First letter of word: ", word[0])
# print()
# print("Last letter of word: ", word[-1]) # print()
# print("range of letters (non inclusive): ", word[0:6])
# print()
# print("another range of letters: ", word[6:12])
# print()
# print(word[:5])
# print()
# print("Last seven letters: ", word[-7:])
# print()
# print("step through every second letter of the big word: ", word[::-2])
# print()
# print("reverse word: ", word[::-1])
# print()
# print("weird word: ", word[::-3])

# built in functions

# country = "egypt"
# length_of_word = len(country)
# print(length_of_word)

# sponge = "SpOnGEbOB SqUaREpaNts"
# print("\nUppercase: ", sponge.upper())
# print("\nLowercase: ", sponge.lower())
# print("\nCapitalized: ", sponge.capitalize())
# print("Title Format: ", sponge.title())

# #Find and replace text
# sentence = "I'm a goofy goober"
# new_sentence = sentence.replace("I'm", "You're")
# next_replacement = sentence.replace("goofy", "goober")
# print(sentence)
# print(new_sentence)
# print(next_replacement)

# # FORMATTED STRINGS IN PYTHON
# # f-strings allow variables and expressions inside strings

# print("\n--- Formatted Strings ---")

# name = "Adam"
# age = 400
# city = "Valhalla"

# print(f"Hello, my name is {name}. I am {age} years old and live in {city}.")

# f-strings can do math and function calls inside {}

# print(f"Next year, I'll be {age + 1}. My name in uppercase is {name.upper()}.")

# print()
# print()
# print()

# Challenge 1: Favorite Quote
# Ask the user for their favorite quote and display its length.
# EXAMPLE OUTPUT:
# Enter your favorite quote: Those who believe in telekinetics, raise my hand.
# Your quote is 48 characters long.

# quote = input("Gimme your favorite quote ")
# length_of_quote = len(quote)
# print(f"Your quote is {length_of_quote} characters long")



# # Challenge 2: Name Formatter
# # Ask the user for their first and last name, then format it as "Last, First".
# # Use concatenation or f strings.
# # Example output:
# # Enter your first name: Ada
# # Enter your last name: Lovelace
# # Output formatted name: Lovelace, Ada

# print(f"{input("Enter your last name: ")}," + f" {input("Enter your first name: ")}")

# first = input("First?") 
# last = input("Last?")
# print(last + ", " + first)

# Challenge 3: Word Mutation
# Ask for a word and print it backwards, in uppercase, and lowercase.
# Example output
# Enter a word: Python
# Backwards: nohtyP
# Uppercase: PYTHON
# Lowercase: python

# word = input("Enter a word: ")
# print("Backwards: ", word[::-1])
# print("Uppercase: ", word.upper())
# print("Lowercase: ", word.lower())