# Wh 2nd turtle race program

#imports
import turtle
import random

#functions
#turtle set up function needs position, color, and speed
def turtle_set(color,position):
    #sets the turtle
    name = turtle.Turtle()
    #sets the color
    name.color(color)
    #sets the shape
    name.shape("turtle")
    #sets the speed
    name.speed(100)
    #set the position
    name.teleport(0,position)
    #exports the turtle
    return name

#code
#set up the turtles with difrent speeds and hide some
t0 = turtle_set("black",1000,250)
t0.hideturtle()
t1 = turtle_set("red",random.randint(100,200),200)
t2 = turtle_set("green",random.randint(70,210),150)
t3 = turtle_set("blue",random.randint(50,170),100)
t4 = turtle_set("yellow",random.randint(60,200),50)
t5 = turtle_set("purple",random.randint(80,190),0)
#make a turtle 0 move to the end
t0.teleport(300,t0.ycor())
#make him draw the finsih line
t0.right(90)
t0.forward(300)
#make the turles run
t1.forward(300)
t2.forward(300)
t3.forward(300)
t4.forward(300)
t5.forward(300)
#if the turtle 1 x position = turtle 0 x position
    #display turtle 1 a the winer
#if the turtle 2 x position = turtle 0 x position
    #display turtle 1 a the winer
#if the turtle 3 x position = turtle 0 x position
    #display turtle 1 a the winer
#if the turtle 4 x position = turtle 0 x position
    #display turtle 1 a the winer
#if the turtle 5 x position = turtle 0 x position
    #display turtle 1 a the winer

turtle.done()