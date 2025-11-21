#WH 2nd draw pictur

import turtle

def draw_branch(len):
    if len > 5:
        for i in range(3):
            turtle.forward(len)
            draw_branch(len/3)
            turtle.backward(len)
            turtle.right(60)

turtle.speed(100)
turtle.color("light blue")
turtle.penup()
turtle.backward(250)
turtle.pendown()

for i in range(6):
    draw_branch(100)
    turtle.right(60)

turtle.hideturtle()