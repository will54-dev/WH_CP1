# Wh 2nd maze genorator 

#impors 
#imppot tutle of the drawing 
#import random to randomly genorate the maze

#the variables
#the pixel scaile the maze size 
#the x lenght 
#the y length
#the side walls x
#the vetical walls y

#the functions

#a fuction that takes: the the y or x lenght, the x or y length, and hole
    #if hole is true
        #set a nother disposibal variable as a 1 list as 0
        #set x or y length to sumthing disposible - 1
        #a loop that repeats x or y length disposible
                #add a 1 to the 1 list 
        #makeing the loop stop
        #set an output veriable to 1 list 
    #else 
        #set a nother disposibal variable as a 1 list as empty
        #set x or y length to sumthing disposible
        #a loop that repeats x or y length disposible
                #add a 1 to the 1 list 
        #makeing the loop stop
        #set an output veriable to 1 list 
        #set an output veriable to a line with out a hole in it

    #set y or x length to sumthing disposible
    #a loop that repeats y or x length disposible
        #set x or y length to sumthing disposible
        #a loop that repeats x or y length disposible
                #set a nother disposibal variable as a 1 list as empty
                #add a random number of 0-1 to the 1 list 
        #makeing the loop stop
        #add 1 list to output
    #makeing the loop stop

    #if hole is true
        #set a nother disposibal variable as a 1 list as empty
        #set x or y length to sumthing disposible - 1
        #a loop that repeats x or y length disposible
                #add a 1 to the 1 list 
        #makeing the loop stop
        #add 0 to 1 list
        #set an output veriable to 1 list 
    #else 
        #set a nother disposibal variable as a 1 list as empty
        #set x or y length to sumthing disposible
        #a loop that repeats x or y length disposible
                #add a 1 to the 1 list 
        #makeing the loop stop
        #set an output veriable to 1 list 
        #set an output veriable to a line with out a hole in it

    #outputs output

#a function tha checkers if it is solvable takes: side walls x, #the vetical walls y, start, and stop
    #set checked positions 
    #set check item to start

    #loop
        #if y item [check item [0 of 0]] of [check item [0 of 1]] is 0 and, check item [0 of 0] - 1 > or = 0
            #add check item [0 of 0] and check item [0 of 1] - 1

        #if x item [check item [0 of 1] + 1] of [check item [0 of 0]] is 0 and, check item [0 of 0] - 1 < or = lenght side walls x
            #add check item [0 of 0] and check item [0 of 1] - 1

        #if y item [check item [0 of 0] + 1] of [check item [0 of 1]] is 0 and, check item [0 of 0] - 1 < or = lenght side walls y
            #add check item [0 of 0] and check item [0 of 1] - 1

        #if x item [check item [0 of 1]] of [check item [0 of 0]] is 0 and, check item [0 of 0] - 1 > or = 0
            #add check item [0 of 0] and check item [0 of 1] - 1

        #check item remove item 0
        #if check item in stop
            #output True
        #if check item is empty 
            #output false

# a function that draws the maze needs: distance , side walls x, and the vetical walls y
#set count y to 0
# #set count x to 0
    #loop for walls x in side walls x
        #loop for wall in side  walls x
            #if side walls x itme count x of count y
            #move the turtle distance 
            #add 1 to count y
        #add 1 to count x