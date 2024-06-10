# c^2 = a^2 + b^2
a = 7
b = 24
c = (a**2 + b**2) ** 0.5
print(c)

# f(x) = x^2 - 5x + 6
# x = (-b + sqrt(b^2 - 4ac)) / 2a
a = 1
b = -5
c = 6
x = (-b + (b**2 - 4*a*c) ** 0.5) / (2*a)
print(f"x: {x}")
x = (-b - (b**2 - 4*a*c) ** 0.5) / (2*a)
print(f"x: {x}")
