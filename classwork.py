username = input("Enter your name: ")
office = input("Enter your office title: ")

# If you create separate strings which are in separate lines inside a pair of brackets
# The strings are automatically joined together by python.
message_body = ("Wisdom Joab, you have been admitted to the faculty of Engineering at Kwara State University, \n"
                "to study Civil Engineering. Please note that on entry into the programme, you are expected to abide \n"
                "by all the rule and regulations of this great Institution.")

message_sender = "Signed " + username
# The code below is just another way of doing the same thing above
# message_sender = f"Signed {username}"

remark = "Yours faithfully."

admission_letter = (message_body + "\n" + message_sender + "\n" + office + "\n" + remark)
# The code below is just another way of doing the same thing above
# admission_letter = f"{message_body} \n{message_sender} \n{remark}"

print(admission_letter)
