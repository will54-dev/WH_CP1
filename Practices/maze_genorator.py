# Wh 2nd maze genorator 

#impors 
#impot turtle of the drawing
import turtle 
#import random to randomly genorate the maze
import random

#the variables
#the pixel scaile the maze size
size = 100
#the x length
x_len = 4
#the y length
y_len = 6
#the side walls x
wall_x = []
#the vetical walls y
wall_y = []

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
    length_1d = length_1
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
        #if y item [check item [0 of 0]] of [check item [0 of 1]] is 0 and, check item [0 of 0] - 1 >= 0
        if vetical_y[item[0][0]][item[0][1]] == 0 and item[0][0] -1 >= 0:
            #add check item [0 of 0] and check item [0 of 1] - 1
            item.append([item[0][0],item[0][1]-1])

        #if x item [check item [0 of 1] + 1] of [check item [0 of 0]] is 0 and, check item [0 of 0] - 1 <= length side walls x
        if vetical_y[item[0][1] + 1][item[0][0]] == 0 and item[0][1] -1 <= 0:
            #add check item [0 of 0]  + 1 and check item [0 of 1]
            item.append([item[0][0] + 1 ,item[0][1]])

        #if y item [check item [0 of 0] + 1] of [check item [0 of 1]] is 0 and, check item [0 of 0] - 1 <= length side walls y
            #add check item [0 of 0] and check item [0 of 1] - 1

        #if x item [check item [0 of 1]] of [check item [0 of 0]] is 0 and, check item [0 of 0] - 1 >= 0
            #add check item [0 of 0] and check item [0 of 1] - 1

        #check item remove item 0
        #if check item in stop
            #output True
        #if check item is empty 
            #output false

# a function that draws the maze needs: distance , side walls x, and the vetical walls y

    #start sets this to be able to senter the maze

    #loop for walls x in side walls x
        #set count to 0
        #loop for wall in side  walls x
            #if wall is 1
                #tutle pen down
                #move the turtle distance
            #if wall is 0
                #tutle pen up
                #move the turtle distance
            #add 1 to count
        #teloport the turtle up distance and left count * distance

    #teloport to starting postioion

    #rotate the tutle left 90
    #loop for walls y in side walls y
        #set count to 0
        #loop for wall in side  walls y
            #if wall is 1
                #tutle pen down
                #move the turtle distance
            #if wall is 0
                #tutle pen up
                #move the turtle distance
            #add 1 to count
        #theloport th turtle up distance and left count * distance

print(wallRandom(y_len,x_len,True))
print(wallRandom(x_len,y_len,False))
