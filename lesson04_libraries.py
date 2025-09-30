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
print("\n--- Random Library ---\n")

# Because computers can't generate random numbers, random library is a pseudorandom number generator (not truly random). 
# It uses a complicated algorithm that creates the appearance of randomness.
# True random would be like rolling a die.
# Pseudorandom generators need a person to create a random number (the date, for example, called a seed) and divide it
# by something (the time), then multiply it by something else (amount of days in the month), and subtract it by
# something (the amount of days in the year).
# Every time you use the same seed, the number is likely to be the same.
# Photgraphs can be used as seeds by sampling the image and turning it into binary, then using that as a seed.



# ** PRECURSOR CHALLENGE **
# Create your own pseudorandom number generator that utilizes as seed to output a random number. 
# The seed should be a floating-point number with five total digits (including those before and after the decimal), and it must be greater than 100.0. 
# Perform at least 3 different math calculations on it (ie, addition, subtraction, and division). 
# Use math library to round the float DOWN to an integer. 
# BONUS CHALLENGE: Make your random number output between 1 and 10. 

seed = 83504
seed2 = seed / 1204
seed2 = math.floor(seed2)
seed3 = seed * 567
seed4 = seed % 9
print(seed4)

import random
luckynum = 67

lucky = random.randint(1, 1000000) # makes a random number from 1 - 1000000

print(lucky)

if(lucky == luckynum):
    print("YOU WON THE GAMBLING!!!")
else:
    print("YOU LOST ALL YOUR MONEY AND NOW YOU'RE HOMELESS!")