# # LISTS IN PYTHON
# # Lists store multiple values in one variable.
# # They are ordered, mutable (changeable), and allow duplicates.
# # A collection of elements
# print()
# print("--- Lists in Python ---")
# animals = ["monkey", "puffer", "chicken"]
# numbers = [1, 2, 3, 4, 5]
# mixed = [6, "fifty", True, 6.7]
# empty_list = []
# print(animals)
# print(numbers)
# print(mixed)
# print("First element of animal list: ", animals[0])
# print("Second element of animal list: ", animals[1])
# print("Last element of animal list: ", animals[-1])
# print()
# print("--- Modifying Lists ---")
# animals[0] = "proboscis monkey"
# print(animals)

# # add element at the end
# empty_list.append("gojo")
# animals.append("zyzzyva")
# print(animals)
# print(empty_list)

# # replace elements by = the index to another thing
# animals[0] = "big monke"
# # or...
# animal_to_replace = animals.index("chicken")
# print(animal_to_replace)
# animals[animal_to_replace] = "donkey"

# # insert element at specific index
# animals.insert(3, "horse")
# animals.insert(5, "camel")
# print("Inserted two animals: ", animals)

# # remove elements
# animals.remove("zyzzyva")
# print("Removed one animal: ", animals)

# # take off last element and store in variable
# last_animal = animals.pop()
# print("Best animal: ", last_animal)
# print("Animal list: ", animals)

# print()
# print("--- Useful List Functions ---")

# nums = [6, 8, 7, 9, 4, 1, 5]
# print("Original numbers: ", nums)
# print("List length: ", len(nums))
# print("Min: ", min(nums))
# print("Max: ", max(nums))
# print("Sum: ", sum(nums))

# nums.sort()
# print(nums)
# animals.sort()
# print(animals)
# # lists are MUTABLE (they can mutate/change, sorta like mutants)

# nums.reverse()
# print(nums)

# print()
# print("--- Checking Membership ---")

# if "big monke" in animals:
#     print("Monke is in the list.")
# else:
#     print("Monke is not in the list.")

# print()
# print("--- Copying Lists ---")
# original_list = [1, 2, 3]
# print(original_list)
# copied_list = original_list.copy()
# copied_list.append(4)
# print(copied_list)

# print()
# print("--- Nested Lists/The Matrix ---")
# matrix = [   
#     [1, 2, 3], 
#     [4, 5, 6], 
#     [7, 8, 9]   ]

# print(matrix[2][2])

### **Challenge 1: Integer Swap**

# Store this list in a variable: [ 1, 2, 3, 4, 5, 6 ] 
# Ask the user to enter a new integer.
# Replace the **third integer** in the original list with the user’s input, and then print the updated list.
# *Hint: use indexing and assignment.*

# nums = [1, 2, 3, 4, 5, 6]
# print(nums)
# replace_num = int(input("Enter a number: "))
# nums[2] = replace_num
# print(nums)

### **Challenge 2: Shopping List Manager**

# Initialize an empty list called `shopping`.
# Add three items of your choice using `.append()`.
# Then insert one extra item at the second position 
# Remove one item of your choice.
# Finally, print the final shopping list.

shopping = []
shopping.append("radioactive waste")
print(shopping)
shopping.append("uranium")
print(shopping)
shopping.append("land mines")
print(shopping)