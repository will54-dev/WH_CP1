# Wh 2nd flexible caculator

# define a function for sum
def allSum(*imput):
    #set sum to 0
    sum = 0
    #loop for item in a imput
    for item in imput:
        #if item is an number add item to sum
        if isinstance(item, (float,int)): sum += item
    #output sum
    return sum

# define a function for avreg
def avrag(*imput):
    #set sum to 0
    sum = 0
    #set count to 0
    count = 0
    #loop for item in imput
    for item in imput:
        #if it is an number and it to sum
        if isinstance(item, (float,int)): sum += item
        #add 1 to count
        count += 1
    #output sum devided by count
    return sum/count

# define a function for producut
def product(*imput):
    #set pr to 1
    pr = 1
    #loop for item in imput
    for item in imput:
        #mutiply pr to item if it is a number
        if isinstance(item, (float,int)): pr *= item
    #output pr
    return pr

# main loop
while True:
    #pmt the user to pick an oporation
    want = input("pick one.\n1. sum\n2. Average\n3. max\n4. min\n5. product\n 6.exit")

    #if the user pickes sum
    if want == "1" or want == "sum"
    #set numbers as a list
    #show that they can imput numbers and done to finish
        #loop
            #set num to input
            #if number is an interger and has only one .
                #add num to numbers
            #if num is done
                #break
            #else 
                #show not a number

