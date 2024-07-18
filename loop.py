# # A program that reads a sequence of numbers
# # and counts how many numbers are even and how many are odd.
# # The program terminates when zero is entered.

# odd_numbers = 0
# even_numbers = 0

# # Read the first number.
# number = int(input("Enter a number or type 0 to stop: "))

# # 0 terminates execution.
# while number != 0:
#     # Check if the number is odd.
#     if number % 2 == 1:
#         # Increase the odd_numbers counter.
#         odd_numbers += 1
#     else:
#         # Increase the even_numbers counter.
#         even_numbers += 1
#     # Read the next number.
#     number = int(input("Enter a number or type 0 to stop: "))

# # Print results.
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count:", even_numbers)

# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

####        GUESS THE NUMBER       #####
# secret_number = 222

# guess = int(input("Guess the secret number: "))

# while guess != secret_number:
#     print("Ha ha! You're stuck in my loop!")
#     guess = int(input("Guess the secret number: "))

# print("Well done, muggle! You are free now.")


# #######    FOR LOOP     #######
# for i in range(2, 8):
#     print("The value of i is currently", i)

# for i in range(1, 100):
#     if i%2 !=0:
#         print(i)

# import time
# for i in range(1, 6):
#     print( i, "Mississipi")
#     i += 1
#     time.sleep(1)

# print("Ready or not, here i come")

# break - example

largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end the program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

