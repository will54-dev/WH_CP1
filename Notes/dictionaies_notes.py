# Wh 2nd notes for dictionarie

avatar = {
    "earth": {
        "Toph": "My name is Toph, cuz it sounds like TOUGH and thats just what I'm."
    },
    "water": {
        "katara": "It's not like I'm a preachy crybaby who can't halp but make speaches about hope all the time.",
    }
}
print(avatar["earth"]["Toph"])
person = {
    #key: value,
    "name": "Katie",
    "age": 37,
    "job": "cordinator",
    "siblings": ["Alex", "Andrew", "tia", "Xavier", "Jake", "Treyson"]
}

print(person["job"])

def print_person(name):
    for key in name.keys():
        if key == "siblings":
            print("Siblings are:")
            for names in name[key]:
                print(f"\t{names}")
        else:
            print(f"{key}: {name[key]}")

print_person(person)
print(person.values())
person["age"] += 1
person["birthday"] = "June 8"
print_person(person)
person["birthday"] = "october 27"
print_person(person)