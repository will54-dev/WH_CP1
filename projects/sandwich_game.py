#Wh 2nd final project 
import random as rand
import math as m
text = {
    "game": {
        "start": "You are a hiker on a trail having a sandwich then a monkey comes by and has stolen your sandwich and gone off the trail.",
        "end": "you got your sandwich back you win. Would you like to play again?"
    },
    "info": {
    #section one
        "trail": "You are on the trail and the monkey went into the forest. There is nothing around.",
        "wooded area": "You are in a wooded area with lots of little shrubs around.",
        "brick wall":  "You see a big brick wall made of a limestone you see a tomato slice on the side of the wall. The wall has a key hole in the side, nothing else of interest.",
        "bench": "The wall seems to continue on until it abruptly stops and you see a bench with a tissue on it.",
    #path two
        "courtyard": "You find yourself in a courtyard with some dumbbells in the corner and a path forward.",
        "field": "you are in a big field with a rock.",
    #path one
        "brick room": "You are in a brick room with two dores each on one wall, one dore is decorated with stone carvings the other is just made of wood. The room also has a large stone in the middle.",
        "pedestal room": "You enter an empty room with a pedestal in the middle of the room",
    #end
        "cave": "You are in a cave? It has some pickles on the ground, there is a pool of water on your right and the cave continues.",
        "pedestal cave": "You find yourself in another cave with a pedestal in it.",
        "clearing": "You enter a clearing with the monkey in the middle."
    },
    "events": {
    #section one
        #section one
        "trail": {
            "Do nothing.": "Why are you waiting around, the monkey is getting away."
        },
        "wooded area": {
            "Touch the shrub.": "The scrub you touch comes to life and tries to kill you."
        },
        "brick wall": {
            "Mess with the key hole.":  "You fall through the ground.",
            "Use the key.": "The wall opens and you step through."
        },
        "bench": {
            "Pick up the tissue.": "You find a key under the tissue."
        },
    #path two
        "courtyard": {
            "Use the dumbbells to get stronger.":  "You feel stronger."
        },
        "field": {
            "Sit on the rock.":  "you fall through the ground."
        },
    #path one
        "brick room": {
            "Sit on the stone.": "You fell  healthier.",
            "Go to the decorated dore.":  "The dore springs to life and eats you."
        },
        "pedestal room": {
            "Investigate the pedestal.": "The pedestal springs to life and you start fighting."
        },
    #end
        "cave": {
            "Investigate the pool of water.": "You fall into the water."
        },
        "pedestal cave": {
             "investigate the pedestal": "The pedestal springs to life and you start fighting. Wait have we done this before"
        },
        "clearing": {
            "Fight the monkey.": "You walk up to the monkey."
        }
    }
}
events  = {
#section one
    #section one
    "trail": {
        "Do nothing.": [False, False]
    },
    "wooded area": {
        "Touch the shrub.": [False, "battle", "shrub", True]
    },
    "brick wall": {
        "Mess with the key hole.": [False, "move", "brick room", True],
        "Use the key.": [True, "move", "courtyard", True]
    },
    "bench": {
        "Pick up the tissue.": [False, "item", "key", "to", "brick wall", "Use the key.", False, True]
    },
#path two
    "courtyard": {
        "Use the dumbbells to get stronger.": [False, "stat", "strength", 0, True]
    },
    "field": {
        "Sit on the rock.": [False, "move", "cave", True]
    },
#path one
    "brick room": {
        "Sit on the stone.": [False, "stat", "HP", 0],
        "Go to the decorated dore.": [False, "move", "cave", True]
    },
    "pedestal room": {
        "Investigate the pedestal.": [False, "battle", "pedestal", "book", True]
    },
#end
    "cave": {
        "Investigate the pool of water.": [False, "move", "pedestal cave", False]
    },
    "pedestal cave": {
            "investigate the pedestal": [False, "battle", "pedestal", "air fryer", True]
    },
    "clearing": {
        "Fight the monkey.": [False, "battle", "monkey", "win", False]
    }
}
encounters = {
    "pedestal": {
            "entrance":  "You are fighting a living Pedestal.",
            "name": "Pedestal",
            "damage": 0,
            "defense": 0,
            "speed": 0,
            "hp": 0,
            "exit": "The Pedestal returns back to normal and you find something."
    },
    "shrub": {
            "entrance": "You are fighting a living Shrub.",
            "name": "Shrub",
            "damage": 0,
            "defense": 0,
            "speed": 0,
            "hp": 0,
            "exit": "The Shrub bursts into leaves and you find something."
    },
    "brick": {
            "entrance": "A Brick flyers into you and you start fighting.",
            "name": "Brick",
            "damage": 0,
            "defense": 0,
            "speed": 0,
            "hp": 0,
            "exit": "The Brick brakes."
    },
    "leaf": {
            "entrance": "A Leaf flyers into your face. Honestly this is just a joke now.",
            "name": "leaf",
            "damage": 0,
            "defense": 0,
            "speed": 0,
            "hp": 1,
            "exit": "You stomp on the leaf with a satisfying crunch."
    },
    "monkey": {
            "entrance": "you find that the monkey is wearing an amulet. Then you hear rumbling, the earth is shaking and then you see the monkey again but it is wearing a magical suit of glimmering bronze armor. You continue to battle with the monkey.",
            "name": "monkey ",
            "damage": 0,
            "defense": 0,
            "speed": 0,
            "hp": 0,
            "exit": "You punch the monkey and get your sandwich back."
    }
}
movement = {
#section one
    "trail": {
        "Go into the forest.": "wooded area"
    },
    "wooded area": {
        "Go back to the trail.": "trail",
        "Continue into the forest.": "brick wall"
    },
    "brick wall": {
        "Follow the wall.": "bench",
        "Go back into the wooded area.": "wooded area"
    },
    "bench": {
        "Go back to the key hole in the wall.": "brick wall"
    },
#path two
    "courtyard": {
        "Go through the path.": "field"
    },
    "field": {
        "Go back to the courtyard.": "courtyard"
    },
#path one
    "brick room": {
        "Go through the wooden dore.": "pedestal room"
    },
    "pedestal room": {
        "Go back through the dore.": "brick room"
    },
#end
    "cave": {
        "Continue through the cave.": "clearing"
    },
    "pedestal cave": {
        "Go back through the pool of water": "cave"
    },
    "clearing": {
        "Leave": "cave"
    }  
}
chance = {
#section one
    "trail": {
        100: "null"
    },
    "wooded area": {
        75: "null",
        25: "leaf"
    },
    "brick wall": {
        100: "null"
    },
    "bench": {
        100: "null"
    },
#path two
    "courtyard": {
        75: "null",
        25: "brick"
    },
    "field": {
        100: "null"
    },
#path one
    "brick room": {
        75: "null",
        25: "brick"
    },
    "pedestal room": {
        100: "null"
    },
#end
    "cave": {
        100: "null"
    },
    "pedestal cave": {
        100: "null"
    },
    "clearing": {
        100: "null"
    }  
}
player = {
    "hp": 4,
    "speed": 4,
    "strenght": 4,
    "damage": 4,
    "defence": 4,
    "weapon": "stick",
    "items": [],
    "position": "trail",
    "battle text": {
        "light attack": "You hit them fast.",
        "attack": "You hit them.",
        "heavy attack":  "You hit them hard."
    },
    "atacks": {
        "light attack": [4,4],
        "attack": [4,4],
        "heavy attack": [4,4]
    }
}
items = {
    "air fryer": {
        "attack": 4,
        "speed": 4
    },
    "book": {
        "attack": 4,
        "speed": 4
    },
    "key": {
        "attack": 4,
        "speed": 4
    },
    "stick": {
        "attack": 4,
        "speed": 4
    }
}

