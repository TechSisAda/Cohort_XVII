# A PROGRAM TO PRINT A FACTORIAL OF POSITIVE NUMBERS 

number = int(input("Enter the number whose factorial you'd like to find: "))

if number < 0:
    print("Please enter a positive number.")
else:
    result = 1
    for i in range(1, number + 1):
        result *= i
    print(f"The factorial of {number} is {result}")
