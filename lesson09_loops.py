# # LOOPS IN PYTHON
# # Loops repeat a block of code until they hit a limit or condition.
# # They exist to save us from typing the same line 500 times.
# # Python gives us for-loops and while-loops.

# print()
# print("--- Loops in Python ---")

# # The for-loop.
# # A for-loop repeats for each element in a sequence (like a list or string).
# import time

# animals = ["turkey", "horse", "clownfish", "rabbit", "duck", "camel"]
# animals[0]

# print("\n Our animals:", animals)
# print("\n--- For Loop: visiting each animal ---")

# for animal in animals:
#     print(f"Now petting a {animal}")
#     if animal == "rabbit":
#         print("It's the rat!")
#     time.sleep(1.5)
    
# print("Now I've given all the animals adequate physical affection!")

# for i in range(6):
#     print("counting:", i)

# # range(start, stop, step)
# for num in range(2, 11, 2):
#     print("count by two: ", num)

# print(range(10))

# print("--- Iterating over strings ---\n")

# fav_word = "fisch"
# letter_list = []
# for letter in fav_word:
#     print(letter, end="")
#     letter_list.append(letter)
#     print(letter_list)
#     print()

# ---------------------------------------------------------
# WHILE LOOPS
# ---------------------------------------------------------
# WORK WITH CONDITIONALS, BASED ON TRUE/FALSE (BOOLEAN)

# A while-loop repeats *while* a condition is true.
# If you forget to change the condition, it loops forever.
# And then your program becomes immortal. Avoid that.

# += to add to a variable, -= to subtract to a variable, = to overright 
import time
count = 0
# while count < 6:
#     print(f"Loopin'. We are on loop #{count}.")
#     count += 1
#     time.sleep(0.5)

# print("We have escaped the loop!")


# user_input = ""
# input("Type 'exit' to escape:")
# while user_input != "exit":
#    user_input = input("Type 'exit' to escape:")

# count = 60
# increment = 1

# while count > 0:
#     count -= increment
#     increment += 1
#     if count < 0:
#         break
#     print(count)