catalogue = {
    "Essential MATLAB": "Shelf 4, Block 2 Row 3",
      "Principles of Elect Engine": "Shelf 5, Block 2, Row 3"
    }

print(catalogue["Principles of Elect Engine"])

print(type(catalogue))
location = catalogue.get("Principles of Elect Engine")
print(location)

catalogue2 = catalogue.copy()
#old dictionary.update({key: value})
catalogue2.update({"Higher Engine Maths": "Shelf 8, Block 4, Row 5"})
print(catalogue2)

catalogue2_keys = list(catalogue2.keys())
print(catalogue2_keys)
print(catalogue2.keys())
print(type(catalogue2.keys()))

print("\n\n")
for book_name in catalogue2.keys():
    print(f" Hello Librarian, please enter the new location for the book {book_name}")
    catalogue2[book_name] = input("New Location: ")
    print(catalogue2)

dictionary = {
    "PY/BEG/17/001": 4.49,
    "PY/BEG/17/002": 3.5,
    "PY/BEG/17/003" : 3.9
}

for (matric_no, cgpa) in dictionary.items():
    print(f"{matric_no} scored {cgpa}")
# name = ["Amirat", "Ameerah", "Ameera"]
# sister = ["Umm Ammarah", "Ammarah"]
# print(name)
# print(sister)
# sister = name.copy
# print(name)
# print(sister)

# name.pop(1)
# print(name)
# print(sister)
