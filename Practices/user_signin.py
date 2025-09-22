# WH 2nd user signin practice

users = [2,["will","hehehe"],["e","1234443"]]

while True:
    while_bool = [True, True, False]
    user_number = 1
    che_number = 3
    username = input("input your user name or type Help for becoming a new user:\n")
    # che user name
    while while_bool[0]:
        if username == users[user_number][0]:
            print(f"hello {users[user_number][0]}")
            while_bool[0] = False
            password = input("input your password:\n")
        elif users[0] == user_number:
            print("your not a user")
            while_bool = [False, False, False]
        elif username == "Help":
            while_bool = [False, False, True, True]
        else:
            user_number += 1
    # che password
    while while_bool[1]:
        if password == users[user_number][1]:
            print(f"welcone {users[user_number][0]}")
            while_bool[1] = False
        elif che_number == 1:
            while_bool[1] = False
        else:
            print(f"wrong pasword {che_number} tries left")
            che_number += -1
            password = input("input your password:\n")
    #new user
    while while_bool[2]:
        user_number = 1
        new_user_1 = input("give your new user name:\n")
        new_user_2 = input("now repeat:\n")
        new_password_1 = input("input your new password:\n")
        new_password_2 = input("now repeat your password:\n")
        if new_user_1 == new_user_2 and new_password_1 == new_password_2:
            while while_bool[3]:
                if new_user_1 == users[user_number][0]:
                    print("aredy a user")
                elif users[0] == user_number:
                    users += [[new_user_1, new_password_1]]
                    users[0] += 1
                    while_bool = [True, True, False, False]
                    print("now a user")
                else:
                    user_number += 1
        else:
            print("not repeated corectly")