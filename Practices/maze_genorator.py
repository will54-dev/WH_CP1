#Wh 2nd maze genorator

#imports
#import turtle
import turtle
#import randon
import random


#deine a function that turns letters into numbers
def maze_part(name,letter,distance):
    #lots of if statmests that take letters and meaks peaces out of them
        #the strates peces
    #makeing I1 into up strate
    if letter == "i1":
        #makes the maze part
        name.forward(distance)
        name.teleport(name.xcor()+distance,name.ycor()-distance)
        name.forward(distance)
        name.teleport(name.xcor()-distance,name.ycor()-distance)
    #makeing i2 into side strate
    if letter == "i2":
        #makes the maze part
        name.right(90)
        name.forward(distance)
        name.teleport(name.xcor()-distance,name.ycor()+distance)
        name.forward(distance)
        name.left(90)
        name.teleport(name.xcor()-distance,name.ycor()-distance)

        #the coners
    #makeing L1 into up left coners
    if letter == "l1":
        #makes the maze part
        name.teleport(name.xcor()+distance,name.ycor())
        name.forward(distance)
        name.left(90)
        name.forward(distance)
        name.right(90)
        name.teleport(name.xcor(),name.ycor()-distance)
    #makeing L2 into up right coners
    if letter == "l2":
        #makes the maze part
        name.forward(distance)
        name.right(90)
        name.forward(distance)
        name.left(90)
        name.teleport(name.xcor()-distance,name.ycor()-distance)
    #makeing L3 into down left coners
    if letter == "l3":
        #makes the maze part
        name.teleport(name.xcor()+distance,name.ycor()+distance)
        name.right(180)
        name.forward(distance)
        name.right(90)
        name.forward(distance)
        name.right(90)
    #makeing L4 into down right coners
    if letter == "l4":
        #makes the maze part
        name.teleport(name.xcor(),name.ycor()+distance)
        name.left(180)
        name.forward(distance)
        name.left(90)
        name.forward(distance)
        name.left(90)
        name.teleport(name.xcor()-distance,name.ycor())

        #the Ts
    #makeing T1 into up srate left
    if letter == "t1":
        #makes the maze part
        name.teleport(name.xcor()+distance,name.ycor())
        name.forward(distance)
        name.teleport(name.xcor()-distance,name.ycor()-distance)
    #makeing T2 into up srate right
    if letter == "t2":
        #makes the maze part
        name.forward(distance)
        name.teleport(name.xcor(),name.ycor()-distance)
    #makeing T3 into side srate up
    if letter == "t3":
        #makes the maze part
        name.teleport(name.xcor(),name.ycor()+distance)
        name.right(90)
        name.forward(distance)
        name.left(90)
        name.teleport(name.xcor()-distance,name.ycor()-distance)
    #makeing T4 into side srate down
    if letter == "t4":
        #makes the maze part
        name.right(90)
        name.forward(distance)
        name.left(90)
        name.teleport(name.xcor()-distance,name.ycor())

        # the x
    #makeing x in to open
        #makes the maze part
        #h nothing

