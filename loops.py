# for item in iterable:
range_object = range(3)
print(range_object)
print("type:", type(range_object))
list_version = list(range_object)
print(list_version)
print(type(list_version))
for item in range(3):
    print(f"Question {item + 1}")
    num1 = float(input("Enter the first num: "))
    num2 = float(input("Enter the second num: "))
    operator = input("Enter the operator ['+', '-', '*', '/']: ")
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print("Invalid operator entered")


