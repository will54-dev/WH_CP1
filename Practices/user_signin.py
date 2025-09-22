# WH 2nd user signin practice

users = [2,["will","123456"],["e","1234443"]]

while True:
    while_bool = [True, True, False]
    user_number = 1
    username = input("input your user name:\n")
    # che user name
    while while_bool[0] == True:
        if username == users[user_number][0]:
            print(f"hello {users[user_number][0]}")
            while_bool[0] = False
        elif users[0] == user_number:
            print("not a user")
            while_bool[0] = False
            while_bool[1] = False
            while_bool[2] = True
        else:
            user_number += 1
    user_number = 1
    password = input("input your password:\n")
    # che password
    while while_bool[1] == True:
        if password == users[user_number][1]:
            print(f"welcone {users[user_number][0]}")
            while_bool[1] = False
        elif users[0] == user_number:
            print("wrong pasword")
            user_number = 1
        else:
            user_number += 1