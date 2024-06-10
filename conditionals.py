# AND
value1 = True
value2 = False
result = value1 and value2


def display(result_text, result_value):
    print(f"{result_text}: {result_value}")


display("AND: (True, False)", value1 and value2)
display("AND: (True, True)", value1 and value1)
display("AND: (False, True)", value2 and value1)
display("AND: (False, False)", value2 and value2)

display("AND: (False, 0)", False and 0)
display("AND: (True, 0)", True and 0)

# TODO: Template AND
# True and True -> True
# True and False -> False
# False and True -> False
# False and False -> False
# operand1 and operand2
#   -> operand1 if operand1 is False
#   -> operand2 if operand1 is True

# OR
display("OR (True, True)", value1 or value1)
display("OR (True, False)", value1 or value2)
display("OR (False, True)", value2 or value1)
display("OR (False, False)", value2 or value2)

# TODO: Template OR
# True and True -> True
# True and False -> True
# False and True -> True
# False and False -> False
# operand1 and operand2
#   -> operand1 if operand1 is True
#   -> operand2 if operand1 is False

# TODO: Type Conversions
display("0 to bool: ", bool(0))
display("'' to bool: ", bool(""))
display("None to bool: ", bool(None))

# NOT
display("Not False", not bool(0))
display("Not True", not bool(4.57))

# XOR
display("XOR (True, False)", value1 ^ value2)
display("XOR (True, True)", value1 ^ value1)
display("XOR (False, True)", value2 ^ value1)
display("XOR (False, False)", value2 ^ value2)


