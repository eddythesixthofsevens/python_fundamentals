# Basic string creation and indexes
greeting = "hello"
name = "ada"

# 0 1 2 3 4
# H e l l o

message = greeting + " " + name + "!!!"

print("Concatenated message: ", message)
print()
print(greeting[1])
print()
word = "super - cali - fragil - istic - expi - ali - docious"
print("First letter of word: ", word[0])
print("Last letter of word: ", word[-1])
print("range of letters (non inclusive): ", word[0:6])