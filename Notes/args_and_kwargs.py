# WH 2nd *args and **kwargs

"""def hello(name = "what", age = "?"):
    return f"Hello {name}! You are {age}!"

print(hello())
print(hello(age = 5, name ="Bob"))"""

def hello(*names, **last):
    for name in names:
        if name == "ted":
            print(f"Hello {name} {last["vlast"]}!")
        else:
            print(f"Hello {name} {last["all"]}!")

hello("will", "will", "will", "ted", all = "me", vlast = "e")