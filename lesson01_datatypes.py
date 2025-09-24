# This is a comment.
# DATA TYPES

# 1. STRINGS

# normal text in quotation marks, including numbers.
print("Hello world!")
# Can be very long.
print(" ")
# Can print open spaces.
# Escape commands like \n
print("Once upon a time there was a very good time called possessed fishes \nwho ate exquisite cheeses and queso devised by clever chickens")
# tab escape command: \t
print("Name: \tEdwin \nAge: \t14 \nGrade: \t9")

# 2. INTEGERS
# whole numbers, positive and negative

print(70)
print(-42)
print(100 - 30)

# 3. FLOAT
# a decimal
# named floats because the decimal can float

print(4.0)
print(2.0 + 4.5)
print(2 + 3.7)
print(6.744 + 7.222)
print(2.0 + 4) #returns a float

# 4. BOOLEAN
# true or false
#compares two values

print(True) # true = 1
print(False) # false = 0
print(True + False)
print(True - True)
print (1 == 1.0) # == checks if two things are equal
print(1 != 2) # != checks if two things are not equal
print("Hello" == "Hello") # case sensitive
print("Hello" == "hello")
print(5 + 5 == 11) # works with expressions

#How do I know what data type I'm working with?

print("\nDATA TYPE LOOKUP\n")

print(type("To see this message, wrap me in a print statement"))

print(type("hola"))
print(type(1))
print(type(1.2453))
print(type(67 != 67))