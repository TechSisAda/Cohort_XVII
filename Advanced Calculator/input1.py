run_again = stop
while not stop:
    print(""" 
          Welcome to the Nexus Calc 
          What Operation do you want to perform. Enter below to confirm:
          1. ADD
          2, SUBTRACT
          3. MULTIPLY
          4. DIVIDE 
          5. EXPONENT 
          6. QUIT 
          """)
    
    user_choice = input("Make a choice: ")
    user_choice = int(user_choice)
    if user_choice == 1:
    
    stop = user_choice == 6