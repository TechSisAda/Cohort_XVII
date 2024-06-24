number = int(input("Enter the number: "))
divisors = range(1, number+1)
count = 0
for denominator in divisors:
    if number % denominator == 0:
        count += 1

if count == 2:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
    