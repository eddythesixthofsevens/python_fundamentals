# LISTS IN PYTHON
# Lists store multiple values in one variable.
# They are ordered, mutable (changeable), and allow duplicates.
# A collection of elements
print()
print("--- Lists in Python ---")
animals = ["monkey", "puffer", "chicken"]
numbers = [1, 2, 3, 4, 5]
mixed = [6, "fifty", True, 6.7]
print(animals)
print(numbers)
print(mixed)
print("First element of animal list: ", animals[0])
print("Second element of animal list: ", animals[1])
print("Last element of animal list: ", animals[-1])
print()
print("--- Modifying Lists ---")
animals[0] = "proboscis monkey"
print(animals)

# add element at the end
animals.append("zyzzyva")
print(animals)

# insert element at specific index
animals.insert(3, "horse")
animals.insert(5, "camel")
print("Inserted two animals: ", animals)

# remove elements
animals.remove("zyzzyva")
print("Removed one animal: ", animals)

# take off last element and store in variable
last_animal = animals.pop()
print("Best animal: ", last_animal)
print("Animal list: ", animals)

print()
print("--- Useful List Functions ---")