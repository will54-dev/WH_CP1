# WH 2nd combat program

import random

def isint(str):
    try:
        int(str)
        return True
    except:
        return False
    
class_points = 100
while True:
    whant = input(f"you have {class_points} class points to spend on:\n\t1. Damage\n\t2. Defence\n\t3. Health\n\t4. speed\n\t5. Done\n")
    if whant == "1":
        damage = 0
        print(f"your damage is {damage}.")
        spend = input(f"How many points do you whant to spend ({class_points})?\n")
        if isint(spend):
            spend = int(spend)
            if spend > class_points or spend < -1*damage:
                print("Too much or not valid.\n")
            else:
                damage += spend
                print(f"your damage is now {damage}.")
        else:
            print("not a number.\n")
    elif whant == "2":
        pass
    elif whant == "3":
        pass
    elif whant == "4":
        pass
    elif whant == "5":
        break
    else:
        print("As a valid number.\n")
