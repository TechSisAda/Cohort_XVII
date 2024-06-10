num_f9_ameera = 4
num_f9_grace = 7
num_f9_daniel = 5

user_cgpa = input("Ameera enter your CGPA: ")
user_cgpa = float(user_cgpa)
if user_cgpa >= 4.5:
    print("First Class 🎉")
else:
    print("Depart from me stupid servants")

is_sunny = True
is_warm = False
if is_sunny:
    print("It is sunny")
if is_warm:
    print("It is warm")


user_input = int(input("Enter the result of your die: "))
if user_input == 1:
    print("Drop 5k")
elif user_input == 2:
    print("Drop 4k")
elif user_input == 3:
    print("Drop 3k")
elif user_input == 4:
    print("Drop 2k")
elif user_input == 5:
    print("Drop 1k")
elif user_input == 6:
    print("You are free")
else:
    print("Take that back to your village people.")
