# Wh 2nd maze genorator 

#impors 
#impot turtle of the drawing
import turtle 
#import random to randomly genorate the maze
import random

#the functions

#a fuction that takes: the the y or x length, the x or y length, and hole
def wallRandom(length_1,length_2,hole):
    #set output
    output = []
    #if hole is true
    if hole:
        #set another disposibal variable as a 1 list as 0
        list = [0]
        #set x or y length to sumthing disposible - 1
        length = length_2 - 1
        #a loop that repeats x or y length disposible
        while length != 0:
            #add a 1 to the 1 list 
            list.append(1)
            #makeing the loop stop
            length -= 1
        #set an output veriable to 1 list 
        output.append(list)
    #else
    else:
        #set another disposibal variable as a 1 list as empty
        list = []
        #set x or y length to sumthing disposible
        length = length_2
        #a loop that repeats x or y length disposible
        while length:
            #add a 1 to the 1 list 
            list.append(1)
            #makeing the loop stop
            length -= 1
        #set an output veriable to 1 list
        output.append(list)

    #set y or x length to sumthing disposible
    length_1d = length_1 -1
    #a loop that repeats y or x length disposible
    while length_1d != 0:
        #set x or y length to sumthing disposible
        length_2d = length_2
        #set list 1 as empty
        list = []
        #a loop that repeats x or y length disposible
        while length_2d != 0:
            #add a random number of 0-1 to the list 2
            list.append(random.randint(0,1))
            #makeing the loop stop
            length_2d -= 1
        #add 1 list to output
        output.append(list)
        #makeing the loop stop
        length_1d -= 1

    #set disposibal variable as a 1 list as empty
    list = []
    #if hole is true
    if hole:
        #set x or y length to sumthing disposible - 1
        length = length_2 - 1
        #a loop that repeats x or y length disposible
        while length != 0:
            #add a 1 to the 1 list
            list.append(1)
            #makeing the loop stop
            length -= 1
        #add 0 to 1 list
        list.append(0)
        #add to output veriable 1 list
        output.append(list)
    #else
    else:
        #set x or y length to sumthing disposible
        length = length_2
        #a loop that repeats x or y length disposible
        while length != 0:
            #add a 1 to the 1 list
            list.append(1)
            #makeing the loop stop
            length -= 1
        #set an output veriable to 1 list 
        output.append(list)

    #outputs output
    return output

#a function tha checkers if it is solvable takes: side walls x, #the vetical walls y, start, and stop
def checkMaze(side_x,vetical_y,start,stop):
    #set checked positions
    checked = []
    #set check item to start
    item = [start]

    #loop
    while True:
            
        #the item
        check = [item[0][0] -1,item[0][1]]
        #if it is not in checked
        if check not in checked:
            #if y item is moveable
            if check[0] >= 0 and vetical_y[item[0][0]][item[0][1]] == 0:
                #add check item [0 of 0] and check item [0 of 1] - 1
                item.append(check)

        #the item
        check = [item[0][0],item[0][1]+1]
        #if it is not in checked
        if check not in checked:
            #if x item is moveable
            if check[1] <= len(side_x) -2 and side_x[item[0][1] +1][item[0][0]] == 0:
                #add check item [0 of 0]  + 1 and check item [0 of 1]
                item.append(check)

        #the item
        check = [item[0][0] +1,item[0][1]]
        #if it is not in checked
        if check not in checked:
            #if y item is moveable
            if check[0] <= len(vetical_y) -2 and vetical_y[item[0][0] +1][item[0][1]] == 0:
                #add check item [0 of 0] and check item [0 of 1] + 1
                item.append([item[0][0] +1,item[0][1]])

        #the item
        check = [item[0][0],item[0][1] -1]
        #if it is not in checked
        if check not in checked:
            #if x item is moveable
            if check[1] >= 0 and side_x[item[0][1]][item[0][0]] == 0:
                #add check item [0 of 0] -1 and check item [0 of 1] -1
                item.append(check)

        #add check item to checked positions
        checked.append(item[0])
        #check item remove item 0
        item.pop(0)
        #if check item in stop
        if stop in item:
            #output True
            return True
        #if check item is empty 
        elif item == []:
            #output false
            return False

# a function that draws the maze needs: distance , side walls x, and the vetical walls y
def mazeDraw(distance,side_x,vetical_y,start):
    #teloport to starting postioion
    turtle.teleport(start[0],start[1])

    #loop for walls x in side walls x
    for x in side_x:
        #set count to 0
        count = 0
        #loop for wall in side  walls x
        for wall in x:
            #if wall is 1
            if wall == 1:
                #tutle pen down
                turtle.pendown()
                #move the turtle distance
                turtle.forward(distance)
            #if wall is 0
            else:
                #tutle pen up
                turtle.penup()
                #move the turtle distance'
                turtle.forward(distance)
            #add 1 to count
            count += 1
        #teloport the turtle up distance and left count * distance
        turtle.teleport(turtle.xcor() - count * distance,turtle.ycor() + distance)

    #teloport to starting postioion
    turtle.teleport(start[0],start[1])
    #rotate the tutle left 90
    turtle.left(90)
    #loop for walls y in side walls y
    for x in vetical_y:
        #set count to 0
        count = 0
        #loop for wall in side  walls y
        for wall in x:
            #if wall is 1
            if wall == 1:
                #tutle pen down
                turtle.pendown()
                #move the turtle distance
                turtle.forward(distance)
            #if wall is 0
            else:
                #tutle pen up
                turtle.penup()
                #move the turtle distance
                turtle.forward(distance)
            #add 1 to count
            count += 1
        #theloport th turtle left distance and down count * distance
        turtle.teleport(turtle.xcor() + distance,turtle.ycor() - count * distance)

#code
#seting the size
#the x length and checking if a number
while True:
    x_len = input("How long do you want it.\n")
    if x_len.isnumeric():
        x_len = int(x_len)
        if x_len <= 40:
            break
        print("Too big.")
    else:
        print("Not a valid number.")

#the y length
while True:
    y_len = input("How tall do you want it.\n")
    if y_len.isnumeric() and y_len < 40:
        y_len = int(y_len)
        if y_len <= 40:
            break
        print("Too big.")
    else:
        print("Not a valid number.")

#the pixel scaile the maze size
size = 500/x_len

#seting the walls
wall_x = wallRandom(y_len,x_len,True)
wall_y = wallRandom(x_len,y_len,False)
#checking if the walls are good
while not checkMaze(wall_x,wall_y,[0,0],[x_len-1,y_len-1]):
    #reseting the walls
    wall_x = wallRandom(y_len,x_len,True)
    wall_y = wallRandom(x_len,y_len,False)

#draw ing the maze
mazeDraw(size,wall_x,wall_y,[size*x_len/-2,size*y_len/-2])

#making the maze stay
turtle.done()