# WH 2nd Random Numbers Notes

import random

# examples of random numbers
print(random.random()) #float between 0 and 1
print(random.randint(-256,256))

name = input("what is your name: \n").strip().title()

# randon stat creator
stat_one = random.randint(1,6)+ random.randint(1,6)+ random.randint(1,6)
stat_two = random.randint(1,6)+ random.randint(1,6)+ random.randint(1,6)
stat_three = random.randint(1,6)+ random.randint(1,6)+ random.randint(1,6)
stat_four = random.randint(1,6)+ random.randint(1,6)+ random.randint(1,6)
stat_five = random.randint(1,6)+ random.randint(1,6)+ random.randint(1,6)
stat_six = random.randint(1,6)+ random.randint(1,6)+ random.randint(1,6)
stat_seven = random.randint(1,6)+ random.randint(1,6)+ random.randint(1,6)

print(f"your stats options are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}, {stat_seven}")

strenght = int(input("which stat are you making your strangth: \n")) + 2