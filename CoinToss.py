# write a code that smulates a random coin toss such that 
# the program takes in the users name 

# the reuslt should only be heads or tails
#  hence the output should print 
# dear user, the coin toss lands on heads 

# import random

# name = input("Enter your name: ")

# # Generate a random number, 0 or 1
# toss = random.randint(0, 1)

# # Map 0 to "heads" and 1 to "tails"
# result = "heads" if toss == 0 else "tails"

# print(f"{name}, the result of the coin toss is: {result}")



import random

name = str(input(" Enter your name: "))

choice = random.randint(0,1)

if choice == 1:
    print (f"Dear {name}, the coin toss lands on heads")

else: print(f"Dear {name}, the coin toss lands on tails")
