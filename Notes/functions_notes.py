# WH 2nd function notes
# all imports
# set global variables 
num = 0
player_hp = 20
monster_hp = 30
game_turn = 1

# set functions 
def add(x, y):
    return x+y
print(add(45,79))
print(add(100,63))
print(add(84,70))

def initials(name):
    names = name.split(" ")
    initial = ""
    for name in names:
        initial += name[0]
    return initial

def attack(dmg, turn):
    if turn == 1:
        if monster_hp - dmg > 0:
            return monster_hp - dmg
        else:
            return 0
    else:
        if player_hp - dmg > 0:
            return player_hp - dmg
        else:
            return 0

# then write your code
while num < add(5,5):
    print("Duck")
    num += 1
print("goose")

print(add(213,add(672954578213,75884545)))

print(f"your initials are: {initials("Will Jeff")}")
print(f"your initials are: {initials("Bob Jeff")}")
if game_turn == 1:
    monster_hp = attack(4, game_turn)
else:
    player_hp = attack(4, game_turn)
print(f"you have {player_hp} HP.")
print(f"the monster has {monster_hp} HP.")