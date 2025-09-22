# wh 2ND Conditionals Notes

import random as k

monster_hp = 20
dmg_mod = 2
atk_bone = 3
roll = k.randint(1,20)
player_hp = 1

if roll == 20:  
    print("you eoiied a crit! double your damage")
    atack = k.randint(1,8) + k.randint(1,8) + dmg_mod
    monster_hp -= atack
    print(f"you did {atack} damage to the monster")
elif roll+atk_bone > 10:
    print("you hit")
    attack = k.randint(1,8) + dmg_mod
    monster_hp -= attack
    print(f"you did {attack} damage to the monster")
elif roll <= 10: 
    if roll == 1:
        print("you rollad a critical failure! The monster gets a free attack")
        damage = (k.randint(1,10) + 2)
        player_hp -= damage
        print(f"you took {damage} damage you now have {player_hp} HP")
    else:
        print("you missed")
else: 
    print("y")
