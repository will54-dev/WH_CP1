# WH 2nd caeser cipher program

# define a function that can ofset a letter by a number
def caeserOffSet(letter,off_set):
    # set Num to Off_set
    num = off_set
    # repeat for evry lower case letter and set Let to the curent letter
    for let in "bcdefghijklomnpqrstuvwxyza":
        # add one to Num
        num += 1
        # check if Letter = Let
        if letter == let:
            # give an output of num but is loops around from 26 and add 27 num but is loops around from 26
            return num%26 + 1
    # repeat for evry upper case letter and set Let to the curent letter
    for let in "BCDEFGHIJKLOMNPQRSTUVWXYZA":
        # add one to Num
        num += 1
        # check if Letter = Let
        if letter == let:
            # give an output of num but is loops around from 26 and add 27
            return num%26 + 27
    # keeps nonletters
    return letter

# define a function that can make a number in to a letter
def numToLetter(number):
    # set Num to 0
    num = 0
    # repeat for evry lower and upper case letter and set Let to the curent letter
    for let in "abcdefghijklomnpqrstuvwxyzABCDEFGHIJKLOMNPQRSTUVWXYZ":
        # add one to Num
        num += 1
        # check if Number = Num
        if number == num:
            # return Let
            return let
    # keeps nonnumbers
    return number

# defines a function that encodes a masage
def encode(message,off_set):
    # set Fine_message as a string
    fine_message = ""
    # a loop of each letter in in Message and the letter is Let
    for let in message:
        #add function numToLetter with function caeserOffSet with Letter as let and Off_set and Off_set as Number to Fine_message
        fine_message += numToLetter(caeserOffSet(let,off_set))
    #return fine_massage
    return fine_message

# defines a function that decodes a masage
def decode(message,off_set):
    # just encoder but a negative value
    return encode(message,-1*off_set)

#loop for the program
while True:
    #ask the user for what they want to do
    while True:
        try:
            want = int(input("\n1. Encode\n2. Decode\n3. Exit\n"))
            break
        except:
            print("Not a number.")

    #if user wants to encode 
    if want == 1:
        #ask for the message
        message = input("\nWhat message do you want to encode: ")
        #ask for the off set
        while True:
            try:
                off_set = int(input("What off set do you want: "))
                break
            except:
                print("Not a number.")
        #show encoded with the message and off set
        print(f"\n{encode(message,off_set)}")
    #if user wants to decode
    elif want == 2:
        #ask for the message
        message = input("\nWhat message do you want to decode: ")
        #ask for the off set
        while True:
            try:
                off_set = int(input("What off set do you want: "))
                break
            except:
                print("Not a number.")
        #show decoded with the message and off set
        print(f"\n{decode(message,off_set)}")
    #if user wants to exit
    elif want == 3:
        #exit loop
        break
    else:
        print("Not a option.")