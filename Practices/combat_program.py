# WH 2nd combat program

import random

damage = 0
defence = 0
health = 0
speed = 0

def isint(str):
    try:
        int(str)
        return True
    except:
        return False
    
def attack(defence_a, damage_a):
    if damage_a > defence_a:
        return damage_a - defence_a
    else:
        return 0
    
class_points = 100
while True:
    whant = input(f"you have {class_points} class points to spend on:\n\t1. Damage\n\t2. Defence\n\t3. Health\n\t4. Speed\n\t5. Done\n")
    
    if whant == "1":
        print(f"your damage is {damage}.")
        spend = input(f"How many points do you whant to spend ({class_points})?\n\t")
        if isint(spend):
            spend = int(spend)
            if spend > class_points or spend < -1*damage:
                print("Not valid.\n")
            else:
                damage += spend
                class_points -= spend
                print(f"your damage is now {damage}.")
        else:
            print("not a number.\n")

    elif whant == "2":
        print(f"your defence is {defence}.")
        spend = input(f"How many points do you whant to spend ({class_points})?\n\t")
        if isint(spend):
            spend = int(spend)
            if spend > class_points or spend < -1*defence:
                print("Not valid.\n")
            else:
                defence += spend
                class_points -= spend
                print(f"your defence is now {defence}.")
        else:
            print("not a number.\n")

    elif whant == "3":
        print(f"your health is {health}.")
        spend = input(f"How many points do you whant to spend ({class_points})?\n\t")
        if isint(spend):
            spend = int(spend)
            if spend > class_points or spend < -1*health:
                print("Not valid.\n")
            else:
                health += spend
                class_points -= spend
                print(f"your health is now {health}.")
        else:
            print("not a number.\n")

    elif whant == "4":
        print(f"your speed is {speed}.")
        spend = input(f"How many points do you whant to spend ({class_points})?\n\t")
        if isint(spend):
            spend = int(spend)
            if spend > class_points or spend < -1*speed:
                print("Not valid.\n")
            else:
                speed += spend
                class_points -= spend
                print(f"your speed is now {speed}.")
        else:
            print("not a number.\n")
    elif whant == "5":
        break
    else:
        print("As a valid imput.\n")

enemy = random.randint(1,5)
enemy_damage = random.randint(-10,10)
enemy_defence = random.randint(-10,10)
enemy_health = random.randint(-10,10)
enemy_speed = random.randint(-10,10)

if enemy == 1:
    enemy = "Bob"
    enemy_damage += 40
    enemy_defence += 40
    enemy_health += 40
    enemy_speed += 20

elif enemy == 2:
    enemy = "Kev"
    enemy_damage += 20
    enemy_defence += 30
    enemy_health += 10
    enemy_speed += 50

elif enemy == 3:
    enemy = "Meb"
    enemy_damage += 30
    enemy_defence += 30
    enemy_health += 30
    enemy_speed += 30

elif enemy == 4:
    enemy = "Jeff"
    enemy_damage += 40
    enemy_defence += 10
    enemy_health += 60
    enemy_speed += 20

else:
    if random.randint(1,10) != 1:
        enemy = "You?"
        enemy_damage += damage
        enemy_defence += defence
        enemy_health += health
        enemy_speed += speed
    else:
        enemy = "Run!!"
        enemy_damage += 200
        enemy_defence += 200
        enemy_health += 200
        enemy_speed += 200

print(f"you are fighting {enemy}.")
while True:
    if speed > enemy_speed:
        print(f"you are first.")
        turn = 1
        break
    elif speed < enemy_speed:
        print(f"{enemy} is first.")
        turn = 2
        break
    else:
        enemy_speed += 1

temdefence = defence
while True:
    if damage == 0:
        print("you don't hav enough attack")
        break
    if turn == 1:
        temdefence = defence
        while True:
            combat = input("\nYou can.\n\t1.attack\n\t2.defend\n\t3.check\n")
            if combat == "1":
                enemy_health -= attack(enemy_defence,damage)
                enemy_defence -= 5
                if enemy_defence < 0:
                    enemy_defence = 0
                print(f"{enemy} is at {enemy_health} health.")
                print(f"{enemy}'s turn")   
                break
            elif combat == "2":
                temdefence = defence + 10
                print(f"Your defence is now {defence + 10}")
                print(f"{enemy}'s turn")  
                break
            elif combat == "3":
                print(f"{enemy} has:\n{enemy_damage} damage\n{enemy_defence} defence\n{enemy_health} health\n{enemy_speed} speed")
            else:
                print("Not a valid input.")
        if enemy_health <= 0:
            print("You win.")
            break
        turn = 2
    else:
        if random.randint(1,500) <= speed:
            print(f"{enemy} missed.")
        else:
            health -= attack(temdefence,enemy_damage)
            print(f"You are now at {health} health.")
        if health <= 0:
            print(f"{enemy} won.")
            break
        turn = 1