def damage(damage, damage_multiplier, defence, defence_multiplier):
    attack_damage = m.floor(1+(damage*damage_multiplier)-(1*defence_multiplier**(defence-damage)))
    if attack_damage <= 0:
        return 0
    else:
        return attack_damage
    
def evauateOr(item,*or_items):
    for x in or_items:
        if item == x:
            return True
    return False

def dictionaryItem(list):
    output = {}
    item = 1
    for x in list:
        output[item] = x
        item += 1
    return output


def battle(player_stats, items, enemy_stats):
    while True:
        weapon = items[player_stats["weapon"]]
        temp_defence = 1
        print("\n"+enemy_stats["entrance"])
        if player_stats["speed"] >= enemy_stats["speed"]:
            first = "player"
        else:
            first = "enemy"
        
        if first == "player":
            print("\nYour turn.")
            while True:
                want = input("Do you want to:\t\n1. Attack\t\n2. Defend\n").lower().strip()
                if evauateOr(want,"1","attack"):
                    temp_defence = 1
                    #user input
                    while True:
                        print("What attack do you want to do (number or name):")
                        key_attack = dictionaryItem(player_stats["atacks"].keys())
                        for print_item in key_attack:
                            print(f"\t{print_item}. {key_attack[print_item]}")
                        want = input()
                        try:
                            player_stats["atacks"][want]
                            attack = want
                            break
                        except:
                            try:
                                key_attack[int(want)]
                                attack = key_attack[int(want)]
                                break
                            except:
                                print("Try again.")
                    #attack evauation
                    if enemy_stats["speed"]/5 <= rand.randint(player_stats["speed"]+weapon["speed"],player_stats["atacks"][attack][0]):
                        print(player_stats["battle text"][attack])
                        enemy_stats["hp"] -= damage(player_stats["strenght"]+player_stats["atacks"][attack][1],weapon["attack"],enemy_stats["defense"],1)
                        print(f"The enemy has {enemy_stats["hp"]} HP.")
                    else:
                        print("You mised.")
                    break
                elif evauateOr(want,"2","defend"):
                    print("You are defending.")
                    temp_defence = 1.25
                    break
                else:
                    print("Try again.")
            first = "enemy"
        else:
            print("Enemys turn")
            player_stats["hp"] -= damage(enemy_stats["damage"],1,player_stats["defence"],temp_defence)
            print(f"Your Hp is now {player_stats["hp"]}.")
        if enemy_stats["hp"] <= 0:
            print("You wone.")
            return True
        if player_stats["hp"] <= 0:
            print("You lost")
            return False

