# WH 2nd order up practice

#dictionary for the menu
menu = {
    #dictionary for drinkes
    "drinkes": {
        "pine and apple juice": 4.99,
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
        "egg": 600.99
    }
}

#set order
order = []

#show that the user should a least oder a main 2 sides and a drink
print("it's recremende to order 1 main course 2 sides and 1 drink.")
#loop for order
while True:
    #ask if the want drink side or main course want to order
    want = input("1. main course\n2. side\n3. drink 4. order")

    #if the user wants a drink
    if want == "3" or want == "drink":
        #show the drinkes with a loop
        for pr in menu["drinkes"]:
            print(f"{pr} is {menu["drinkes"][pr]}")
        #ask the user what drink the want 
        want = input("waht drink do you want.")
        #check if the drink is one the menu
        try:
            menu["drinkes"][want]
            #add that drink to order
            order.append([want,menu["drinkes"][want]])
        except:
            print("not on menu.")

    #if the user wants to get a side
        #show the sides with a loop
        #ask the user what side the want 
        #add that side to order

    #if the user wants to ge a main course
        #show the main courses with a loop
        #ask the user what main course the want 
        #add that main course to order

    #if the user wants to order 
    else:
        #if order has somthing in it
        if order != []:
            #continue to printing
            break
        #else
        else:
            #sow that they have not orderd anythig
            print("you have no")

#print the order with one loop
