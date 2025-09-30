# WH 2nd Shopping List Manager

list_shop = []


while True:
    while True:
        print("option 1 add to shopping list.\noption 2 remove from shopping list.\noption 3 view shopping list.\noption 4 exit program.")
        try:
            action = int(input("choose an option (1-4).\n"))
            break
        except:
            print("-----------------------------------")
            print("not an action.")
            print("-----------------------------------")
    if action == 1:
        print("-----------------------------------")
        item = input("enter item.\n")
        print("-----------------------------------")
        list_shop.append(item)
        print(f"{item} added to shopping list.")
    elif action == 2:
        print("-----------------------------------")
        if len(list_shop) != 0:
            while_num = 0
            print("0: nevermind")
            while while_num != len(list_shop):
                print(f"item {while_num+1}: {list_shop[while_num]}")
                while_num += 1
            while True:
                try:
                    item = int(input("What item do you want to remove (as a number):\n"))
                    print("-----------------------------------")
                    break
                except:
                    print("-----------------------------------")
                    print("not an number.")
                    print("-----------------------------------")
            if item == 0:
                print("ok")
            elif item <= len(list_shop) and item >= 1:
                item = list_shop[item-1]
                list_shop.remove(item)
                print(f"{item} removed from list.")
            else:
                print("item is not on list.")
        else:
            print("nothing on list.")
    elif action == 3:
        print("-----------------------------------")
        if len(list_shop) != 0:
            while_num = 0
            while while_num != len(list_shop):
                print(f"item {while_num+1}: {list_shop[while_num]}")
                while_num += 1
        else:
            print("no list")
    elif action == 4:
        print("-----------------------------------")
        print("exited")
        break
    else:
        print("-----------------------------------")
        print("not an action.")
    print("-----------------------------------")
