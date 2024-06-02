#LOAN AGREEMENT PROJECT
amount_input = 0
loan_rate = 0
loan_duration = 0

name_input = str(input("Enter your name (Surname first): \n"))
name = name_input.title()

bank_input = str(input("Enter Bank name: \n"))
bank = bank_input.upper()

amount_input = int(input("How much do you intend to loan? \n"))
loan_rate = float(input("How much rate you intend " + bank_input + " to loan you? \n"))
loan_duration = int(input("How many years is this loan valid for ? \n"))


P = amount_input
R = loan_rate
T = loan_duration

interest = P * R * T / 100
A = float(P + interest)

agreement = str(f'''I, {name}, hereby agree to accept the loan of ₦{amount_input}
for the period of {loan_duration} years at a rate of {loan_rate}% from {bank} Ltd.\nI, oblige of my own free will to comply with all the CBN rules and regulations guiding loan,
contracts and will not hold the lending party {bank} Ltd responsible for confiscating all designated collateral, 
should I not pay the requisite return of ₦{A} at the end of the loaning term.''')

print(agreement)
print(f"Signed {name}")
