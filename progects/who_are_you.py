# WH 2nd who are you progect

user_name = input("give you name: ")
#user_age = input("give you age")
#user_color = input("give your favorite color")
with open("users.txt") as e:
e.write(user_name)
with open("users.txt", "w") as e:
    print(e.read())