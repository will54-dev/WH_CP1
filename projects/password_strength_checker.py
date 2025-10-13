# Wh 2nd password checker projects

# set times to 0
times = 0
# user list to a list of e, pasword, Password, P@ssword, P@sswr0d
user_list = [["e",1],["pasword",2],["Password",3],["P@ssword",4],["P@sswr0d",5]]
# loop for the pasword checker
while True:
#   ask for the thing the user wants to do
    while True:
        try:
            want = int(input("1: check a pasword\n2: see all paswords\n3: compare passwords\n4:exit\n\t"))
            break
        except:
            print("not a number")
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
        password = input("make a password\n")

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
            if letter in "~`!@#$%^&*()\\_+-={\}[]|;':\"<>?,./":
#               set special to 1
                special = 1
#       if letter_length >= 8
        if letter_lenght >= 8: 
#           set lenght to 1
            lenght = 1

#       set strenght to special + num + uppper + lower + length
        strenght = special + num + upper + lower + lenght

#       if strenght = 0
        if strenght == 0:
#           show [------------------------------]
            print("[------------------------------]")
#       else if strenght = 1
#           show [######------------------------]
#       else if strenght = 2
#           show [############------------------]
#       else if strenght = 3
#           show [##################------------]
#       else if strenght = 4
#           show [########################------]
#       else if strenght = 5
#           show [##############################]

#       if special = 0
#           show you need a special character.
#       if num = 0
#           show you need a number.
#       if upper = 0
#           show you need an uppercase letter.
#       if lower = 0
#           show you need a lowercase letter.
#       if length = 0
#           show you need 8 character.
#       set user list index times = pasword & strenght
#       add 1 to times

#   if the user wants to see all paswords

#       show user list but cool

#   if the user wants to compare pasword

#       show user list but cool with out the strenght

#       user imput for item what do you want
#       show your pasword pasword is strenght-user list item strenght points stronger.

#   if the user wants to exit 
#       end loop