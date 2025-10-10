# Wh 2nd password checker projects

# loop for the pasword checker
#   ask for the thing the user wants to do
#   if the user wants to check a pasword
#       set upper to 0
#       set lower to 0
#       set num to 0
#       set special to 0
#       set letter_lenght to 0
#       set lenght to 0
#       ask for the users pasword
#       loop for each letter in password each letter being the letter
#       add one to letter_lenght
#       if letter has ASDFGHJKLQWERTYUIOPZXCVBNM in it
#           set upper to 1
#       if letter has qwertyuiopasdfghjklzxcvbnm in it
#           set lower to 1
#       if letter has 1234567890 in it
#           set num to 1
#       if letter has ~\`!@#$%^&*()\_+-={}[]|;':\"<>?,./ in it
#           set special to 1
#       if letter_length = 8
#           set lenght to 1
#       set strenght to special + num + uppper + lower + length
#       if 