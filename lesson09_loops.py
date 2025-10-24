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

for i in range(6):
    print("counting:", i)

for num in range(2, 11, 2):
    print("count by two: ", num)