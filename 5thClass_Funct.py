#Get fumction_name(parametres):
#code ...
def confession(lover, beloved):
    print(f"{lover} loves you, {beloved}")

confession(lover= "Kifasi", beloved= "Asiya")
confession(lover= "Jesse", beloved= "Grace")


# def hate_speech(hater, hated):
#     print(f"Everybody hates you, {hated}")

# hate_speech("Daniel", "Kifasi")

def hate_speech(hated, hater = "Everybody"):
    print(f"{hater} hates you {hated}")

hate_speech("Kifasi")

def add_num(a, b, c):
    return a + b + c
result = add_num()