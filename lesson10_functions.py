# functions are blocks of code that can be reused
# to run a function, you call it by writing its name followed by parentheses and any arguments it needs

print("Functions (Procedures)")

print("\nExample 1")

def say_hi():
    print("Hi.")

def say_bye():
    print("Bye.")

say_hi()
say_bye()

print("\nExample 2")

def express_this(e): # e is called a parameter, which is a placeholder for an ARGUMENT
    return e
expression1 = express_this(1 + 2)   # the mathematical expression is the argument,the actual value that will be used by a function's parameter
print(expression1)
expression2 = express_this(45 * 6)
print(expression2)

print("\n Example 3")

def greeter(n): # n is the parameter
    return f"Hi, {n}. "
first = greeter("Jojo")
second = greeter("Bizbo")
third = greeter ("Hoppy")

print(first, second, third)

print("\n Example 4")

def remainder(a, b):
    return a % b
result = remainder(6, 2)
print("Remainder:", result)

print("\n Example 5")

def is_far(distance):
    # INSERT BASE CASE
    if distance < 1 or distance > 100:
        return "Error"
    elif distance >= 100:
        return "That's far."
    elif distance < 100 and distance > 20:
        return "That's not too far."
    elif distance <= 20:
        return "That's nearby."
print(is_far(20))

print("\n Example 6")
# I want to create a function that takes in a number and doubles it, then adds it to a list.
# The function should also take in a number of times that we should double the number

def double_sequencer(number, times):
    value = number
    sequence = []
    sequence.append(value)
    for i in range(times):
        value = value * 2
        sequence.append(value)
    
    return sequence
result = double_sequencer(1,5)
print(result)