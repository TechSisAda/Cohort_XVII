# CREATE A BAND NAME GENERATOR 
# The interface should first prompt the user to Enter their state of birth.
# Find then the interface should also prompt the suer to input the kind of pet they possess...
# or wish to possess eg: dog , cats, etc 
# lastly the code should work like this : Abuja Cat 
# start with a welcome message 

print("BAND NAME GENERATOR \nCreate a Name for your band !!! ")
state = input("Enter your state of Origin: \n")
pet = input("What is your favorite pet? \n")

print(f"The name of your band is {state.upper()} {pet.upper()}!!!")
