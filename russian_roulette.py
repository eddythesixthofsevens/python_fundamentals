import random
loaded = 5


blank = random.randint(1, 6) # makes a random number from 1 - 1000000 
print(blank)
if(blank != loaded):
    print("You're safe... for now.")
else:
    print("You fired the live round. You're dead.")