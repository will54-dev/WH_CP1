# Wh 2nd turtle race program

#imports
import turtle
import random

#functions
#turtle set up function needs position, color, and speed
def turtle_set(color,x_position,y_posirion):
    #sets the turtle
    name = turtle.Turtle()
    #sets the color
    name.color(color)
    #sets the shape
    name.shape("turtle")
    #sets the speed
    name.speed(1)
    #set the position
    name.teleport(y_posirion,x_position)
    #exports the turtle
    return name

# a function that doos the movment of the turtle
def turtle_move(name,rand):
    #set the amount it moves
    move = random.randint(20,rand)
    #moves int that amount
    name.forward(move)


#code
#set up the turtles and hide some
t0 = turtle_set("black",250,300)
t0.hideturtle()
t1 = turtle_set("red",200,-300)
t2 = turtle_set("green",150,-300)
t3 = turtle_set("blue",100,-300)
t4 = turtle_set("yellow",50,-300)
t5 = turtle_set("purple",0,-300)
#make t0 draw the finsih line
t0.right(90)
t0.forward(300)
#make the turles run
#loop
loop = True
while loop:
    #moves all the turtles
    #loop for t1, t2, t3, 4, t5 as a var
    for var in [t1,t2,t3,t4,t5]:
        #uses turtle move wite the var as name and a random and rand
        turtle_move(var, 40)
        #check if the turtle won
        if var.xcor() >= t0.xcor():
            var.forward(400)
            #show winer
            print(f"{var.color()[1]} is the winner")
            #ends the loops
            loop = False
            break