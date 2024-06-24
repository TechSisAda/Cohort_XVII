stop_number = int(input("Enter the number limit: "))
divisor = int(input("Enter the divisor: "))
multiples = []
for number in range(1, stop_number + 1):
    if number % divisor == 0:
        multiples.append(number)

print(multiples)
