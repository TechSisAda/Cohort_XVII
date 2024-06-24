names = ["Asiya", "Emmanuel", "Oluwole", "Wilfred", "Maimuna"]
scores = [30, 70, 75, 95, 55]
print(names)
print(scores)

# add lists with +
# multiply list values with *
new_names = ["Fatima", "Onyedika", "Grace"]
new_scores = [82, 50, 70]
final_names = names + new_names
final_scores = scores + new_scores
names.extend(new_names)
scores.extend(new_scores)
print(names)
print(scores)
print(final_names)
print(final_scores)

# names = names * 7
# print(names)

names.remove("Fatima")
print(names)
scores.remove(82)
print(scores)

fruits = ["Love", "Joy", "Peace", "Patience", "Longamnity", "Goodness", "Benignity"]
scores = [20, 100, 50, 20, 12, 50, 75]

index = fruits.index("Patience")
fruits.pop(index)
scores.pop(index)
print(fruits)
print(scores)
