# MODULE 5 ON THE CISCO PYTHON

# WRITE A PROGRAM TO CONVERT MILES TO KILOMETERS.
# WHEN ONE KILOMETER = 1.61 MILES 

# miles = 7.38
# kilometers = 12.25
# m_to_km = miles * 1.61
# km_to_m = kilometers / 1.61
# print(miles, " miles is ", round(m_to_km, 1), " kilometers.")
# print(kilometers, "Kilometers is ", round(km_to_m, 1), "miles.")


# SOLVE THIS SIMULTANEOUS EQN FOR WHEN  X = 1, 0 , -1

# x1 = 0 
# x1 = float(x1)
# y1 = (3*(x1**3)) - (2*(x1 ** 2)) + (3*x1) - 1
# print("y1 = ", y1)

# x2 = 1
# x2 = float(x2)
# y2 = (3*(x2 ** 3)) - (2*(x2 ** 2)) + (3*x2) - 1
# print("y2 = ",y2)

# x3 = -1
# x3 = float(x3)
# y3 = (3*(x3 ** 3)) - (2*(x3 ** 2)) + (3*x3) - 1
# print("y3 = ", y3)


# TEST PROGRAM
# x = 1
# y = 2
# y = y + x is the same as y += x
# y += x
# print(x + y ) 


# PROGRAM THAT CONVERTS HOURS TO SECONDS 
# hour = 1
# seconds = 60
# print("2 Hours = ", hour * (60**2), "seconds")

# USING THE + AND * STATEMENT
# fname = input("Enter your first name: ")
# lname = input("Enter your last name: ")
# # print("Thank you,", fname, lname, end="." )
# print("THANK YOU! " + fname +" "+ lname, end=".")


#CREATING SHAPES (RECTANGLE)
# print("_"*11)
# print(("|" + " "*9 +"|\n")*5, end="")
# print("-"*11)


# CALCULATIONS USING TYPE CONVERSIONS (STR, FLOAT, INT)

# # input a float value for variable a here
# a = float(input("Enter first number = "))
# # input a float value for variable b here
# b = float(input("Enter second number = "))

# # output the result of addition here
# print("ADDITION = a + b = " + str(a + b))
# # output the result of subtraction here
# print("SUBTRACTION = a - b = " + str(a-b))
# # output the result of multiplication here
# print("MULTIPLICATION = a * b = " + str(a*b))
# # output the result of division here
# print("DIVISON = a / b = " + str(a/b))

# print("\nThat's all, folks!")


# TEST CALCULATION
# x = 1
# y1 = 1 / (x + 1 / ((x + 1 / (x + 1 / x))))
# print(y1)

# x = 10
# y2 = 1 / (x + 1 / ((x + 1 / (x + 1 / x))))
# print(y2)

# x = 100
# y3 = 1 / (x + 1 / ((x + 1 / (x + 1 / x))))
# print(y3)

# x = -5
# y4 = 1 / (x + 1 / ((x + 1 / (x + 1 / x))))
# print(y4)

# TO CALCULATE THE TIME AN EVENT STARTS BASED ON THE TIME 
# IT STARTED AND THE DURATION OF THE EVENT 

# # ENTER THE START HOUR 
# start_hour = int(input("Enter the start hour: "))
# start_mins = int(input("Enter the start minutes: "))
# duration = int(input("Enter the duration of event in minutes: "))

# total_mins = (duration + start_mins) + (start_hour * 60)

# # print (total_mins)

# # NEXT CALCULATE THE END HOURS 
# end_hour = (total_mins // 60)
# end_mins = (total_mins % 60)
# print (f"The event ends by {end_hour} : {end_mins}")

# THE STRICT (>, <) AND NON-STRICT (>=, <=) OPERATORS
# number_of_lions = 10
# number_of_lioness = 23
# answer = number_of_lions >= number_of_lioness
# print(answer)

# n = int(input())
# answer = n > 100
# print (answer)

num_1 = int(input())
num_2 = int(input())
num_3 =int(input())
# # if num_1 > num_2 :
# Larger_num = num_1
# if num_2 > Larger_num:
#     Larger_num = num_2

# if num_3 > Larger_num:
#     Larger_num = num_3
# # else:
# #     Larger_num = num_2

# print("The larger number is: ", Larger_num)

# YOU CAN ALSO USE MAX AND MIN AS BUILT-IN FUNCTION N=BY PYTHON
larger_num = max(num_1, num_2, num_3)
smaller_num = min(num_1, num_2, num_3)
print ("The larger number is: ", larger_num)
print("The smaller number is: ", smaller_num)