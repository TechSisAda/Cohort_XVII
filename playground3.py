num1 = 120.2
# Xen => X * 10^n
num2 = 6
num3 = num1 // num2
print(num3)
print(type(num3))

# Todo: Conventions for arithmetic data types
# 1. if any of the inputs is a float -> float
# 2. if the operator is / -> float
# 3. if the operator is // and no input is a float -> int
# 4. if the result is decimal or whole number
# -> float (decimal) / int (whole number)

# binary (num) -> 0bnum
binary1 = 0b1000
print(binary1)
# octal (num) -> 0onum
octal1 = 0o7
print(octal1)
# hexadecimal (num) -> 0xnum
hex1 = 0x10
print(hex1)
