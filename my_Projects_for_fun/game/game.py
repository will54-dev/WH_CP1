# WH 2nd a game

data_file = "my_Projects_for_fun/game/game.txt"
line_1 = "***************"
line_2 = "***************"
line_3 = "*******#*******"
line_4 = "***************"
line_5 = "***************"
x = 0
y = 0
isopen = True
while isopen:
    with open(data_file, 'w') as file:
        content = file.write("")
    with open(data_file, 'r') as file:
        content = file.read()
        for wasd in content:
            if wasd in "w":
                y += 1
            if wasd in "s":
                y -= 1
            if wasd in "a":
                x -= 1
            if wasd in "d":
                x += 1
            if wasd in "o":
                isopen = False
        print(x)
        print(y)
    