def percentage(dictionary):
    chance_list = [0]
    for x in dictionary:
        chance_list.append(chance_list[-1]+x)
    random = rand.randint(chance_list[0],chance_list[-1])
    key_list = []
    for x in dictionary:
        key_list.append(dictionary[x])
    count = 0
    for x in chance_list:
        if random < x: break
        count += 1
    return key_list[count-1]

while True:
    print(text["game"]["start"])
    encounter = percentage(chance[player["position"]])
    if encounter != "null":
        battle(player,items,encounters[encounter])

    while True:
        print("\n"+text["info"][player["position"]])
 
        player_want = input("\nWould you like to do (number or word).\n1. Move\n2. Equip\n3. do something\n").lower().strip()
        if evauateOr(player_want,"1", "move"):

            while True:
                print("\nWere would you like to go.")
                key_move = dictionaryItem(movement[player["position"]].keys())
                for print_items in key_move:
                    print(f"{print_items}. {key_move[print_items]}")
                player_want = input()
                try:
                    position = movement[player["position"]][key_move[int(player_want)]]
                    break
                except:
                    try:
                        position = movement[player["position"]][player_want]
                        break
                    except:
                        print("Try again.")
            player["position"] = position
            encounter = percentage(chance[player["position"]])
            if encounter != "null":
                battle(player,items,encounters[encounter])

        elif evauateOr(player_want,"2", "Equip"):

            while True:
                print(f"\nYou currently have {player["weapon"]} with {items[player["weapon"]]["attack"]} strength and {items[player["weapon"]]["speed"]} speed equiped.")

                player_want = input("You can.\n1: Equip\n2: Go back\n").lower().strip()
                if evauateOr(player_want,"1","equip"):
                    if player["items"] != []:
    
                        while True:
                            print("\nWhat item(s) do you want to equip.")
                            item_num = dictionaryItem(player["items"])
                            for print_items in item_num:
                                print(f"{print_items}. {item_num[print_items]}: with {items[item_num[print_items]]["attack"]} strength and {items[item_num[print_items]]["speed"]} speed")
                            player_want = input()
                            try:
                                player["weapon"] = item_num[int(player_want)]
                                break
                            except:
                                try:
                                    items[player_want]
                                    player["weapon"] = player_want
                                    break
                                except:
                                    print("Try again.")
                        print(f"\nYour new weapon is {player["weapon"]}.")
                        break
                    else:
                        print("You have no items.")
                        break
                elif evauateOr(player_want,"2","go back"):
                    break
                else:
                    print("Try again.")

        elif evauateOr(player_want,"3", "do something"):
    
            while True:
                print("\nWhat do you want to do.")
                events_key = dictionaryItem(events[player["position"]].keys())
                for print_items in events_key:
                    if events[player["position"]][events_key[print_items]][0] == False:
                        print(f"{print_items}: {events_key[print_items]}")
                player_want = input()
                try:
                    interaction = events[player["position"]][events_key[int(player_want)]]
                    events[player["position"]][events_key[int(player_want)]][0] = events[player["position"]][events_key[int(player_want)]][-1]
                    print(text["events"][player["position"]][events_key[int(player_want)]])
                    break
                except:
                    try:
                        interaction = events[player["position"]][player_want]
                        events[player["position"]][player_want][0] = events[player["position"]][player_want][-1]
                        print(text["events"][player["position"]][player_want])
                        break
                    except:
                        print("Try again.")
            if "move" in interaction:
                player["position"] = interaction[interaction.index("move")+1]
            if "item" in interaction:
                player["items"].append(interaction[interaction.index("item")+1])
            if "stat" in interaction:
                player[interaction[interaction.index("stat")+1]] += interaction[interaction.index("stat")+2]
            if "to" in interaction:
                events[interaction[interaction.index("to")+1]][interaction[interaction.index("to")+2]] = interaction[interaction.index("to")+3]
            if "battle" in interaction:
                if battle(player,items,encounters[interaction[interaction.index("battle")+1]]):
                    if "win" in interaction:
                        break
                    elif len(interaction) - interaction.index("battle") == 4:
                        player["items"].append(interaction[interaction.index("item")+2])
        else:
            print("Try again.")
    print(text["game"]["end"])
    player_want = input("would you like to play again.\n1. Yes\n2. No").lower().strip()
    if evauateOr(player_want,"2","no"):
        break