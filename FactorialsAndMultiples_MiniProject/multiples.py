# A PROGRAM THAT PRINTS OUT THE MULTIPLES OF 3.5.7 AND 11.
# FROM 1-100

for i in range(1, 101):
    if i % 3 == 0:
        print(f"{i} is a multiple of 3")

for i in range(1, 101):
    if i % 5 == 0:
        print(f"{i} is a multiple of 5")

for i in range(1, 101):
    if i % 7 == 0:
        print(f"{i} is a multiple of 7")

for i in range(1, 101):
    if i % 11 == 0:
        print(f"{i} is a multiple of 11")

