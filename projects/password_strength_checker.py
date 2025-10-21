# Wh 2nd password checker projects

# user list to a list of e, pasword, Password, P@ssword, P@sswr0d
user_list = [["e",1],["password",2],["PASSword",3],["P@ssword",4],["P@sswr0d",5]]
# loop for the pasword checker
while True:
#   ask for the thing the user wants to do
    while True:
        try:
            want = int(input("1: check a password\n2: see all passwords\n3: compare passwords\n4: exit\n"))
            break
        except:
            print("not a number")
        print("------------------------------------------------------")
    print("------------------------------------------------------")
#   if the user wants to check a pasword
    if want == 1:
#       set upper to 0
        upper = 0
#       set lower to 0
        lower = 0
#       set num to 0
        num = 0
#       set special to 0
        special = 0
#       set letter lenght to 0
        letter_lenght = 0
#       set lenght to 0
        lenght = 0
#       ask for the users pasword
        password = input("make a password to check\n")

#       loop for each letter in password each letter being the letter
        for letter in password:
#               add one to letter lenght
            letter_lenght +=1
#           if letter has ASDFGHJKLQWERTYUIOPZXCVBNM in it
            if letter in "ASDFGHJKLQWERTYUIOPZXCVBNM":
#               set upper to 1
                upper = 1
#           if letter has qwertyuiopasdfghjklzxcvbnm in it
            if letter in "qwertyuiopasdfghjklzxcvbnm":
#               set lower to 1
                lower = 1
#           if letter has 1234567890 in it
            if letter in "1234567890":
#               set num to 1
                num = 1
#           if letter has ~\`!@#$%^&*()\_+-={}[]|;':\"<>?,./ in it
            if letter in "~`!@#$%^&*()\\_+-={}[]|;':\"<>?,./":
#               set special to 1
                special = 1
#       if letter_length >= 8
        if letter_lenght >= 8: 
#           set lenght to 1
            lenght = 1

#       set strenght to special + num + uppper + lower + length
        strenght = special + num + upper + lower + lenght

        print("------------------------------------------------------")
#       if strenght = 0
        if strenght == 0:
#           show [------------------------------]
            print("[------------------------------]")
#       else if strenght = 1
        elif strenght == 1:
#           show [######------------------------]
            print("[######------------------------]")
#       else if strenght = 2
        elif strenght == 2:
#           show [############------------------]
            print("[############------------------]")
#       else if strenght = 3
        elif strenght == 3:
#           show [##################------------]
            print("[##################------------]")
#       else if strenght = 4
        elif strenght == 4:
#           show [########################------]
            print("[########################------]")
#       else if strenght = 5
        elif strenght == 5:
#           show [##############################]
            print("[##############################]")
#       if special = 0
        if special == 0:
#           show you need a special character.
            print("you need a special character.")
#       if num = 0
        if num == 0:
#           show you need a number.
            print("you need a number.")
#       if upper = 0
        if upper == 0:
#           show you need an uppercase letter.
            print("you need an uppercase letter.")
#       if lower = 0
        if lower == 0:
#           show you need a lowercase letter.
            print("you need a lowercase letter.")
#       if length = 0
        if lenght == 0:
#           show you need 8 character.
            print("you need 8 character.")
#       set user list index times = pasword & strenght
        user_list.append([password,strenght])
        print("------------------------------------------------------")


#   if the user wants to see all paswords
    elif want == 2:
        print("\tPasswords")
#       show user list but cool
        item_lenght = 0
        for x in user_list:
            item_lenght += 1
            print(f"{item_lenght}. {x[0]}: strenght {x[1]}")
        print("------------------------------------------------------")
#   if the user wants to compare pasword
    elif want == 3:
#       show user list but cool with out the strenght
        item_lenght = 0
        for x in user_list:
            item_lenght += 1
            print(f"{item_lenght}. {x[0]}")
        print("------------------------------------------------------")

#       user imput for item what do you want
        while True:
            try:
                item1 = int(input("which password do you want to compare. (as a number)\n"))
                item1 = user_list[item1-1]
                break
            except:
                print("------------------------------------------------------")
                print("not a number or not on list.")
                print("------------------------------------------------------")
        print("------------------------------------------------------")
        while True:
           try:
               item2 = int(input("which password do you want to compare it with. (as a number)\n"))
               item2 = user_list[item2-1]
               break
           except:
               print("------------------------------------------------------")
               print("not a number or not on list.")
               print("------------------------------------------------------")
#       show your pasword pasword is strenght - user list item strenght points stronger.
               print("------------------------------------------------------")
               print(f"{item1[0]} is {item1[1]-item2[1]} stronger than {item2[0]}")
               print("------------------------------------------------------")

#   if the user wants to exit 
    elif want == 4:
#       end loop
        break