first_number = float(input("Enter first number? \n"))
second_number = float(input("Input the second number? \n"))
operator_sign = str(input("What operator? (+ , - , * , / ) \n"))

def calculate(first_num, second_num, operator_sign):
    if operator_sign == '+':
        return first_num + second_num
    elif operator_sign == '-':
        return first_num - second_num
    elif operator_sign == '*':
        return first_num * second_num
    elif operator_sign == '/':
        if second_num == 0:
            return "Error! Division by zero aint allowed."
        return first_num / second_num
    else:
        return "Error: Unknown Operation."

result = calculate(first_number, second_number, operator_sign)

print(f"The result of {first_number} {operator_sign} {second_number} is: {result}")