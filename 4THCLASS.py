# # names = ["Joab", "Grace", "Kifasi"]
# # cgpa = [4.49, 2.45 , 3.6]

# # #indexing the list
# # print(names[0])
# # print(cgpa[0])
# # student_name = names[0]
# # student_score = cgpa[0]
# # print(f"{student_name} scored {student_score}")

# # # finding the index of an item 
# # index = names.index("Kifasi")
# # print("Index: ", index)
# # student_name = names[index]
# # student_score = cgpa[index]

# # print(f"{student_name} scored {student_score}")



# names = ["Asiya", "Emmanuel", "Oluwole", "Kifasi", "Mariam"]
# scores = [30, 70, 75, 95, 55]

# # when using .extend you will use [] inside the ()
# # while .append adds it to end of the list so no need to use [] inside ()

# names.append("adaeze")
# scores.append(96)

# print(names)
# print(scores)

# # add lists with + 
# # multiply list with *

# new_nmaes = ["Fatima", "Onyedika", "Grace"]
# new_scores = [82, 50, 70]

# final_names = names + new_nmaes
# final_scores= scores + new_scores

# names.extend(new_nmaes)
# scores.extend(new_scores)
# print(names)
# print(scores)
# print(final_names)
# print(final_scores)

# # you cannot concatenate(+) a list and a string 
# # but you can multiply(*) a list with a number

# # names = names * 7
# # print(names)

# names.remove("Fatima")
# print(names)
# scores.remove(82)
# print(scores)

# fruits = ["love", "joy", "peace", "paitence", "longivity"]
# scoreing = [20, 100, 50, 20, 12]
# print(fruits)
# print(scoreing)

# fruits.pop(3)
# scoreing.pop(3)

# print(fruits)
# print(scoreing)

# FOR ITEM ITERATE 
for item in [1, 2, 3, 4, 5]:
    print(item)