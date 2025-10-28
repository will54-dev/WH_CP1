# Wh 2nd Libraries and Built-In Functions notes
import random
import turtle

number = 7
num = number
def turtle_shape(sides,side_lenght):
    turtle.speed(100*sides)
    num = sides
    while num != 0:
        turtle.forward(side_lenght/sides)
        turtle.right(360/sides)
        num -= 1


random.randbytes(1)
turtle.color("#f56527")
turtle.fillcolor("blue")
turtle.pensize(5)
repeat = 100
while repeat != 0:
    lenght = random.randint(1,250)
    sides_1 = random.randint(3,10)
    rotation = random.randint(1,360)
    turtle.begin_fill()
    turtle_shape(sides_1,lenght)
    turtle.end_fill()
    turtle.penup()
    turtle.right(rotation)
    turtle.forward(lenght+100)
    turtle.pendown()
    repeat -=1


turtle.done()
