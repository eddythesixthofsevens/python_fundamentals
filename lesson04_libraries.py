# LIBRARIES
# Libraries are kind of like repositories of code that you can import into your files to make code.

# Abstractions are commands with a ton of code behind them that we do not see; we simply run the command.

# MATH LIBRARY

import math

# print("\n--- Math Library ---\n")

# print("Square root: ", math.sqrt(25))
# print("Round up to an integer:", math.ceil(3.14))
# print("Round down to an integer:", math.floor(6.7))
# print("Power:", math.pow(2, 5))
# print("Pi",math.pi)

# # RANDOM LIBRARY
# print("\n--- Random Library ---\n")

# Because computers can't generate random numbers, random library is a pseudorandom number generator (not truly random). 
# It uses a complicated algorithm that creates the appearance of randomness.
# True random would be like rolling a die.
# Pseudorandom generators need a person to create a random number (the date, for example, called a seed) and divide it
# by something (the time), then multiply it by something else (amount of days in the month), and subtract it by
# something (the amount of days in the year).
# Every time you use the same seed, the number is likely to be the same.
# Photgraphs can be used as seeds by sampling the image and turning it into binary, then using that as a seed.

import random

# ** PRECURSOR CHALLENGE **
# Create your own pseudorandom number generator that utilizes as seed to output a random number. 
# The seed should be a floating-point number with five total digits (including those before and after the decimal), and it must be greater than 100.0. 
# Perform at least 3 different math calculations on it (ie, addition, subtraction, and division). 
# Use math library to round the float DOWN to an integer. 
# BONUS CHALLENGE: Make your random number output between 1 and 10. 

# seed = 134.67
# seed2 = seed / 1204
# seed2 = math.floor(seed2)
# seed3 = seed * 567
# seed4 = seed % 10
# seed5 = math.floor(seed4)
# print(seed5)

# input()

# # BONUS
# seed = 12.4444
# step1 = seed / 6.7
# step2 = step1 - 800
# step3 = step2 + 180843
# result = math.floor(step3)
# limitednumber = step3 - result
# answer = math.floor(limitednumber * 10)

# print(answer)

# Abstraction is when a programming language makes a complicated thing easy (random numbers, for example).

print("Random integer:", random.randint(1, 100))

print("Random float between 0 and 1:", random.random())

# Printing random.random() prints a random float, while random.randint prints a random integer in a range.

# Lists in python are done by creating a variable, using open brackets,

print(random.choice(["taco", "burrito", "enchilada", "quesadilla"]))
myfavs = ["ramen", "fish", "koshary", "chicken"]
print(random.choice(myfavs))
print(random.shuffle(myfavs))
print(myfavs)

# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Formulas: the area of a circle is πr² -- the radius is diameter / 2

radius = 14 / 2
circle_area = math.pi * (math.pow(radius, 2))
print(circle_area)

# Challenge 2: Simulate a Die Roll
# Use the random library to simulate rolling a six-sided die.
# The output should be a random integer between 1 and 6.
# Store the result in a variable called "die_roll" and print it.

die_roll = random.randint(1, 6)
print(die_roll)