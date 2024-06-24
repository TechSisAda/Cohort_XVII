names = ["Joab", "Grace", "Kifasi"]
cgpa = [4.49, 2.45, 3.6]
# Indexing of List
print(names[0])
print(cgpa[0])
student_name = names[0]
student_score = cgpa[0]
print(f"{student_name} scored {student_score}")

# Finding the index of an item.
index = names.index("Grace")
print("index:", index)
student_name = names[index]
student_score = cgpa[index]
print(f"{student_name} scored {student_score}")

names2 = ["Asiya", "Emmanuel", "Oluwole", "Wilfred", "Maimuna"]
scores = [30, 70, 75, 95, 55]
names2.append("Wisdom")
scores.append(96)
print(names2)
print(scores)

names2.extend(["Khalifa"])
scores.extend([96])
print(names2)
print(scores)
names2.extend("Joy")
print(names2)
