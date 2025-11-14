# WH 2nd order up practice

#dictionary for the menu
menu = {
    #dictionary for drinkes
    "drink": {
        "apple juice": 4.99,
        "sprite": 4.99,
        "milk": 8.99,
        "water": 0.00
    },
    #dictionary for sides
    "side": {
        "applesauce": 2.99,
        "corn": 4.99,
        "carrot": 8.99
    },
    #dictionary for mains
    "main course": {
        "hotdog": 9.99,
        "ham": 6.99,
        "chicken": 6.99,
        "burger": 6.99,
        "eggs": 8.99
    }
}

# define a fnction that dose the order with the item name
def orderAdd(item_name):
    #show the item name with a loop
    #some varibles to make it easer to order
    number = 0
    item = {}
    #to space it
    print()
    for pr in menu[item_name]:
        #add one to number
        number += 1
        #and the item name to item
        item[str(number)] = pr
        print(f"{number}: {pr} is {menu[item_name][pr]}")
    #ask the user what item name the want 
    want = input(f"\nwhat {item_name} do you want.\n").strip().lower()
    #check if the item name is one the menu
    try:
        #tell them it went through
        print(f"you have orderd {want}\n")
        #return that item name
        return [want,menu[item_name][want]]
    except:
        #if the other dos not work do try this one to see if they did an number
        try:
            #tell them it went through
            print(f"you have orderd {item[want]}\n")
            #return that item name
            return [item[want],menu[item_name][item[want]]]
        except:
            #if they bolth don't work tell them that is not on the menu
            print("\nnot on menu.\n")

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
        #add order add to order
        order.append(orderAdd("drink"))

    #if the user wants to get a side
    elif want == "2" or want == "side":
        #add order add to order
        order.append(orderAdd("side"))

    #if the user wants to get a main course
    elif want == "1" or want == "main course":
        #add order add to order
        order.append(orderAdd("main course"))

    #if the user wants to order 
    elif want == "4" or want == "order":
        #if order has somthing in it
        if order != []:
            #set how much you pay
            pay = 0
            #show you orderd
            print("\nyou orderd:")
            #print the order with one loop
            for item in order:
                print(f"{item[0]} is {item[1]}$")
                pay += item[1]
            print(f"that comes to {pay}$.")
            #end
            break
        #else
        else:
            #sow that they have not orderd anythig
            print("\nyou have no things to order\n")
    #if the user put in a not valid imput
    else:
        #show that it is not valid
        print("\nnot an option.\n")