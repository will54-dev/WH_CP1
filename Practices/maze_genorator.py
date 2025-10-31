#Wh 2nd maze genorator

#imports
#import turtle
import turtle
#import randon
import random

turtle.forward()
turtle.right()
turtle.teleport(turtle.xcor(),turtle.ycor())


#deine a function that turns letters into numbers
def maze_part(name,letter,distance):
    #lots of if statmests that take letters and meaks peaces out of them
        #the strates peces
    #makeing I1 into up strate
    if letter == "i1":
        name.right(90)
        name.forward(distance)
        turtle.teleport(turtle.xcor()-distance,turtle.ycor()+distance)
        name.forward(distance)
        turtle.left(90)
    #makeing i2 into side strate
    if letter == "i2":
        #the coners
    #makeing L1 into up left coners
    if letter == "l1":
    #makeing L2 into up right coners
    if letter == "l2":
    #makeing L3 into down left coners
    if letter == "l3":
    #makeing L4 into down right coners
    if letter == "l4":
        #the Ts
    #makeing T1 into up srate left
    if letter == "t1":
    #makeing T2 into up srate right
    if letter == "t2":
    #makeing T3 into side srate up
    if letter == "t3":
    #makeing T4 into side srate down
    if letter == "t4":
        # the x
    #makeing F into side srate down
    if letter == "x":