character = {
    "Name": "Phong",
    "Age": 18,
    "Strength": 7,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Ashe", "Aziz"],
    "Gold": 100,
    "Level":10
}

character["Gold"] += 50
print("Gold: ", character["Gold"])

character["Backpack"].append("FlintStone")
print("Backpack:", ",".join(character["Backpack"]))
#Phan7
skills = [
    {"Name": "tack", "minium level": 1, "Damage":5, "Hit rate":0.3},
    {"Name": "Attack", "minium level": 2, "Damage": 3, "Hit rate":0.5},
    {"Name": "Strong Kick", "minium level": 4, "Damage": 9, "Hit rate":0.2},
]
for i, skill in enumerate(skills, start=1):
    print("skill", i, ":", skill["Name"])