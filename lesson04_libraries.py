# LIBRARIES
# Libraries are kind of like repositories of code that you can import into your files to make code.

# Abstractions are commands with a ton of code behind them that we do not see; we simply run the command.

# MATH LIBRARY

import math
print("\n--- Math Library ---\n")

print("Square root: ", math.sqrt(25))
print("Round up to an integer:", math.ceil(3.14))
print("Round down to an integer:", math.floor(6.7))
print("Power:", math.pow(2, 5))
print("Pi",math.pi)

# RANDOM LIBRARY

import random
luckynum = 1

lucky = random.randint(1, 10) # makes a random number from 1 - 10

print(lucky)

if(lucky == 1)
print()