# WH 2nd order up practice

#dictionary for the menu
menu = {
    #dictionary for drinkes
    "drinks": {
        "apple juice": 4.99,
        "sprite": 4.99,
        "milk": 8.99,
        "water": 0.00
    },
    #dictionary for sides
    "sides": {
        "applesauce": 2.99,
        "corn": 4.99,
        "carrot": 8.99
    },
    #dictionary for mains
    "food": {
        "hotdog": 9.99,
        "ham": 6.99,
        "chicken": 6.99,
        "burger": 6.99,
        "eggs": 8.99
    }
}

#set order
order = []

#show that the user should a least oder a main 2 sides and a drink
print("It's recremende to order 1 main course 2 sides and a drink.")
#loop for order
while True:
    #ask if the want drink side or main course want to order
    want= input("1. main course\n2. side\n3. drink\n4. order\n").strip().lower()

    #if the user wants a drink
    if want == "3" or want == "drink":
        #show the drinkes with a loop
        #some varibles to make it easer to order
        number = 0
        item = {}
        #to space it
        print()
        for pr in menu["drinks"]:
            #add one to number
            number += 1
            #and the drink to item
            item[str(number)] = pr
            print(f"{number}: {pr} is {menu["drinks"][pr]}")
        #ask the user what drink the want 
        want = input("\nwhat drink do you want.\n").strip().lower()
        #check if the drink is one the menu
        try:
            #add that drink to order
            order.append([want,menu["drinks"][want]])
            #tell them it went through
            print(f"you have orderd {want}\n")
        except:
            #if the other dos not work do try this one to see if they did an number
            try:
                #add that drink to order
                order.append([item[want],menu["drinks"][item[want]]])
                #tell them it went through
                print(f"you have orderd {item[want]}\n")
            except:
                #if they bolth don't work tell them that is not on the menu
                print("\nnot on menu.\n")
        #set want to 3 to not make it end
        want = "3"

    #if the user wants to get a side
    if want == "2" or want == "side":
        #show the sides with a loop
        #some varibles to make it easer to order
        number = 0
        item = {}
        #to space it
        print()
        for pr in menu["sides"]:
            #add one to number
            number += 1
            #and the sides to item
            item[str(number)] = pr
            print(f"{number}: {pr} is {menu["sides"][pr]}")
        #ask the user what side the want 
        want = input("\nwhat side do you want.\n").strip().lower()
    #check if the side is one the menu
        try:
            #add that side to order
            order.append([want,menu["sides"][want]])
            #tell them it went through
            print(f"you have orderd {want}\n")
        except:
            #if the other dos not work do try this one to see if they did an number
            try:
                #add that side to order
                order.append([item[want],menu["sides"][item[want]]])
                #tell them it went through
                print(f"you have orderd {item[want]}\n")
            except:
                #if they bolth don't work tell them that is not on the menu
                print("\nnot on menu.\n")
        #set want to 3 to not make it end
        want = "2"

    #if the user wants to get a main course
    if want == "1" or want == "main course":
        #show the main course with a loop
        #some varibles to make it easer to order
        number = 0
        item = {}
        #to space it
        print()
        for pr in menu["food"]:
            #add one to number
            number += 1
            #and the main course to item
            item[str(number)] = pr
            print(f"{number}: {pr} is {menu["food"][pr]}")
        #ask the user what main course the want 
        want = input("\nwhat main course do you want.\n").strip().lower()
    #check if the main course is one the menu
        try:
            #add that main course to order
            order.append([want,menu["food"][want]])
            #tell them it went through
            print(f"you have orderd {want}\n")
        except:
            #if the other dos not work do try this one to see if they did an number
            try:
                #add that main course to order
                order.append([item[want],menu["food"][item[want]]])
                #tell them it went through
                print(f"you have orderd {item[want]}\n")
            except:
                #if they bolth don't work tell them that is not on the menu
                print("\nnot on menu.\n")
        #set want to 3 to not make it end
        want = "1"

    #if the user wants to order 
    elif want == "4" or want == "order":
        #if order has somthing in it
        if order != []:
            #continue to printing
            break
        #else
        else:
            #sow that they have not orderd anythig
            print("\nyou have no things to order\n")
    #if the user put in a not valid imput
    else:
        #show that it is not valid
        print("\nnot an option.\n")

#set how much you pay
pay = 0
#show you orderd
print("\nyou orderd:")
#print the order with one loop
for item in order:
    print(f"{item[0]} is {item[1]}$")
    pay += item[1]
print(f"that comes to {pay}$.")