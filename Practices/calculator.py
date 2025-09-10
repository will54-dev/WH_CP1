# WH 2nd calculator practice

while(1 == 1):
    while_num = 0
    while while_num == 0:
        number_1 = input("give a number: ")
        try:
            number_1 = float(number_1)
            while_num = 1
        except:
            while_num = 0

    while while_num == 1:
        number_2 = input("give another number: ")
        try:
            number_2 = float(number_2)
            while_num = 2
        except:
            while_num = 1
    addition = False
    if input("would you like to add. ") == "yes":
        print("you are adding")
        addition = True
    subtraction = False
    if input("would you like to subtract. ") == "yes":
        print("you are subtracting")
        subtraction = True
    multiplication = False
    if input("would you like to Multiply. ") == "yes":
        print("you are multiplying")
        multiplication = True
    division = False
    if input("would you like to use division. ") == "yes":
        print("you are dividing")
        division = True
    int_division = False
    if input("would you like to use integer division. ") == "yes":
        print("you are using integer division")
        int_division = True
    modulo = False
    if input("would you like to use modulo. ") == "yes":
        print("you are using modulo")
        modulo = True
    exponents = False
    if input("would you like to use exponents. ") == "yes":
        print("you are using exponents")
        exponents = True

    if addition == True:
        try:
            print(f"{number_1} + {number_2} = {number_1+number_2}")
        except:
            print(f"it failed to perform {number_1} + {number_2}")
    if subtraction == True:
        try:
            print(f"{number_1} - {number_2} = {number_1-number_2}")
        except:
            print(f"it failed to perform {number_1} - {number_2}")
    if multiplication == True:
        try:
            print(f"{number_1} * {number_2} = {number_1*number_2}")
        except:
            print(f"it failed to perform {number_1} * {number_2}")
    if division == True:
        try:
            print(f"{number_1}/{number_2} = {number_1/number_2}")
        except:
            print(f"it failed to perform {number_1}/{number_2}")
    if int_division == True:
        try:
            print(f"{number_1}//{number_2} = {number_1//number_2}")
        except:
            print(f"it failed to perform {number_1}//{number_2}")
    if modulo == True:
        try:
            print(f"{number_1} % {number_2} = {number_1%number_2}")
        except:
            print(f"it failed to perform {number_1} % {number_2}")
    if exponents == True:
        try:
            print(f"{number_1} ** {number_2} = {number_1**number_2}")
        except:
            print(f"it failed to perform {number_1} ** {number_2}")