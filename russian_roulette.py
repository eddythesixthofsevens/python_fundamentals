import random
loaded = (1)
blank = random.randint(1, 6)
print(blank)
if(blank != loaded):
    print("You're safe... for now.")
else:
    print("You fired the live round. You're dead.")

loaded = ["1", "2", "3", "4", "5", "6"]
