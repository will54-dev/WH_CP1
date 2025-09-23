# WH 2nd Elif and Logical Operators Notes

homework = True
chores = True
room = True

if homework and chores and room:
    print("You can go to your frends house.")
elif not chores or not room:
    print("do your chores")
else:
    print("go do your home work")

username = input("enter your user name: ")
password = input("enter your password: ")

if username == 'will' and password == "1234":
    print("wecome will")
elif username == 'will' and password == "password":
    print("wecome will")
elif username == 'will' and password == "e":
    print("wecome will")
elif username == 'will' and password == "h":
    print("wecome will")
else:
    print("not the magic word")
